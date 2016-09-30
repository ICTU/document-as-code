"""
    measure - defines and describes a measure
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.util import all_true


from domain.base import Base


class Measure(Base):
    """ Measures that help to fulfill requirements. """

    def __init__(self, identifier, description, requirements, deliverables=None, done=False):

        super(Measure, self).__init__( identifier )

        self.description = description
        self.requirements = requirements
        self.deliverables = deliverables or []
        self.done = done

    @classmethod
    def for_requirement(cls, requirement):
        return [measure for measure in cls.all if requirement in measure.requirements]

    @classmethod
    def all_completed_for_requirement(cls, requirement):
        return all_true(measure.done for measure in cls.for_requirement(requirement))

    @classmethod
    def for_deliverable(cls, deliverable):
        return [measure for measure in cls.all if deliverable in measure.deliverables]

    @classmethod
    def all_completed_for_deliverable(cls, deliverable):
        return all_true(measure.done for measure in cls.for_deliverable(deliverable))
