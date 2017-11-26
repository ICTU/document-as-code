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

S0501 = Section(
    identifier="05.01",
    title=u"Informatiebeveiligingsbeleid",
    fragments=[
        Norm(
            identifier="05.01.01",
            title=u"Beleidsdocumenten voor informatiebeveiliging",
            text=u"Een document met informatiebeveiligingsbeleid behoort door de directie "
                 u"te worden goedgekeurd en gepubliceerd en kenbaar te worden gemaakt aan "
                 u"alle werknemers en relevante externe partijen.",
            fragments=[
                Verifier(
                    identifier="05.01.01/01",
                    title="",
                    text=u"Er is beleid voor informatiebeveiliging door het lijnmanagement vastgesteld, "
                         u"gepubliceerd en beoordeeld op basis van inzicht in risico's, kritische bedrijfsprocessen "
                         u"en toewijzing van verantwoordelijkheden en prioriteiten.",
                ),
            ],
        ),
        Norm(
            identifier="05.01.02",
            title=u"Beoordeling van het informatiebeveiligingsbeleid",
            text=u"Het informatiebeveiligingsbeleid behoort met geplande tussenpozen, of "
                 u"zodra zich belangrijke wijzigingen voordoen, te worden beoordeeld om te "
                 u"bewerkstelligen dat het geschikt, toereikend en doeltreffend blijft.",
            fragments=[
                Verifier(
                    identifier="05.01.02/01",
                    title="",
                    text=u"Het informatiebeveiligingsbeleid wordt minimaal een keer per drie jaar, of "
                         u"zodra zich belangrijke wijzigingen voordoen, beoordeeld en zonodig bijgesteld.",
                ),
            ],
        ),
    ],
)

CH05 = Chapter(
    identifier="05",
    title=u"Beveiligingsbeleid",
    fragments=[
        S0501,
    ]
)
