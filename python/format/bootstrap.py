from yattag import Doc


class BootstrapDoc(Doc):
    """ A HTML document with Bootstrap CSS and some helper methods. """

    def tagtext(self):
        """ Override to set the doctype. """
        doc, tag, text = super(BootstrapDoc, self).tagtext()
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

    def h1(self, h1_text, h1_subtext=None):
        """ Add a h1 with an optional sub text. """
        self.__header('h1', h1_text, h1_subtext)

    def h2(self, h2_text, h2_subtext=None):
        """ Add a h2 with an optional sub text. """
        self.__header('h2', h2_text, h2_subtext)

    def __header(self, header_tag, header_text, header_subtext=None):
        """ Add a header with text and optional sub text. """
        with self.tag(header_tag):
            self.asis(header_text)
            if header_subtext:
                self.text(' ')
                with self.tag('small'):
                    self.asis(header_subtext)

    def table(self, headers, rows, caption=None):
        """ Add a table with the headers and rows and an optional caption. The rows are sorted. If any cell contains
            a list it is joined with comma as separator. """
        with self.tag('table', klass='table table-striped'):
            if caption:
                with self.tag('caption'):
                    self.text(caption)
            with self.tag('thead'):
                with self.tag('tr'):
                    for header in headers:
                        with self.tag('th'):
                            self.text(header)
            with self.tag('tbody'):
                for row in sorted(rows):
                    with self.tag('tr'):
                        for cell in row:
                            with self.tag('td'):
                                if isinstance(cell, list):
                                    cell = ', '.join(sorted(cell))
                                self.asis(cell)

    def p(self, *p_text, **kwargs):
        """ Add a paragraph. """
        with self.tag('p', **kwargs):
            self.text(*p_text)

    def bookmark(self, bookmark_text):
        """ Return a bookmark that can be used to link to. """
        return self.__tag_with_text('span', bookmark_text, id=bookmark_text)

    def link(self, link_text):
        """ Return a link to a bookmark. """
        return self.__tag_with_text('a', link_text, href="#{0}".format(link_text))

    def badge(self, list_or_number):
        """ Return a badge. If the argument is a list, use the length of the list as number. """
        number = list_or_number if isinstance(list_or_number, int) else len(list_or_number)
        return self.__tag_with_text('span', "{0!s}".format(number), klass="badge")

    def label(self, label_text, modifier='default'):
        """ Return a label with the specified text and an optional modifier (color). """
        assert modifier in ('default', 'primary', 'success', 'info', 'warning', 'danger')
        return self.__tag_with_text('span', label_text, klass="label label-{0}".format(modifier))

    def __tag_with_text(self, tag_name, tag_text, **kwargs):
        """ Return a tag with the specified tag name and text. The optional kwargs are applied to the tag. """
        doc, tag, text = self.__class__().tagtext()
        with tag(tag_name, **kwargs):
            text(tag_text)
        return doc.getvalue()
