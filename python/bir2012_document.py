"""
    example document - demonstrate how 'Document as Code' works
"""

from __future__ import absolute_import
from __future__ import print_function

import datetime
import sys

from yattag import indent

from domain.bir.model.bir_measure import BirMeasure
from domain.bir.content.bir_measures import NotApplicable, Explained

from domain.bir2012 import BIR2012 as BIR

from format.bootstrap import BootstrapDoc


doc, tag, text = BootstrapDoc().tagtext()


# --- document preparation ---

# fake measure to flag absence of true measure and to ease rendering
TODO = BirMeasure("TODO", "Things left todo", identifiers=[])


def link_measures_to_fragments(fragment):
    """
    link defined measures to a fragment and its subfragments
    each measure relates to fragments through the identifiers used for those fragments
    here that symbolic reference is turned into actual object references
    :param fragment: fragment to start with
    :return: measures assigned to this fragment
    """

    # augment fragment with measures defined for it
    fragment.bir_measures = set()

    # depth first collection of measures defined for subfragments
    for subfragment in fragment.fragments:
        fragment.bir_measures.update(link_measures_to_fragments(subfragment))

    # post visit processing to add all measures defined for this fragment
    fragment.bir_measures.update(BirMeasure.all_applicable_to_fragment(fragment.identifier))

    # no measures implicates we still have work to do
    if not fragment.bir_measures:
        fragment.bir_measures.add(TODO)
        # provide identification for missing stuff
        print('        "{}",'.format(fragment.identifier))

    return fragment.bir_measures


# --- label rendering ---

def measure_to_label_data(measure):
    """
    create a label for a measure
    both the label text and its visual level determined from the measure and its state
    :param measure: the measure
    :return: label text, visual level
    """

    if measure is NotApplicable:
        return 'nvt', 'primary'

    if measure is Explained:
        return 'explain', 'info'

    if measure is TODO:
        return 'todo', 'danger'

    # regular measure - is it done already?

    if not measure.done:
        return measure.identifier, 'warning'

    return measure.identifier, 'success'


def turn_measures_into_label_data(measures):
    """
    determine correct presentation of a collection of measures
    computes the labels for the measures and sorts them in proper order
    :param measures: the measures
    :return: list of labels (label text, visual level)
    """

    # sort order of measures
    special_measure_sort_order = {
        TODO:          1,
        Explained:     7,
        NotApplicable: 9,
    }
    regular_measure_sort_order = 3

    return [
        measure_to_label_data(measure)
        for measure in sorted(
            measures, key=lambda m: (special_measure_sort_order.get(m, regular_measure_sort_order), m.identifier)
        )
    ]


def turn_label_data_into_labels(labels_data):
    """
    turns a list of labels into a list of formatted labels
    :param labels_data: list of labels (label text, visual level)
    :return: list of formatted labels
    """

    label_style = "font-size:11px"

    return [doc.label(txt, lvl, style=label_style) for txt, lvl in labels_data]


def turn_measures_into_labels(measures):
    """
    turn a collection of measures into a properly sorted list of formatted labels for those measures
    :param measures: the measures
    :return: list of formatted labels
    """

    labels_data = turn_measures_into_label_data(measures)

    return turn_label_data_into_labels(labels_data)


# --- generic fragment rendering ---

def render_fragment(fragment, h, render_sub_level=None):
    """
    render a document fragment
    :param fragment: the fragment
    :param h: heading renderer
    :param render_sub_level: optional renderer for next fragment level
    """

    labels = turn_measures_into_labels(fragment.bir_measures)

    h(fragment.get_title(), ''.join(labels))

    if fragment.lead:
        doc.p(fragment.lead, klass='lead')
    if fragment.text:
        doc.p(fragment.text)
    if render_sub_level:
        for subfragment in fragment.fragments:
            render_sub_level(subfragment)


# --- specific document part renderers ---

# ---- main document ----

def render_measures(measures):
    """
    render the measures linked to a document part (i.e. a fragment)
    :param measures: the measures
    :return: list of formatted labels
    """

    return turn_measures_into_labels(measures)


