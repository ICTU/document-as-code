"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.document.recursive_fragment import RecursiveFragment

from . import text


F1 = RecursiveFragment(
    identifier="F1",
    title="Fragment",
    text="Say something smart about this recursive fragments example",
    fragments=[
        RecursiveFragment(
            identifier="",
            title="Subfragment",
            text="Something catchy",
            fragments=[
                RecursiveFragment(
                    identifier="",
                    title="Subsubfragment",
                ),
            ]
        ),
        RecursiveFragment(
            identifier="",
            title="Another Subfragment",
            text="or something foolish",
        ),
    ]
)


F2 = RecursiveFragment(
    identifier="F1",
    title="Another Fragment",
    fragments=[
        RecursiveFragment(
            identifier="",
            title="Yet Another Subfragment",
        ),
        RecursiveFragment(
            identifier="",
            title="How Many Subfragments?",
        ),
    ]
)

F0 = RecursiveFragment(
    identifier="F0",
    title=text.title,
    lead=text.intro,
    text=text.reading_guide,
    fragments=[F1,F2],
)
