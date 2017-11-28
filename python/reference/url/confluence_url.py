"""
    Confluence URL - reference to a page within Confluence
"""
from __future__ import absolute_import
from __future__ import print_function

import sys

if sys.version_info < (3, 0):
    from urllib import quote_plus
else:
    from urllib.parse import quote_plus


class ConfluenceUrl(object):
    """
    From the Confluence documentation:
    
    * anchor
        pattern:
            http://myconfluence.com/display/spacekey/pagename#pagename-anchorname
        example:
            https://confluence.atlassian.com/display/DOC/Working+with+Links#WorkingwithLinks-InsertLinkAnchor

    * heading
        pattern:
            http://myconfluence.com/display/spacekey/pagename#pagename-headingtext
        example:
            https://confluence.atlassian.com/display/DOC/Working+with+Links#WorkingwithLinks-Insertalink
    """

    _base_url = None
    _page_title = None
    _anchor_name = None


    def __init__(self, base_url, page_title=None, anchor_name=None):
        """
        :param base_url: base of all URLs, including the spacekey
        :param page_title: title of the page as displayed
        :param anchor_name: name of the anchor, also works for headings
        """
        self._base_url = base_url
        self._page_title = page_title
        self._anchor_name = anchor_name


    def __str__(self):
        return "{cls.__name__}({b!r}, {p!r}, {a!r})".format(
            cls=self.__class__,
            b=self._base_url,
            p=self._page_title,
            a=self._anchor_name
        )

    __repr__ = __str__


    def page_title(self, page_title, anchor_name=None):
        """
        build on top of an existing base URL
        :param page_title: title of the page as displayed
        :param anchor_name: name of the anchor, also works for headings
        """
        return self.__class__(self._base_url, page_title, anchor_name if anchor_name else self._anchor_name)


    def anchor_name(self, anchor_name):
        """
        build on top of an existing base URL and page title
        :param anchor_name: name of the anchor, also works for headings
        """
        return self.__class__(self._base_url, self._page_title, anchor_name)


    @property
    def confluence_page_name(self):
        """
        page name conforming Confluence standard
        """
        return quote_plus(self._page_title)


    @property
    def confluence_anchor_name(self):
        """
        anchor name conforming Confluence standard
        """
        page_in_anchor = self._page_title.replace(' ', '')
        anchor_name_in_anchor = self._anchor_name.replace(' ', '')
        return '-'.join((page_in_anchor, anchor_name_in_anchor))


    @property
    def url(self):
        """
        compose the actual URL from its parts
        """
        url = self._base_url

        if self._page_title:
            url = '/'.join((url, self.confluence_page_name))

            if self._anchor_name:
                url = '#'.join((url, self.confluence_anchor_name))

        return url
