# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S0501 = Section(
    identifier="05.01",
    title="Informatiebeveiligingsbeleid",
    fragments=[
        Norm(
            identifier="05.01.01",
            title="Beleidsdocumenten voor informatiebeveiliging",
            text="Een document met informatiebeveiligingsbeleid behoort door de directie "
                 "te worden goedgekeurd en gepubliceerd en kenbaar te worden gemaakt aan "
                 "alle werknemers en relevante externe partijen.",
            fragments=[
                Verifier(
                    identifier="05.01.01/01",
                    title="",
                    text="Er is beleid voor informatiebeveiliging door het lijnmanagement vastgesteld, "
                         "gepubliceerd en beoordeeld op basis van inzicht in risico's, kritische bedrijfsprocessen "
                         "en toewijzing van verantwoordelijkheden en prioriteiten.",
                ),
            ],
        ),
        Norm(
            identifier="05.01.02",
            title="Beoordeling van het informatiebeveiligingsbeleid",
            text="Het informatiebeveiligingsbeleid behoort met geplande tussenpozen, of "
                 "zodra zich belangrijke wijzigingen voordoen, te worden beoordeeld om te "
                 "bewerkstelligen dat het geschikt, toereikend en doeltreffend blijft.",
            fragments=[
                Verifier(
                    identifier="05.01.02/01",
                    title="",
                    text="Het informatiebeveiligingsbeleid wordt minimaal een keer per drie jaar, of "
                         "zodra zich belangrijke wijzigingen voordoen, beoordeeld en zonodig bijgesteld.",
                ),
            ],
        ),
    ],
)

CH05 = Chapter(
    identifier="05",
    title="Beveiligingsbeleid",
    fragments=[
        S0501,
    ]
)
