"""
    base - base class for domain classes
"""

from __future__ import absolute_import
from __future__ import print_function


class Base(object):
    """
    base class for domain classes
    """

    all = None

    identifier = None

    def __init__(self, identifier):
        """
        create domain object and self-register it
        """
        if self.__class__.all is None:
            self.__class__.all = set()

        self.__class__.all.add(self)

        self.identifier = identifier

    @classmethod
    def find_instance(cls, identifier):
        """
        find instance with given identifier
        :param identifier: instance to look for
        :return: instance or None
        """
        for instance in cls.all:
            if instance.identifier == identifier:
                return instance
        return None
