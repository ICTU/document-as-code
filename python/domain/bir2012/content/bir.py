"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function

from domain.bir2012.content.ch05 import CH05
from domain.bir2012.content.ch06 import CH06
from domain.bir2012.content.ch07 import CH07
from domain.bir2012.content.ch08 import CH08
from domain.bir2012.content.ch09 import CH09
from domain.bir2012.content.ch10 import CH10
from domain.bir2012.content.ch11 import CH11
from domain.bir2012.content.ch12 import CH12
from domain.bir2012.content.ch13 import CH13
from domain.bir2012.content.ch14 import CH14
from domain.bir2012.content.ch15 import CH15
from domain.document import Document

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
