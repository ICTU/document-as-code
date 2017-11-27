"""
    person - describe a person
"""
from __future__ import absolute_import
from __future__ import print_function


from domain import base


class Person(base.Base):
    """
    person - information describing a person
    """


    def __init__(self, given_name, surname, email=None):
        """
        create a person's description
        """
        self.given_name = given_name
        self.surname = surname
        self.email = email


    @property
    def name(self):
        """
        name by which the person is known
        :return: the name
        """
        return "{} {}".format(self.given_name, self.surname)
