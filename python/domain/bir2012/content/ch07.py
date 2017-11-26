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

S0701 = Section(
    identifier="07.01",
    title=u"Verantwoordelijkheid voor bedrijfsmiddelen",
    fragments=[
        Norm(
            identifier="07.01.01",
            title=u"Inventarisatie van bedrijfsmiddelen",
            text=u"Alle bedrijfsmiddelen behoren duidelijk te zijn geïdentificeerd en er behoort een inventaris van "
                 u"alle belangrijke bedrijfsmiddelen te worden opgesteld en bijgehouden.",
            fragments=[
                Verifier(
                    identifier="07.01.01/01",
                    title=u"",
                    text=u"Er is een actuele registratie van bedrijfsmiddelen die voor de organisatie een belang "
                         u"vertegenwoordigen zoals informatie(verzamelingen), software, hardware, diensten, mensen en "
                         u"hun kennis/vaardigheden. Van elk middel is de waarde voor de organisatie, het vereiste "
                         u"beschermingsniveau en de verantwoordelijke lijnmanager bekend.",
                ),
            ],
        ),
        Norm(
            identifier="07.01.02",
            title=u"Eigendom van bedrijfsmiddelen",
            text=u"Alle informatie en bedrijfsmiddelen die verband houden met ICT-voorzieningen behoren een eigenaar "
                 u"te hebben in de vorm van een aangewezen deel van de organisatie.",
            fragments=[
                Verifier(
                    identifier="07.01.02/01",
                    title=u"",
                    text=u"Voor elk bedrijfsproces, applicatie, gegevensverzameling en ICT-faciliteit is een "
                         u"verantwoordelijke lijnmanager benoemd.",
                ),
            ],
        ),
        Norm(
            identifier="07.01.03",
            title=u"Aanvaardbaar gebruik van bedrijfsmiddelen",
            text=u"Er behoren regels te worden vastgesteld, gedocumenteerd en geïmplementeerd voor aanvaardbaar "
                 u"gebruik van informatie en bedrijfsmiddelen die verband houden met ICT-voorzieningen.",
            fragments=[
                Verifier(
                    identifier="07.01.03/01",
                    title=u"",
                    text=u"Er zijn regels voor acceptabel gebruik van bedrijfsmiddelen (met name internet, e-mail en "
                         u"mobiele apparatuur). Het ARAR verplicht ambtenaren zich hieraan te houden. Voor extern "
                         u"personeel is dit in het contract vastgelegd.",
                ),
                Verifier(
                    identifier="07.01.03/02",
                    title=u"",
                    text=u"Gebruikers hebben kennis van de regels.",
                ),
                Verifier(
                    identifier="07.01.03/03",
                    title=u"",
                    text=u"Apparatuur, informatie en programmatuur van de organisatie mogen niet zonder toestemming "
                         u"vooraf van de locatie worden meegenomen. De toestemming kan generiek geregeld worden in "
                         u"het kader van de functieafspraken tussen manager en medewerker.",
                ),
                Verifier(
                    identifier="07.01.03/04",
                    title=u"",
                    text=u"Informatiedragers worden dusdanig gebruikt dat vertrouwelijke informatie niet beschikbaar "
                         u"kan komen voor onbevoegde personen.",
                ),
            ],
        ),
    ],
)


S0702 = Section(
    identifier="07.02",
    title=u"Classificatie van informatie",
    fragments=[
        Norm(
            identifier="07.02.01",
            title=u"Richtlijnen voor classificatie van informatie",
            text=u"Informatie behoort te worden geclassificeerd met betrekking tot de waarde, wettelijke eisen, "
                 u"gevoeligheid en onmisbaarheid voor de",
            fragments=[
                Verifier(
                    identifier="07.02.01/01",
                    title=u"",
                    text=u"De organisatie heeft rubriceringrichtlijnen opgesteld (ter invulling van het VIRBI).",
                ),
            ],
        ),
        Norm(
            identifier="07.02.02",
            title=u"Labeling en verwerking van informatie",
            text=u"Er behoren geschikte, samenhangende procedures te worden ontwikkeld en geïmplementeerd voor de "
                 u"labeling en verwerking van informatie overeenkomstig het classificatiesysteem dat de organisatie "
                 u"heeft geïmplementeerd.",
            fragments=[
                Verifier(
                    identifier="07.02.02/01",
                    title=u"",
                    text=u"De lijnmanager heeft maatregelen (conform VIRBI) getroffen om te voorkomen dat niet "
                         u"geautoriseerde personen kennis kunnen nemen van gerubriceerde informatie.",
                ),
                Verifier(
                    identifier="07.02.02/02",
                    title=u"",
                    text=u"De opsteller van de informatie doet een voorstel tot rubricering en brengt deze aan op "
                         u"de informatie. De vaststeller van de inhoud van de informatie stelt tevens de rubricering "
                         u"vast.",
                ),
            ],
        ),
    ],
)


CH07 = Chapter(
    identifier="07",
    title=u"Beheer van bedrijfsmiddelen",
    fragments=[
        S0701,
        S0702,
    ]
)
