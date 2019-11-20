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


S1401 = Section(
    identifier="14.01",
    title=u"Informatiebeveiligingsaspecten van bedrijfscontinuïteitsbeheer",
    fragments=[
        Norm(
            identifier="14.01.01",
            title=u"Informatiebeveiliging opnemen in het proces van bedrijfscontinuïteitsbeheer",
            text=u"Er behoort een beheerd proces voor bedrijfscontinuïteit in de gehele organisatie te worden "
                 u"ontwikkeld en bijgehouden, voor de naleving van eisen voor informatiebeveiliging die nodig "
                 u"zijn voor de continuïteit van de bedrijfsvoering.",
            fragments=[
                Verifier(
                    identifier="14.01.01/01",
                    title=u"",
                    text=u"Calamiteitenplannen worden gebruikt in de jaarlijkse bewustwording-, training- en "
                         u"testactiviteiten.",
                ),
            ],
        ),
        Norm(
            identifier="14.01.02",
            title=u"Bedrijfscontinuïteit en risicobeoordeling",
            text=u"Gebeurtenissen die tot onderbreking van bedrijfsprocessen kunnen leiden, behoren te worden "
                 u"geïdentificeerd, tezamen met de waarschijnlijkheid en de gevolgen van dergelijke onderbrekingen "
                 u"en hun gevolgen voor informatiebeveiliging.",
            fragments=[
                Verifier(
                    identifier="14.01.02/01",
                    title=u"",
                    text=u"Er is een Business Impact Analyse (BIA) waarin de gebeurtenissen worden geïdentificeerd "
                         u"die kunnen leiden tot discontinuïteit in het bedrijfsproces. Aan de hand van een "
                         u"risicoanalyse zijn de waarschijnlijkheid en de gevolgen van de discontinuïteit in "
                         u"kaart gebracht in termen van tijd, schade en herstelperiode.",
                ),
            ],
        ),
        Norm(
            identifier="14.01.03",
            title=u"continuïteitsplannen ontwikkelen en implementeren waaronder informatiebeveiliging",
            text=u"Er behoren plannen te worden ontwikkeld en geïmplementeerd om de bedrijfsactiviteiten te handhaven "
                 u"of te herstellen en om de beschikbaarheid van informatie op het vereiste niveau en in de vereiste "
                 u"tijdspanne te bewerkstelligen na onderbreking of uitval van kritische bedrijfsprocessen.",
            fragments=[
                Verifier(
                    identifier="14.01.03/01",
                    title=u"",
                    text=u"""In de continuïteitsplannen wordt minimaal aandacht besteed aan:
<ul>
<li>Identificatie van essentiële procedures voor bedrijfscontinuïteit.</li>
<li>Veilig te stellen informatie (aanvaardbaarheid van verlies van informatie).</li>
<li>Prioriteiten en volgorde van herstel en reconstructie.</li>
<li>Documentatie van systemen en processen.</li>
<li>Kennis en kundigheid van personeel om de processen weer op te starten.</li>
</ul>""",
                ),
            ],
        ),
        Norm(
            identifier="14.01.04",
            title=u"Kader voor de bedrijfscontinuïteitsplanning",
            text=u"Er behoort een enkelvoudig kader voor bedrijfscontinuïteitsplannen te worden gehandhaafd om te "
                 u"bewerkstelligen dat alle plannen consistent zijn, om eisen voor informatiebeveiliging op "
                 u"consistente wijze te behandelen en om prioriteiten vast te stellen voor testen en onderhoud.",
            fragments=[
                Verifier(
                    identifier="14.01.04/01",
                    title=u"",
                    text=u"- conform norm -",
                ),
            ],
        ),
        Norm(
            identifier="14.01.05",
            title=u"Testen, onderhoud en herbeoordelen van bedrijfscontinuïteitsplannen",
            text=u"Bedrijfscontinuïteitsplannen behoren regelmatig te worden getest en geüpdate, om te bewerkstelligen "
                 u"dat ze actueel en doeltreffend blijven.",
            fragments=[
                Verifier(
                    identifier="14.01.05/01",
                    title=u"",
                    text=u"Er worden minimaal jaarlijks oefeningen en testen gehouden om de "
                         u"bedrijfscontinuïteitsplannen en mate van readiness van de organisatie te toetsen "
                         u"(opzet, bestaan en werking). Aan de hand van de resultaten worden de plannen bijgesteld "
                         u"en wordt de organisatie bijgeschoold.",
                ),
            ],
        ),
    ],
)


CH14 = Chapter(
    identifier="14",
    title=u"Bedrijfscontinuïteitsbeheer",
    fragments=[
        S1401,
    ]
)
