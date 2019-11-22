"""
    source - defines and describes a source
"""

from domain.base import Base


class Source(Base):

    def __init__(self, identifier, title, version=None):

        super().__init__(identifier)

        self.title = title
        self.version = version
