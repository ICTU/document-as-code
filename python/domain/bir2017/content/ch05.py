# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S0501 = Section(
    identifier="05.01",
    title="Aansturing door de directie van de informatiebeveiliging",
    text="Doelstelling: Het verschafen van directieaansturing van en -steun voor informatiebeveiliging in "
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
                         "vastgesteld door de leiding van de organisatie en bevat tenminste de in het artikel 3 "
                         "van het VIR genoemde punten.",
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
                    text="Het informatiebeveiligingsbeleid wordt minimaal één keer per drie jaar, of bij "
                         "belangrijke wijzigingen als gevolg van reorganisatie of verandering in de "
                         "verantwoordelijkheidsverdeling, beoordeeld en zo nodig bijgesteld (VIR, artikel 3).",
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
        S0501,
    ]
)
