"""
    requirement - defines and describes a requirement
"""

from domain.base import Base


class Requirement(Base):

    def __init__(self, identifier, description, sources):

        super().__init__(identifier)

        self.description = description
        self.sources = sources

    @classmethod
    def from_source(cls, source):
        return [requirement for requirement in cls.all if source in requirement.sources]
