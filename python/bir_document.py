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

from domain.bir2012.content.bir import BIR

from format.bootstrap import BootstrapDoc


doc, tag, text = BootstrapDoc().tagtext()


# --- document preparation ---

# fake measure to flag absence of true measure and to ease rendering
TODO = BirMeasure("TODO", "Things left todo", identifiers=[])


def assign_measures_to_fragments(fragment):

    fragment.bir_measures = set()

    # depth first with post visit processing
    for subfragment in fragment.fragments:
        fragment.bir_measures.update(assign_measures_to_fragments(subfragment))

    fragment.bir_measures.update(BirMeasure.all_applicable_to_fragment(fragment.identifier))
    if not fragment.bir_measures:
        fragment.bir_measures.add(TODO)
        # provide identification for missing stuff
        print('        "{}",'.format(fragment.identifier))

    return fragment.bir_measures


# --- label rendering ---

def measure_to_label_data(measure):

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

    # sort order of measures

    SPECIAL_MEASURE = {
        TODO:          1,
        Explained:     7,
        NotApplicable: 9,
    }
    REGULAR_MEASURE = 3

    return [
        measure_to_label_data(measure)
        for measure in sorted(measures, key=lambda m: (SPECIAL_MEASURE.get(m, REGULAR_MEASURE), m.identifier))
   ]


def turn_label_data_into_labels(labels_data):

    LABEL_STYLE = "font-size:11px"

    return [doc.label(text, kind, style=LABEL_STYLE) for text, kind in labels_data]


def turn_measures_into_labels(measures):

    labels_data = turn_measures_into_label_data(measures)

    return turn_label_data_into_labels(labels_data)


# --- generic fragment rendering ---

def render_fragment(fragment, h, render_sub_level=None):

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

def render_measures(measures):

    return turn_measures_into_labels(measures)


def render_norm(norm):

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
    render_fragment(section, doc.h2, render_norm)


def render_chapter(chapter):
    render_fragment(chapter, doc.h1, render_section)


def render_document(document):
    render_fragment(document, doc.h1, render_chapter)


def render_verifiers_with_state(label, verifiers):
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
                            for measure in verifier.bir_measures if measure not in [TODO, Explained, NotApplicable]
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

                    for measure in verifier.bir_measures:

                        if measure is NotApplicable:
                            state = STATE_NA

                        elif measure is Explained:
                            state = STATE_EXPLAINED

                        elif measure is TODO:
                            state = STATE_TODO

                        # regular measure - is it done already?

                        elif not measure.done:
                            state = STATE_PLANNED

                        else:
                            state = STATE_COMPLETED

                        grouped_by_state[state].append(verifier)

    return grouped_by_state


def render_verifiers_by_state(document):

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

assign_measures_to_fragments(BIR)


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
    with open('bir_document.html', 'w') as fout:
        fout.write(bir_content.encode('ascii', errors='xmlcharrefreplace'))
else:
    with open('bir_document.html', mode='w', encoding='ascii', errors='xmlcharrefreplace') as fout:
        print(bir_content, file=fout)

