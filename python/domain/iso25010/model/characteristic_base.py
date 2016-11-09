'''
    Iso25010CharacteristicBase - base class for ISO 25010 software quality characteristics
'''
from __future__ import absolute_import
from __future__ import print_function


from ...base import Base


class Iso25010CharacteristicBase( Base ):
    '''
    base class for ISO 25010 software quality characteristics
    '''

    name        = None  # name of the characteristic
    description = None  # description of the characteristic


    def __init__( self, identifier, name, description ):
        '''
        Constructor
        '''
        super(Iso25010CharacteristicBase, self).__init__( identifier )

        self.name        = name
        self.description = description