def render_norm(norm):
    """
    render a norm
    a norm contains an introductory text followed by some verifiers
    :param norm: the norm
    """

    render_fragment(norm, doc.h3)
    doc.table(
        ('Ref', 'Verifier', 'Status'),
        [
            (
                doc.bookmark(verifier.identifier),
                verifier.text,
                render_measures(verifier.bir_measures)
            )
            for verifier in norm.fragments
        ]
    )


def render_section(section):
    """
    render a section
    a section is a fragment that contains norms
    :param section: the section
    """
    render_fragment(section, doc.h2, render_norm)


def render_chapter(chapter):
    """
    render a chapter
    a chapter is a fragment that contains sections
    :param chapter: the chapter
    """
    render_fragment(chapter, doc.h1, render_section)


def render_document(document):
    """
    render a document
    a document is a fragment that contains chapters
    :param document: the document
    """
    render_fragment(document, doc.h1, render_chapter)


# ---- index document parts ----

def render_verifiers_with_state(label, verifiers):
    """
    render a collection of verifiers
    :param label: label of the collection
    :param verifiers: the verifiers
    """
    doc.h2(label, doc.badge(len(verifiers)))

    if verifiers:
        doc.table(
            ('Ref', 'Verifier', ''),
            [
                (
                    doc.bookmark(verifier.identifier),
                    verifier.text,
                    render_measures(
                        [
                            measure
                            for measure in verifier.bir_measures
                            # a verifier may appear in multiple measures
                            # it may therefore also be mapped onto on of the special measures
                            # this must be suppressed here
                            if measure not in [TODO, Explained, NotApplicable]
                        ]
                    )
                )
                for verifier in verifiers
            ]
        )
    else:
        doc.p("-- geen --")


STATE_NA = 'not_applicable'
STATE_EXPLAINED = 'explained'
STATE_TODO = 'todo'
STATE_PLANNED = 'planned'
STATE_COMPLETED = 'completed'


def group_verifiers_by_state(document):
    """
    collect verifiers of a document by their state (i.e. coverage by a measure)
    :param document: the document
    :return: mapping verifier state -> collection of verifiers
    """

    grouped_by_state = {
        STATE_NA: [],
        STATE_EXPLAINED: [],
        STATE_TODO: [],
        STATE_PLANNED: [],
        STATE_COMPLETED: [],
    }

    for chapter in document.fragments:
        for section in chapter.fragments:
            for norm in section.fragments:
                for verifier in norm.fragments:

                    # a verifier may appear in multiple measures
                    # so each measure must be mapped onto a state
                    for measure in verifier.bir_measures:

                        # special measures

                        if measure is NotApplicable:
                            state = STATE_NA

                        elif measure is Explained:
                            state = STATE_EXPLAINED

                        elif measure is TODO:
                            state = STATE_TODO

                        # regular measure - is it done already?

                        elif measure.done:
                            state = STATE_COMPLETED

                        else:
                            state = STATE_PLANNED

                        grouped_by_state[state].append(verifier)

    return grouped_by_state


def render_verifiers_by_state(document):
    """
    render groups of verifiers as an index of the document
    :param document: the document
    """

    labels_states = (
        ('Todo', STATE_TODO),
        ('Gepland', STATE_PLANNED),
        ('Gereed', STATE_COMPLETED),
        ('Explain', STATE_EXPLAINED),
        ('Niet van toepassing', STATE_NA),
   )

    grouped_by_state = group_verifiers_by_state(document)

    doc.h1('Verifier status')

    for label, state in labels_states:
        render_verifiers_with_state(label, grouped_by_state[state])


# --- PROCESSING STARTS HERE ---

# --- prepare the BIR document ---

link_measures_to_fragments(BIR)


# --- render the BIR document ---

with tag('html'):

    doc.head(BIR.title)

    with tag('body'):

        doc.p('gegenereerd op ', datetime.datetime.now().isoformat(), style="font-size:11px")

        with tag('div', klass='container'):

            render_document(BIR)

        with tag('div', klass='container'):

            render_verifiers_by_state(BIR)


# --- produce the BIR document ---

bir_content = indent(doc.getvalue())


if sys.version_info < (3, 0):
    with open('bir2012_document.html', 'w') as fout:
        fout.write(bir_content.encode('ascii', errors='xmlcharrefreplace'))
else:
    with open('bir2012_document.html', mode='w', encoding='ascii', errors='xmlcharrefreplace') as fout:
        print(bir_content, file=fout)

