"""
    example document - demonstrate how 'Document as Code' works
"""

import datetime
import pathlib
import re

from yattag import indent

from format.bootstrap import BootstrapDoc
from domain.compliance.model.measure import Measure

from .base_labeler import BaseLabeler


class DocumentRenderingContext(object):

    def __init__(self, filepath):
        self.filepath = filepath
        filepath.parent.mkdir(parents=True, exist_ok=True)

    def __enter__(self):
        self.doc_tag_text = BootstrapDoc().tagtext()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            return False

        doc, _tag, _text = self.doc_tag_text
        content = indent(doc.getvalue())
        with open(self.filepath, mode='w', errors='xmlcharrefreplace') as fout:
            print(content, file=fout)


class DocumentRenderer(object):

    STATE_NA = 'not_applicable'
    STATE_EXPLAINED = 'explained'
    STATE_TODO = 'todo'
    STATE_PLANNED = 'planned'
    STATE_COMPLETED = 'completed'

    labeler = None
    doc = None

    def __init__(self, labeler_class):
        super().__init__()
        self.todo = Measure("TODO", "Things left todo", identifiers=[])
        self.explain = Measure.explain()
        self.not_applicable = Measure.not_applicable()
        self.labeler_class = labeler_class

    def create_labeler(self, doc):
        if not issubclass(self.labeler_class, BaseLabeler):
            raise TypeError(f"labeler should be a BaseLabeler, not {self.labeler_class.__name__}")
        return self.labeler_class(doc, self.todo, self.explain, self.not_applicable)

    # --- document rendering ---

    def render_main_document_as_one(self, document, filepath, measures_annex=True):
        """
        render a document as a single file
        a document is a fragment that contains chapters
        :param document: the document
        :param filepath: where to save the rendered document
        :param measures_annex: whether to include the measures annex
        """
        with DocumentRenderingContext(filepath) as ctx:
            doc, tag, text = ctx.doc_tag_text

            self.labeler = self.create_labeler(doc)
            self.doc = doc

            with tag('html'):
                doc.head(document.title)

                with tag('body'):
                    doc.p('gegenereerd op ', datetime.datetime.now().isoformat(), style="font-size:11px")

                    with tag('div', klass='container'):
                        self._render_fragment(document, self.doc.h1, self._render_chapter)

                    with tag('div', klass='container'):
                        self.render_verifier_annex(document)

                    if measures_annex:
                        with tag('div', klass='container'):
                            self.render_measures_annex()

            self.doc = None
            self.labeler = None

    def render_main_document_as_parts(self, document, dirpath, measures_annex=True):
        """
        render a document as a group of files - one for each chapter and annex
        a document is a fragment that contains chapters
        :param document: the document
        :param dirpath: where to save the rendered document parts
        :param measures_annex: whether to include the measures annex
        """
        dirpath = pathlib.Path(dirpath).resolve()
        if not dirpath.exists():
            dirpath.mkdir(parents=True)

        index = []

        # chapters

        for chapter in document.fragments:

            filename = self._title_to_filename(chapter.title, prefix=chapter.identifier)
            filepath = dirpath / filename

            self._write_document_file(filepath, chapter.title, self._render_chapter, chapter)

            index.append((f"{chapter.identifier} {chapter.title}", filename))

        # annex A

        title = "Verifier status"
        filename = self._title_to_filename(title, prefix="A")
        filepath = dirpath / filename

        self._write_document_file(filepath, title, self.render_verifier_annex, document)

        index.append((f"A {title}", filename))

        # annex B - optional

        if measures_annex:
            title = "Maatregelen"
            filename = self._title_to_filename(title, prefix="B")
            filepath = dirpath / filename

            self._write_document_file(filepath, title, self.render_measures_annex)

            index.append((f"B {title}", filename))

        # table of content

        filename = self._title_to_filename("index")
        filepath = dirpath / filename

        self._write_document_file(filepath, "inhoud", self._toc_maker, index)

    @staticmethod
    def _title_to_filename(title, prefix=None):
        """
        determine a file name for a document with a title
        :param title: the document title
        :param prefix: title prefix - e.g. chapter number (optional)
        :return: string
        """
        title_part = "-".join(re.sub("[^0-9a-z]", " ", title.lower()).split())
        if prefix:
            prefix_part = "-".join(re.sub("[^0-9a-zA-Z]", " ", prefix).split())
            return f"{prefix_part}-{title_part}.html"
        return f"{title_part}.html"

    def _write_document_file(self, filepath, title, content_maker, *args, **kwargs):
        """
        write content to a document file
        :param filepath: path to the file to write to
        :param title: title of the document
        :param content_maker: creates the actual content
        :param *args: arguments to pass to content_maker
        :param *kwargs: keyword arguments to pass to content_maker
        """
        with DocumentRenderingContext(filepath) as ctx:
            doc, tag, text = ctx.doc_tag_text

            self.labeler = self.create_labeler(doc)
            self.doc = doc

            with tag('html'):
                doc.head(title)

                with tag('body'):
                    doc.p('gegenereerd op ', datetime.datetime.now().isoformat(), style="font-size:11px")

                    with tag('div', klass='container'):
                        content_maker(*args, **kwargs)

            self.doc = None
            self.labeler = None

    def _toc_maker(self, index):
        """
        create a table of contents
        :param index: collect of (title, filename) pairs
        """
        self.doc.h1("Inhoud")
        for title, filename in index:
            with self.doc.tag('p'):
                self.doc.asis(self.doc.link(f"{title}", url=f"{filename}"))

    # --- parts of the main document ---

    def _render_chapter(self, chapter):
        """
        render a chapter
        a chapter is a fragment that contains sections
        :param chapter: the chapter
        """
        self._render_fragment(chapter, self.doc.h1, self._render_section)

    def _render_section(self, section):
        """
        render a section
        a section is a fragment that contains norms
        :param section: the section
        """
        self._render_fragment(section, self.doc.h2, self._render_norm)

    def _render_norm(self, norm):
        """
        render a norm
        a norm contains an introductory text followed by some verifiers
        :param norm: the norm
        """
        self._render_fragment(norm, self.doc.h3)
        if norm.fragments:
            self.doc.table(
                ('Ref', 'Verifier', 'BBN', 'Status'),
                [
                    (
                        self.doc.bookmark(verifier.identifier),
                        verifier.text,
                        ''.join(self.labeler.bbn_to_labels(verifier.bbn)),
                        ''.join(self.labeler.measures_to_labels(verifier.measures)),
                    )
                    for verifier in norm.fragments
                ],
                widths=("80px", "*", "84px", "40px"),
            )

    def _render_fragment(self, fragment, heading_renderer, sublevel_render=None):
        """
        render a document fragment
        :param fragment: the fragment
        :param heading_renderer: heading renderer
        :param sublevel_render: renderer for next fragment level (optional)
        """
        labels = self.labeler.fragment_to_labels(fragment)

        heading_renderer(fragment.get_title(), ''.join(labels))

        if fragment.lead:
            self.doc.p(fragment.lead, klass='lead')
        if fragment.text:
            self.doc.asis(fragment.text)
        if sublevel_render:
            for subfragment in fragment.fragments:
                sublevel_render(subfragment)

    # --- verifier annex ---

    def render_verifier_annex(self, document):
        """
        render verifier coverage in an annex
        :param document:
        """
        labels_states = (
            ('Todo', self.STATE_TODO),
            ('Gepland', self.STATE_PLANNED),
            ('Gereed', self.STATE_COMPLETED),
            ('Explain', self.STATE_EXPLAINED),
            ('Niet van toepassing', self.STATE_NA),
        )

        grouped_by_state = self.group_verifiers_by_state(document)

        self.doc.h1('Verifier status')

        for label, state in labels_states:
            self._render_verifier_group(label, grouped_by_state[state])

    def _render_verifier_group(self, label, verifiers):
        """
        render a group of verifiers
        :param label: label of the group
        :param verifiers: the group of verifiers
        """
        self.doc.h2(label, self.doc.badge(len(verifiers)))

        if verifiers:
            self.doc.table(
                ('Ref', 'Verifier', 'BBN', ''),
                [
                    (
                        self.doc.bookmark(verifier.identifier),
                        verifier.text,
                        ''.join(self.labeler.bbn_to_labels(verifier.bbn)),
                        self.labeler.measures_to_labels(
                            [
                                measure
                                for measure in verifier.measures
                                # a verifier may appear in multiple measures
                                # it may therefore also be mapped onto on of the special measures
                                # this must be suppressed here
                                if measure not in (self.todo, self.explain, self.not_applicable, )
                            ]
                        )
                    )
                    for verifier in verifiers
                ],
                widths=("80px", "*", "84px", "40px"),
            )
        else:
            self.doc.p("-- geen --")

    def _render_verifier(self, verifier):
        pass

    # --- measures annex ---

    def render_measures_annex(self, measures=None):
        """
        render measures, their description and state
        """
        specials = (self.todo, self.not_applicable, self.explain)
        measures_to_report = set(measures if measures else Measure.all) - set(specials)

        self.doc.h2("Maatregelen", self.doc.badge(len(measures_to_report)))

        for measure in sorted(measures_to_report, key=lambda m: m.identifier):
            self._render_measure(measure)

    def _render_measure(self, measure):
        """
        render a single measure
        :param measure: the measure
        """
        label = self.labeler.measure_to_label(measure)
        self.doc.h3(measure.identifier, label)
        self.doc.p(measure.description)

    # --- document preparation ---

    def link_measures_to_fragments(self, fragment):
        """
        link defined measures to a fragment and its subfragments
        each measure relates to fragments through the identifiers used for those fragments
        here that symbolic reference is turned into actual object references
        :param fragment: fragment to start with
        :return: measures assigned to this fragment
        """

        # augment fragment with measures defined for it
        fragment.measures = set()

        # depth first collection of measures defined for subfragments
        for subfragment in fragment.fragments:
            fragment.measures.update(self.link_measures_to_fragments(subfragment))

        # post visit processing to add all measures defined for this fragment
        fragment.measures.update(Measure.all_applicable_to_fragment(fragment.identifier))

        # no measures implicates we still have work to do
        if not fragment.measures:
            fragment.measures.add(self.todo)

        return fragment.measures

    # ---

    def group_verifiers_by_state(self, document):
        """
        collect verifiers of a document by their state (i.e. coverage by a measure)
        :param document: the document
        :return: mapping verifier state -> collection of verifiers
        """
        grouped_by_state = {
            self.STATE_NA: [],
            self.STATE_EXPLAINED: [],
            self.STATE_TODO: [],
            self.STATE_PLANNED: [],
            self.STATE_COMPLETED: [],
        }

        for chapter in document.fragments:
            for section in chapter.fragments:
                for norm in section.fragments:
                    for verifier in norm.fragments:

                        # a verifier may appear in multiple measures
                        # so each measure must be mapped onto a state
                        for measure in verifier.measures:

                            # special measures

                            if measure is self.not_applicable:
                                state = self.STATE_NA

                            elif measure is self.explain:
                                state = self.STATE_EXPLAINED

                            elif measure is self.todo:
                                state = self.STATE_TODO

                            # regular measure - is it done already?

                            elif measure.done:
                                state = self.STATE_COMPLETED

                            else:
                                state = self.STATE_PLANNED

                            grouped_by_state[state].append(verifier)

        return grouped_by_state
