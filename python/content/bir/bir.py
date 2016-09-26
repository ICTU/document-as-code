"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.document import Document, Chapter

from .ch05 import CH05
from .ch06 import CH06
from .ch07 import CH07
from .ch08 import CH08
from .ch09 import CH09
from .ch10 import CH10
from .ch11 import CH11
from .ch12 import CH12
from .ch13 import CH13
from .ch14 import CH14
from .ch15 import CH15


BIR = Document(
    identifier="BIR",
    title=u"Baseline Informatiebeveiliging Rijksdienst",
    fragments=[
        CH05,
        CH06,
        CH07,
        CH08,
        CH09,
        CH10,
        CH11,
        CH12,
        CH13,
        CH14,
        CH15,
    ]
)