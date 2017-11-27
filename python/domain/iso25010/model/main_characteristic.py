"""
    Iso25010MainCharacteristic - ISO 25010 software quality main characteristic
"""
from __future__ import absolute_import
from __future__ import print_function


from . import characteristic_base as cb


class Iso25010MainCharacteristic(cb.Iso25010CharacteristicBase):
    """
    ISO 25010 software quality main characteristic
    """

    _sub_characteristics = None


    def __init__(self, identifier, name, description, *subs):
        """
        create an ISO 25010 main characteristic
        :param identifier: identifier for the characteristic
        :param name: name for the characteristic
        :param description: description for the characteristic
        :param subs: subcharacteristics
        """
        super(Iso25010MainCharacteristic, self).__init__(identifier, name, description)

        self._sub_characteristics = []

        for s in subs:
            self.sub_characteristic(s)


    def sub_characteristic(self, sub_characteristic):
        """
        add a subcharacteristic
        :param sub_characteristic: the one to add
        """
        if sub_characteristic not in self._sub_characteristics:
            self._sub_characteristics.append(sub_characteristic)
            sub_characteristic.part_of(self)
