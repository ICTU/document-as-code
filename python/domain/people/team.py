"""
    team - describe a team
"""
from domain import base


class Team(base.Base):
    """
    team - named group of persons
    """

    def __init__(self, name, *persons):
        """
        create a team
        :param name: name of the team
        :param persons: members of the team
        """
        super().__init__()
        self.name = name
        self.persons = [p for p in persons]

    def add_person(self, person):
        """
        add a person as member of the team
        :param person: the new member
        """
        self.persons.append(person)

