# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH05S01 = Section(
    identifier="05.01",
    title="Aansturing door de directie van de informatiebeveiliging",
    text="Doelstelling: Het verschaffen van directieaansturing van en -steun voor informatiebeveiliging in "
         "overeenstemming met bedrijfseisen en relevante wet- en regelgeving.",
    fragments=[

        Norm(
            identifier="05.01.01",
            title="Beleidsregels voor informatiebeveiliging",
            text="Ten behoeve van informatiebeveiliging behoort een reeks "
                 "beleidsregels te worden gedefinieerd, goedgekeurd door de directie, gepubliceerd en gecommuniceerd "
                 "aan medewerkers en relevante externe partijen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="05.01.01/01",
                    title="",
                    text="Er is een informatiebeveiligingsbeleid opgesteld door de organisatie. Dit beleid is "
                         "vastgesteld door de leiding van de organisatie en bevat tenminste de volgende punten: <br/>"
                         "<ol style='list-style-type: lower-alpha;'>"
                         "<li>de strategische uitgangspunten en randvoorwaarden die de organisatie hanteert voor "
                         "informatiebeveiliging en in het bijzonder de inbedding in, en afstemming op het algemene "
                         "beveiligingsbeleid en het informatievoorzieningsbeleid;</li>"
                         "<li>de organisatie van de informatiebeveiligingsfunctie, waaronder verantwoordelijkheden, "
                         "taken en bevoegdheden;</li>"
                         "<li>de toewijzing van de verantwoordelijkheden voor ketens van informatiesystemen aan "
                         "lijnmanagers;</li>"
                         "<li>de gemeenschappelijke betrouwbaarheidseisen en normen die op de organisatie van "
                         "toepassing zijn;</li>"
                         "<li>de frequentie waarmee het informatiebeveiligingsbeleid wordt ge&euml;valueerd;</li>"
                         "<li>de bevordering van het beveiligingsbewustzijn.</li>"
                        "</ol>",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="05.01.02",
            title="Beoordeling van het informatiebeveiligingsbeleid",
            text="Het beleid voor informatiebeveiliging behoort "
                 "met geplande tussenpozen of als zich significante veranderingen voordoen, te worden beoordeeld om "
                 "te waarborgen dat het voortdurend passend, adequaat en doeltreffend is.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="05.01.02/01",
                    title="",
                    text="Het informatiebeveiligingsbeleid wordt minimaal &eacute;&eacute;n keer per drie jaar, of bij "
                         "belangrijke wijzigingen als gevolg van reorganisatie of verandering in de "
                         "verantwoordelijkheidsverdeling, beoordeeld en zo nodig bijgesteld.",
                    bbn=1,
                ),
            ],
        ),

    ],
)


CH05 = Chapter(
    identifier="05",
    title="Informatiebeveiligingsbeleid",
    fragments=[
        CH05S01,
    ]
)
