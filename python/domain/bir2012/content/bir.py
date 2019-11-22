"""
    fragments - define text fragments in the document
"""
from . import ch05
from . import ch06
from . import ch07
from . import ch08
from . import ch09
from . import ch10
from . import ch11
from . import ch12
from . import ch13
from . import ch14
from . import ch15

from domain import document


BIR = document.Document(
    identifier="BIR2012",
    title="Baseline Informatiebeveiliging Rijksdienst - 2012",
    fragments=[
        ch05.CH05,
        ch06.CH06,
        ch07.CH07,
        ch08.CH08,
        ch09.CH09,
        ch10.CH10,
        ch11.CH11,
        ch12.CH12,
        ch13.CH13,
        ch14.CH14,
        ch15.CH15,
    ]
)
