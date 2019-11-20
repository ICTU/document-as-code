# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.bio.model.norm import Norm
from domain.bio.model.verifier import Verifier
from domain.document.model.chapter import Chapter
from domain.document.model.section import Section


CH17S01 = Section(
    identifier="17.01",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="17.01.03",
            title=u"TITLE",
            text=u"""
Informatiebeveiligingscontinuïteit verifiëren, beoordelen en evalueren;
De organisatie behoort de ten behoeve van informatiebeveiligingscontinuïteit vastgestelde en geïmplementeerde beheersmaatregelen regelmatig te verifiëren om te waarborgen dat ze deugdelijk en doeltreffend zijn tijdens ongunstige situaties.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="17.01.03/01",
                    title=u"",
                    text=u"""
Continuïteitsplannen worden jaarlijks getest op geldigheid en bruikbaarheid.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="17.01.03/02",
                    title=u"",
                    text=u"""
Door het uitvoeren van een expliciete risicoafweging worden de bedrijfskritische procesonderdelen met hun bijbehorende betrouwbaarheidseisen geïdentificeerd.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="17.01.03/03",
                    title=u"",
                    text=u"""
De dienstverlening van de bedrijfskritische onderdelen wordt bij calamiteiten minimaal binnen een week hersteld.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH17 = Chapter(
    identifier="17",
    title=u"TITLE",
    fragments=[
        CH17S01
    ]
)
