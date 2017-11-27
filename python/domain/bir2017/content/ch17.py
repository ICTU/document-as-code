# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function

from domain.bir.model.norm import Norm
from domain.bir.model.verifier import Verifier
from domain.document.model.chapter import Chapter
from domain.document.model.section import Section

S1701 = Section(
    identifier="17.01",
    title=u"",
    fragments=[

        Norm(
            identifier="17.01.01",
            title=u"",
            text=u"Informatiebeveiligingscontinuïteit plannen: De organisatie behoort haar eisen voor "
                 u"informatiebeveiliging en voor de continuïteit van het informatiebeveiligingsbeheer in ongunstige "
                 u"situaties, bijv. een crisis of een ramp, vast te stellen.",
            fragments=[
            ],
        ),

        Norm(
            identifier="17.01.02",
            title=u"",
            text=u"Informatiebeveiligingscontinuïteit implementeren: De organisatie behoort processen, procedures "
                 u"en beheersmaatregelen vast te stellen, te documenteren, te implementeren en te handhaven om het "
                 u"vereiste niveau van continuïteit voor informatiebeveiliging tijdens een ongunstige situatie te "
                 u"waarborgen.",
            fragments=[
            ],
        ),

        Norm(
            identifier="17.01.03",
            title=u"",
            text=u"Informatiebeveiligingscontinuïteit verifiëren, beoordelen en evalueren: De organisatie behoort "
                 u"de ten behoeve van informatiebeveiligingscontinuïteit vastgestelde en geïmplementeerde "
                 u"beheersmaatregelen regelmatig te verifiëren om te waarborgen dat ze deugdelijk en doeltreffend "
                 u"zijn tijdens ongunstige situaties.",
            fragments=[
                Verifier(
                    identifier="17.01.03/01",
                    title=u"",
                    text=u"Continuïteitsplannen worden jaarlijks getest op geldigheid en bruikbaarheid.",
                ),
                Verifier(
                    identifier="17.01.03/02",
                    title=u"",
                    text=u"Door het uitvoeren van een expliciete risicoafweging worden de bedrijfskritische "
                         u"procesonderdelen met hun bijbehorende betrouwbaarheidseisen geïdentificeerd.",
                ),
                Verifier(
                    identifier="17.01.03/03",
                    title=u"",
                    text=u"De dienstverlening van de bedrijfskritische onderdelen wordt bij calamiteiten minimaal "
                         u"binnen een week hersteld.",
                ),
            ],
        ),

    ],
)


S1702 = Section(
    identifier="17.02",
    title=u"",
    fragments=[

        Norm(
            identifier="17.02.01",
            title=u"",
            text=u"Beschikbaarheid van informatieverwerkende faciliteiten: Informatieverwerkende faciliteiten behoren "
                 u"met voldoende redundantie te worden geïmplementeerd om aan beschikbaarheidseisen te voldoen.",
            fragments=[
            ],
        ),

    ],
)


CH17 = Chapter(
    identifier="17",
    title=u"",
    fragments=[
        S1701,
        S1702,
    ]
)

