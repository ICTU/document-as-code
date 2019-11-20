"""
    BIO measure - defines and describes a measure for BIO compliance
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.base import Base


class BioMeasure(Base):
    """ Measures that help to in BIO compliance. """

    _explain = None
    _not_applicable = None

    def __init__(self, identifier, description, identifiers, url=None, done=False):

        super(BioMeasure, self).__init__(identifier)

        self.description = description
        self.identifiers = identifiers
        self.url = url
        self.done = done

    def set_explain(self):
        self.register_explain(self)
        return self

    def set_not_applicable(self):
        self.register_not_applicable(self)
        return self

    # ---

    @classmethod
    def all_applicable_to_fragment(cls, fragment_identifier):
        return [
            bir_measure
            for bir_measure in cls.all
            for identifier in bir_measure.identifiers
            if fragment_identifier.startswith(identifier)
        ]

    # --- class property explain (rw) ---

    @classmethod
    def register_explain(cls, explain):
        if not isinstance(explain, cls):
            raise TypeError(f"explain should be {cls.__name__}, not {explain.__class__.__name__}")
        cls._explain = explain

    @classmethod
    def explain(cls):
        return cls._explain

    # --- class property not_applicable (rw) ---

    @classmethod
    def register_not_applicable(cls, not_applicable):
        if not isinstance(not_applicable, cls):
            raise TypeError(f"not_applicable should be {cls.__name__}, not {not_applicable.__class__.__name__}")
        cls._not_applicable = not_applicable

    @classmethod
    def not_applicable(cls):
        return cls._not_applicable
