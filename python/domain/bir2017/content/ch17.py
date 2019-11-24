# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S1701 = Section(
    identifier="17.01",
    title="Informatiebeveiligingscontinu&iuml;teit",
    text="Doelstelling: Informatiebeveiligingscontinu&iuml;teit behoort te worden ingebed in de systemen van het "
         "bedrijfscontinu&iuml;teitsbeheer van de organisatie.",
    fragments=[

        Norm(
            identifier="17.01.01",
            title="Informatiebeveiligingscontinu&iuml;teit plannen",
            text="De organisatie behoort haar eisen voor informatiebeveiliging en voor de continu&iuml;teit van het "
                 "informatiebeveiligingsbeheer in ongunstige situaties, bijv. een crisis of een ramp, vast te "
                 "stellen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="17.01.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="17.01.02",
            title="Informatiebeveiligingscontinu&iuml;teit implementeren",
            text="De organisatie behoort processen, procedures en beheersmaatregelen vast te stellen, te "
                 "documenteren, te implementeren en te handhaven om het vereiste niveau van continu&iuml;teit voor "
                 "informatiebeveiliging tijdens een ongunstige situatie te waarborgen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="17.01.02/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="17.01.03",
            title="Informatiebeveiligingscontinu&iuml;teit verifi&euml;ren, beoordelen en evalueren",
            text="De organisatie behoort de ten behoeve van informatiebeveiligingscontinu&iuml;teit vastgestelde en "
                 "ge&iuml;mplementeerde beheersmaatregelen regelmatig te verifi&euml;ren om te waarborgen dat ze "
                 "deugdelijk en doeltreffend zijn tijdens ongunstige situaties.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="17.01.03/01",
                    title="",
                    text="Continu&iuml;teitsplannen worden jaarlijks getest op geldigheid en bruikbaarheid.",
                    bbn=2,
                ),
                Verifier(
                    identifier="17.01.03/02",
                    title="",
                    text="Door het uitvoeren van een expliciete risicoafweging worden de bedrijfskritische "
                         "procesonderdelen met hun bijbehorende betrouwbaarheidseisen ge&iuml;dentificeerd.",
                    bbn=2,
                ),
                Verifier(
                    identifier="17.01.03/03",
                    title="",
                    text="De dienstverlening van de bedrijfskritische onderdelen wordt bij calamiteiten minimaal "
                         "binnen een week hersteld.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S1702 = Section(
    identifier="17.02",
    title="Redundante componenten",
    text="Doelstelling: Beschikbaarheid van informatieverwerkende faciliteiten bewerkstelligen.",
    fragments=[

        Norm(
            identifier="17.02.01",
            title="Beschikbaarheid van informatieverwerkende faciliteiten",
            text="Informatieverwerkende faciliteiten behoren met voldoende redundantie te worden ge&iuml;mplementeerd "
                 "om aan beschikbaarheidseisen te voldoen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="17.02.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


CH17 = Chapter(
    identifier="17",
    title="Informatiebeveiligingsaspecten van bedrijfscontinu&iuml;teitsbeheer",
    fragments=[
        S1701,
        S1702,
    ]
)
