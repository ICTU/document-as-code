# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function

from domain.document.model.chapter import Chapter
from domain.document.model.section import Section
from domain.norm_specification.model.norm import Norm
from domain.norm_specification.model.verifier import Verifier


S0501 = Section(
    identifier="05.01",
    title=u"Aansturing door de directie van de informatiebeveiliging",
    text=u"Doelstelling: Het verschafen van directieaansturing van en -steun voor informatiebeveiliging in "
         u"overeenstemming met bedrijfseisen en relevante wet- en regelgeving.",
    fragments=[

        Norm(
            identifier="05.01.01",
            title=u"Beleidsregels voor informatiebeveiliging",
            text=u"Ten behoeve van informatiebeveiliging behoort een reeks "
                 u"beleidsregels te worden gedefinieerd, goedgekeurd door de directie, gepubliceerd en gecommuniceerd "
                 u"aan medewerkers en relevante externe partijen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="05.01.01/01",
                    title=u"",
                    text=u"Er is een informatiebeveiligingsbeleid opgesteld door de organisatie. Dit beleid is "
                         u"vastgesteld door de leiding van de organisatie en bevat tenminste de in het artikel 3 "
                         u"van het VIR genoemde punten.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="05.01.02",
            title=u"Beoordeling van het informatiebeveiligingsbeleid",
            text=u"Het beleid voor informatiebeveiliging behoort "
                 u"met geplande tussenpozen of als zich significante veranderingen voordoen, te worden beoordeeld om "
                 u"te waarborgen dat het voortdurend passend, adequaat en doeltreffend is.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="05.01.02/01",
                    title=u"",
                    text=u"Het informatiebeveiligingsbeleid wordt minimaal één keer per drie jaar, of bij "
                         u"belangrijke wijzigingen als gevolg van reorganisatie of verandering in de "
                         u"verantwoordelijkheidsverdeling, beoordeeld en zo nodig bijgesteld (VIR, artikel 3).",
                    bbn=1,
                ),
            ],
        ),

    ],
)

CH05 = Chapter(
    identifier="05",
    title=u"Informatiebeveiligingsbeleid",
    fragments=[
        S0501,
    ]
)
