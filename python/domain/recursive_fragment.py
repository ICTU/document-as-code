"""
    source - defines and describes a source
"""

from __future__ import absolute_import
from __future__ import print_function


from .base import Base


class RecursiveFragment(Base):


    number    = None
    text      = None
    fragments = None


    def __init__( self, identifier, title, text=None, fragments=[] ):

        super(RecursiveFragment, self).__init__( identifier )

        self.title = title
        self.text  = text
        self.fragments = []
        
        self.add( *fragments )


    def add( self, *fragments ):
        self.fragments.extend( fragments )
        return self


    def renumber( self, number, sep='.', start=1 ):
        self.number = str(number)
        for nr, fragment in enumerate( self.fragments, start ):
            fragment.renumber( sep.join( (self.number,str(nr)) ), sep, start )


    def get_title( self ):
        if self.number:
            title = "{} - {}".format( self.number, self.title )
        else:
            title = self.title
        return title