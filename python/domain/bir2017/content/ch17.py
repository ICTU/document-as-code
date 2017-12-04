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
    title=u"Informatiebeveiligingscontinu�teit",
    text=u"Doelstelling: Informatiebeveiligingscontinu�teit behoort te worden ingebed in de systemen van het "
         u"bedrijfscontinu�teitsbeheer van de organisatie.",
    fragments=[

        Norm(
            identifier="17.01.01",
            title=u"Informatiebeveiligingscontinu�teit plannen",
            text=u"De organisatie behoort haar eisen voor informatiebeveiliging en voor de continu�teit van het "
                 u"informatiebeveiligingsbeheer in ongunstige situaties, bijv. een crisis of een ramp, vast te "
                 u"stellen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="17.01.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="17.01.02",
            title=u"Informatiebeveiligingscontinu�teit implementeren",
            text=u"De organisatie behoort processen, procedures en beheersmaatregelen vast te stellen, te "
                 u"documenteren, te implementeren en te handhaven om het vereiste niveau van continu�teit voor "
                 u"informatiebeveiliging tijdens een ongunstige situatie te waarborgen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="17.01.02/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="17.01.03",
            title=u"Informatiebeveiligingscontinu�teit verifi�ren, beoordelen en evalueren",
            text=u"De organisatie behoort de ten behoeve van informatiebeveiligingscontinu�teit vastgestelde en "
                 u"ge�mplementeerde beheersmaatregelen regelmatig te verifi�ren om te waarborgen dat ze deugdelijk en "
                 u"doeltreffend zijn tijdens ongunstige situaties.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="17.01.03/01",
                    title=u"",
                    text=u"Continu�teitsplannen worden jaarlijks getest op geldigheid en bruikbaarheid.",
                    bbn=2,
                ),
                Verifier(
                    identifier="17.01.03/02",
                    title=u"",
                    text=u"Door het uitvoeren van een expliciete risicoafweging worden de bedrijfskritische "
                         u"procesonderdelen met hun bijbehorende betrouwbaarheidseisen ge�dentificeerd.",
                    bbn=2,
                ),
                Verifier(
                    identifier="17.01.03/03",
                    title=u"",
                    text=u"De dienstverlening van de bedrijfskritische onderdelen wordt bij calamiteiten minimaal "
                         u"binnen een week hersteld.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S1702 = Section(
    identifier="17.02",
    title=u"Redundante componenten",
    text=u"Doelstelling: Beschikbaarheid van informatieverwerkende faciliteiten bewerkstelligen.",
    fragments=[

        Norm(
            identifier="17.02.01",
            title=u"Beschikbaarheid van informatieverwerkende faciliteiten",
            text=u"Informatieverwerkende faciliteiten behoren met voldoende redundantie te worden ge�mplementeerd om "
                 u"aan beschikbaarheidseisen te voldoen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="17.02.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


CH17 = Chapter(
    identifier="17",
    title=u"Informatiebeveiligingsaspecten van bedrijfscontinu�teitsbeheer",
    fragments=[
        S1701,
        S1702,
    ]
)

