"""
    source - defines and describes a source
"""

from __future__ import absolute_import
from __future__ import print_function


from ..base import Base


class RecursiveFragment(Base):

    title     = None
    lead      = None
    text      = None
    fragments = None


    def __init__( self, identifier, title, lead=None, text=None, fragments=[] ):

        super(RecursiveFragment, self).__init__( identifier )

        self.title = title
        self.lead  = lead
        self.text  = text
        self.fragments = []
        
        self.add( *fragments )


    def add( self, *fragments ):
        self.fragments.extend( fragments )
        return self


    def get_title( self ):
        return u"{} - {}".format( self.identifier, self.title )