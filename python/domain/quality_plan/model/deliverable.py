"""
    deliverable - defines and describes a deliverable
"""
from domain.base import Base


class Deliverable(Base):

    def __init__(self, identifier, title, version=None):

        super().__init__(identifier)

        self.title = title
        self.version = version
