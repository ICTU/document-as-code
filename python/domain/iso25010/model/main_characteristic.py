'''
    Iso25010MainCharacteristic - ISO 25010 software quality main characteristic
'''
from __future__ import absolute_import
from __future__ import print_function


from .characteristic_base import Iso25010CharacteristicBase


class Iso25010MainCharacteristic( Iso25010CharacteristicBase ):
    '''
    ISO 25010 software quality main characteristic
    '''

    _sub_characteristics = None


    def __init__( self, identifier, name, description, *subs ):
        '''
        Constructor
        '''
        super(Iso25010MainCharacteristic, self).__init__( identifier, name, description )

        self._sub_characteristics = []

        for s in subs:
            self.sub_characteristic( s )


    def sub_characteristic( self, sub_characteristic ):
        """
        """
        if sub_characteristic not in self._sub_characteristics:
            self._sub_characteristics.append( sub_characteristic )
            sub_characteristic.part_of( self )