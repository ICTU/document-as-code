"""
    requirements - define requirements in the document
"""

from __future__ import absolute_import
from __future__ import print_function


from domain import Requirement
from .sources import S1, S2


R1 = Requirement(
    identifier="R1",
    description="This is requirement 1",
    sources=[S1],
)

R2 = Requirement(
    identifier="R2",
    description="This is requirement 2",
    sources=[S1, S2],
)

R3 = Requirement(
    identifier="R3",
    description="This is requirement 3. This requirement is completed because all of its measures have been completed.",
    sources=[S2],
)

R4 = Requirement(
    identifier="R4",
    description="This is requirement 4. It has no measures defined.",
    sources=[S2],
)
