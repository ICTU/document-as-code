"""
    bootstrap - a HTML document with Bootstrap CSS and some helper methods
"""
from yattag import Doc


class BootstrapDoc(Doc):
    """ A HTML document with Bootstrap CSS and some helper methods. """

    def tagtext(self, with_doctype=True):
        """ Override to set the doctype. """
        doc, tag, text = super().tagtext()
        if with_doctype:
            doc.asis('<!DOCTYPE html>')
        return doc, tag, text

    def head(self, title):
        """ Add the head tag with a link to the Bootstrap CSS and a title. """
        with self.tag('head'):
            self.stag('link', rel="stylesheet", crossorigin="anonymous",
                      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css",
                      integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u")
            with self.tag('title'):
                self.text(title)

    # --- H1 ---

    def h1(self, h1_text, h1_subtext=None, h1_bookmark=None):
        """ Add a h1 with an optional sub text. """
        self.asis(self.h1_raw(h1_text, h1_subtext, h1_bookmark))

    def h1_raw(self, h1_text, h1_subtext=None, h1_bookmark=None):
        """ A h1 with an optional sub text. """
        return self.__header('h1', h1_text, h1_subtext, h1_bookmark)

    # --- H2 ---

    def h2(self, h2_text, h2_subtext=None, h2_bookmark=None):
        """ Add a h2 with an optional sub text. """
        self.asis(self.h2_raw(h2_text, h2_subtext, h2_bookmark))

    def h2_raw(self, h2_text, h2_subtext=None, h2_bookmark=None):
        """ A h2 with an optional sub text. """
        return self.__header('h2', h2_text, h2_subtext, h2_bookmark)

    # --- H3 ---

    def h3(self, h3_text, h3_subtext=None, h3_bookmark=None):
        """ Add a h3 with an optional sub text. """
        self.asis(self.h3_raw(h3_text, h3_subtext, h3_bookmark))

    def h3_raw(self, h3_text, h3_subtext=None, h3_bookmark=None):
        """ A h3 with an optional sub text. """
        return self.__header('h3', h3_text, h3_subtext, h3_bookmark)

    # --- H4 ---

    def h4(self, h4_text, h4_subtext=None, h4_bookmark=None):
        """ Add a h4 with an optional sub text. """
        self.asis(self.h4_raw(h4_text, h4_subtext, h4_bookmark))

    def h4_raw(self, h4_text, h4_subtext=None, h4_bookmark=None):
        """ A h4 with an optional sub text. """
        return self.__header('h4', h4_text, h4_subtext, h4_bookmark)

    # --- shared header utility ---

    def __header(self, header_tag, header_text, header_subtext=None, header_bookmark=None):
        """ Add a header with text and optional sub text. """
        # create canonical bookmark for header: UPPERCASE, spaces replaced by '-', multiple '-' compressed to one
        tmp = (header_bookmark if header_bookmark else header_text).replace(' ', '-').upper()
        bookmark = None
        while tmp != bookmark:
            bookmark = tmp
            tmp = tmp.replace('--', '-')

        doc, tag, text = self.__class__().tagtext(False)
        with tag('span', id=bookmark):
            with tag(header_tag):
                doc.asis(header_text)
                if header_subtext:
                    text(' ')
                    with tag('small'):
                        doc.asis(header_subtext)
        return doc.getvalue()

    # --- various document parts ---

    def table(self, headers, rows, caption=None, sort_rows=True, sort_cells=True, widths=None):
        """ Add a table with the headers and rows and an optional caption. The rows are sorted. If any cell contains
            a list it is joined with comma as separator. Widths can be given in an attempt to force column widths. """
        if widths is None:
            widths = [None] * len(headers)
        else:
            widths = (list(widths) + ([None] * len(headers)))[:len(headers)]

        with self.tag('table', klass='table table-striped'):
            if caption:
                with self.tag('caption'):
                    self.text(caption)
            with self.tag('thead'):
                with self.tag('tr'):
                    for header, width in zip(headers, widths):
                        if width:
                            with self.tag('th', ('width', width)):
                                self.text(header)
                        else:
                            with self.tag('th'):
                                self.text(header)
            with self.tag('tbody'):
                for row in sorted(rows) if sort_rows else rows:
                    with self.tag('tr'):
                        for cell in row:
                            with self.tag('td'):
                                if isinstance(cell, list):
                                    cell = ', '.join(sorted(cell) if sort_cells else cell)
                                self.asis(cell)

    def p(self, *p_text, **kwargs):
        """ Add a paragraph. """
        with self.tag('p', **kwargs):
            self.text(*p_text)

    def bookmark(self, bookmark_text):
        """ Return a bookmark that can be used to link to. """
        return self.__tag_with_text('span', bookmark_text, id=bookmark_text)

    def link(self, link_text, anchor=None, url=None):
        """ Return a link to a bookmark. """
        if anchor is None:
            anchor = link_text
        if url is None:
            url = "#{0}".format(anchor)
        return self.__tag_with_text('a', link_text, href=url)

    def badge(self, list_or_number):
        """ Return a badge. If the argument is a list, use the length of the list as number. """
        number = list_or_number if isinstance(list_or_number, int) else len(list_or_number)
        return self.__tag_with_text('span', "{0!s}".format(number), klass="badge")

    def label(self, label_text, modifier='default', **kwargs):
        """ Return a label with the specified text and an optional modifier (color). """
        assert modifier in ('default', 'primary', 'success', 'info', 'warning', 'danger')
        kwargs['klass'] = "label label-{0}".format(modifier)
        return self.__tag_with_text('span', label_text, **kwargs)

    # --- shared tag utility ---

    def __tag_with_text(self, tag_name, tag_text, **kwargs):
        """ Return a tag with the specified tag name and text. The optional kwargs are applied to the tag. """
        doc, tag, text = self.__class__().tagtext(False)
        with tag(tag_name, **kwargs):
            text(tag_text)
        return doc.getvalue()
