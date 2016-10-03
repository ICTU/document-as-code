"""
    Confluence URL - reference to a page within Confluence
"""
from __future__ import absolute_import
from __future__ import print_function


from urllib import quote_plus


class ConfluenceUrl( object ):
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


    def __init__( self, base_url, page_title, anchor_name=None ):
        """
        @param base_url: base of all URLs, including the spacekey
        @param page_title: title of the page as displayed
        @param anchor_name: name of the anchor, also works for headings
        """
        self.base_url    = base_url
        self.page_title  = page_title
        self.anchor_name = anchor_name


    @property
    def url( self ):
        """
        compose the actual URL from its parts
        """
        page_in_url = quote_plus( self.page_title )
        url = '/'.join( ( self.base_url, page_in_url ) )

        if self.anchor_name:
            page_in_anchor = self.page_title.replace( ' ', '' )
            anchor_name_in_anchor = self.anchor_name.replace( ' ', '' )
            anchor = '-'.join( ( page_in_anchor, anchor_name_in_anchor ) )
            url = '#'.join( ( url, anchor ) )

        return url


