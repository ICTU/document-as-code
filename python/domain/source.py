"""
    source - defines and describes a source
"""

from __future__ import absolute_import
from __future__ import print_function


from .base import Base


class Source(Base):

    def __init__(self, identifier, title, version=None):

        super(Source, self).__init__( identifier )

        self.title = title
        self.version = version
