"""
    person - describe a person
"""
from domain import base


class Person(base.Base):
    """
    person - information describing a person
    """

    def __init__(self, given_name, surname, email=None, **kwargs):
        """
        create a person's description
        """
        super().__init__()
        self.given_name = given_name
        self.surname = surname
        self.email = email
        for kw in kwargs:
            setattr(self, kw, kwargs[kw])

    @property
    def name(self):
        """
        name by which the person is known
        :return: the name
        """
        return f"{self.given_name} {self.surname}"
