"""
    requirement - defines and describes a requirement
"""

from __future__ import absolute_import
from __future__ import print_function


from .base import Base


class Requirement(Base):

    def __init__(self, identifier, description, sources):

        super(Requirement, self).__init__( identifier )

        self.description = description
        self.sources = sources

    @classmethod
    def from_source(cls, source):
        return [requirement for requirement in cls.all if source in requirement.sources]
