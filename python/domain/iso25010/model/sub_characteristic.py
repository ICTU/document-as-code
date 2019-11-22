"""
    Iso25010SubCharacteristic - ISO 25010 software quality sub characteristic
"""
from . import characteristic_base as cb


class Iso25010SubCharacteristic(cb.Iso25010CharacteristicBase):
    """
    ISO 25010 software quality sub characteristic
    """

    _main_characteristic = None

    def __init__(self, identifier, name, description, part_of=None):
        """
        :param identifier: identifier for the characteristic
        :param name: name for the characteristic
        :param description: description for the characteristic
        """
        super().__init__(identifier, name, description)

        if part_of:
            self.part_of(part_of)

    def part_of(self, main_characteristic):
        """
        make sub characteristic part of a main characteristic
        :param main_characteristic: of which this subcharacteristic becomes a part
        """
        if self._main_characteristic is None:
            self._main_characteristic = main_characteristic
            main_characteristic.sub_characteristic(self)
