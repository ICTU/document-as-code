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
    title=u"Informatiebeveiligingsaspecten van bedrijfscontinu�teitsbeheer",
    fragments=[
        Norm(
            identifier="14.01.01",
            title=u"Informatiebeveiliging opnemen in het proces van bedrijfscontinu�teitsbeheer",
            text=u"Er behoort een beheerd proces voor bedrijfscontinu�teit in de gehele organisatie te worden "
                 u"ontwikkeld en bijgehouden, voor de naleving van eisen voor informatiebeveiliging die nodig "
                 u"zijn voor de continu�teit van de bedrijfsvoering.",
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
            title=u"Bedrijfscontinu�teit en risicobeoordeling",
            text=u"Gebeurtenissen die tot onderbreking van bedrijfsprocessen kunnen leiden, behoren te worden "
                 u"ge�dentificeerd, tezamen met de waarschijnlijkheid en de gevolgen van dergelijke onderbrekingen "
                 u"en hun gevolgen voor informatiebeveiliging.",
            fragments=[
                Verifier(
                    identifier="14.01.02/01",
                    title=u"",
                    text=u"Er is een Business Impact Analyse (BIA) waarin de gebeurtenissen worden ge�dentificeerd "
                         u"die kunnen leiden tot discontinu�teit in het bedrijfsproces. Aan de hand van een "
                         u"risicoanalyse zijn de waarschijnlijkheid en de gevolgen van de discontinu�teit in "
                         u"kaart gebracht in termen van tijd, schade en herstelperiode.",
                ),
            ],
        ),
        Norm(
            identifier="14.01.03",
            title=u"continu�teitsplannen ontwikkelen en implementeren waaronder informatiebeveiliging",
            text=u"Er behoren plannen te worden ontwikkeld en ge�mplementeerd om de bedrijfsactiviteiten te handhaven "
                 u"of te herstellen en om de beschikbaarheid van informatie op het vereiste niveau en in de vereiste "
                 u"tijdspanne te bewerkstelligen na onderbreking of uitval van kritische bedrijfsprocessen.",
            fragments=[
                Verifier(
                    identifier="14.01.03/01",
                    title=u"",
                    text=u"""In de continu�teitsplannen wordt minimaal aandacht besteed aan:
<ul>
<li>Identificatie van essenti�le procedures voor bedrijfscontinu�teit.</li>
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
            title=u"Kader voor de bedrijfscontinu�teitsplanning",
            text=u"Er behoort een enkelvoudig kader voor bedrijfscontinu�teitsplannen te worden gehandhaafd om te "
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
            title=u"Testen, onderhoud en herbeoordelen van bedrijfscontinu�teitsplannen",
            text=u"Bedrijfscontinu�teitsplannen behoren regelmatig te worden getest en ge�pdate, om te bewerkstelligen "
                 u"dat ze actueel en doeltreffend blijven.",
            fragments=[
                Verifier(
                    identifier="14.01.05/01",
                    title=u"",
                    text=u"Er worden minimaal jaarlijks oefeningen en testen gehouden om de "
                         u"bedrijfscontinu�teitsplannen en mate van readiness van de organisatie te toetsen "
                         u"(opzet, bestaan en werking). Aan de hand van de resultaten worden de plannen bijgesteld "
                         u"en wordt de organisatie bijgeschoold.",
                ),
            ],
        ),
    ],
)


CH14 = Chapter(
    identifier="14",
    title=u"Bedrijfscontinu�teitsbeheer",
    fragments=[
        S1401,
    ]
)
