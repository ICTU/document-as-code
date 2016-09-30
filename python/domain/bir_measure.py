"""
    BIR measure - defines and describes a measure for BIR compliance
"""

from __future__ import absolute_import
from __future__ import print_function


from .base import Base


class BirMeasure(Base):
    """ Measures that help to in BIR compliance. """

    def __init__(self, identifier, description, identifiers, done=False):

        super(BirMeasure, self).__init__( identifier )

        self.description = description
        self.identifiers = identifiers
        self.done = done

    # ---

    @classmethod
    def all_applicable_to_fragment(cls, fragment_identifier):
        return [bir_measure for bir_measure in cls.all for identifier in bir_measure.identifiers if fragment_identifier.startswith(identifier)]

