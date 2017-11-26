"""
    bir measures - define the BIR measures taken
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.bir.model import bir_measure


# --- specific measures ---

M01 = bir_measure.BirMeasure(
    identifier="M01",
    description="",
    identifiers=[
    ],
)


# --- explained and accepted exceptions ---

Explained = bir_measure.BirMeasure(
    identifier="BM Explained",
    description="Geaccepteerde afwijking",
    identifiers=[
    ],
)


# --- declared and accepted as not applicable ---

NotApplicable = bir_measure.BirMeasure(
    identifier="Not Applicable",
    description="Niet van toepassing",
    identifiers=[
    ],
)
