"""
    util - various utilities
"""

from __future__ import absolute_import
from __future__ import print_function


def all_true(iterable):
    """ Helper that returns true if the iterable is not empty and all its elements evaluate to true. """
    items = list(iterable)
    return all(items) if items else False
