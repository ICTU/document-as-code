"""
    verifier - defines and describes a verifier with a norm
"""
from domain.document.model import recursive_fragment


class Verifier(recursive_fragment.RecursiveFragment):

    bbn = None

    def __init__(self, identifier, title, bbn=None, lead=None, text=None, fragments=[]):
        """
        create a verifier
        """
        super().__init__(identifier, title, lead=lead, text=text, fragments=fragments)

        self.bbn = bbn
