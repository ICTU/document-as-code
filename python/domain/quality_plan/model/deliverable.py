"""
    deliverable - defines and describes a deliverable
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.base import Base


class Deliverable(Base):

    def __init__(self, identifier, title, version=None):

        super(Deliverable, self).__init__( identifier )

        self.title = title
        self.version = version
