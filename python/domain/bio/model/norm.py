"""
    norm - defines and describes a norm
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.document.model import recursive_fragment


class Norm(recursive_fragment.RecursiveFragment):

    bbn = None

    def __init__(self, identifier, title, bbn=None, lead=None, text=None, fragments=[]):
        """
        create a norm
        BIR 2017 introduced a security level (basisbeschermingsniveau, BBN)
        """
        super(Norm, self).__init__(identifier, title, lead=lead, text=text, fragments=fragments)

        self.bbn = bbn
