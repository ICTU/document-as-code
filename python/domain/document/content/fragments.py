"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.document.model import recursive_fragment as rf
from domain.quality_plan.content import text


F1 = rf.RecursiveFragment(
    identifier="F1",
    title="Fragment",
    text="Say something smart about this recursive fragments example",
    fragments=[
        rf.RecursiveFragment(
            identifier="",
            title="Subfragment",
            text="Something catchy",
            fragments=[
                rf.RecursiveFragment(
                    identifier="",
                    title="Subsubfragment",
                ),
            ]
        ),
        rf.RecursiveFragment(
            identifier="",
            title="Another Subfragment",
            text="or something foolish",
        ),
    ]
)


F2 = rf.RecursiveFragment(
    identifier="F1",
    title="Another Fragment",
    fragments=[
        rf.RecursiveFragment(
            identifier="",
            title="Yet Another Subfragment",
        ),
        rf.RecursiveFragment(
            identifier="",
            title="How Many Subfragments?",
        ),
    ]
)

F0 = rf.RecursiveFragment(
    identifier="F0",
    title=text.title,
    lead=text.intro,
    text=text.reading_guide,
    fragments=[F1, F2],
)
