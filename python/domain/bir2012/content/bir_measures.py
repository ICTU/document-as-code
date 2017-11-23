"""
    bir measures - define the BIR measures taken
"""

from __future__ import absolute_import
from __future__ import print_function

from domain.bir20122012.model.bir_measure import BirMeasure

# --- specific measures ---

M01 = BirMeasure(
    identifier="M01",
    description="",
    identifiers=[
    ],
)


# --- explained and accepted exceptions ---

Explained = BirMeasure(
    identifier="BM Explained",
    description="Geaccepteerde afwijking",
    identifiers=[
    ],
)


# --- declared and accepted as not applicable ---

NotApplicable = BirMeasure(
    identifier="Not Applicable",
    description="Niet van toepassing",
    identifiers=[
    ],
)
