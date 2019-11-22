# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S1401 = Section(
    identifier="14.01",
    title="Informatiebeveiligingsaspecten van bedrijfscontinu�teitsbeheer",
    fragments=[
        Norm(
            identifier="14.01.01",
            title="Informatiebeveiliging opnemen in het proces van bedrijfscontinu�teitsbeheer",
            text="Er behoort een beheerd proces voor bedrijfscontinu�teit in de gehele organisatie te worden "
                 "ontwikkeld en bijgehouden, voor de naleving van eisen voor informatiebeveiliging die nodig "
                 "zijn voor de continu�teit van de bedrijfsvoering.",
            fragments=[
                Verifier(
                    identifier="14.01.01/01",
                    title="",
                    text="Calamiteitenplannen worden gebruikt in de jaarlijkse bewustwording-, training- en "
                         "testactiviteiten.",
                ),
            ],
        ),
        Norm(
            identifier="14.01.02",
            title="Bedrijfscontinu�teit en risicobeoordeling",
            text="Gebeurtenissen die tot onderbreking van bedrijfsprocessen kunnen leiden, behoren te worden "
                 "ge�dentificeerd, tezamen met de waarschijnlijkheid en de gevolgen van dergelijke onderbrekingen "
                 "en hun gevolgen voor informatiebeveiliging.",
            fragments=[
                Verifier(
                    identifier="14.01.02/01",
                    title="",
                    text="Er is een Business Impact Analyse (BIA) waarin de gebeurtenissen worden ge�dentificeerd "
                         "die kunnen leiden tot discontinu�teit in het bedrijfsproces. Aan de hand van een "
                         "risicoanalyse zijn de waarschijnlijkheid en de gevolgen van de discontinu�teit in "
                         "kaart gebracht in termen van tijd, schade en herstelperiode.",
                ),
            ],
        ),
        Norm(
            identifier="14.01.03",
            title="continu�teitsplannen ontwikkelen en implementeren waaronder informatiebeveiliging",
            text="Er behoren plannen te worden ontwikkeld en ge�mplementeerd om de bedrijfsactiviteiten te handhaven "
                 "of te herstellen en om de beschikbaarheid van informatie op het vereiste niveau en in de vereiste "
                 "tijdspanne te bewerkstelligen na onderbreking of uitval van kritische bedrijfsprocessen.",
            fragments=[
                Verifier(
                    identifier="14.01.03/01",
                    title="",
                    text="""In de continu�teitsplannen wordt minimaal aandacht besteed aan:
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
            title="Kader voor de bedrijfscontinu�teitsplanning",
            text="Er behoort een enkelvoudig kader voor bedrijfscontinu�teitsplannen te worden gehandhaafd om te "
                 "bewerkstelligen dat alle plannen consistent zijn, om eisen voor informatiebeveiliging op "
                 "consistente wijze te behandelen en om prioriteiten vast te stellen voor testen en onderhoud.",
            fragments=[
                Verifier(
                    identifier="14.01.04/01",
                    title="",
                    text="- conform norm -",
                ),
            ],
        ),
        Norm(
            identifier="14.01.05",
            title="Testen, onderhoud en herbeoordelen van bedrijfscontinu�teitsplannen",
            text="Bedrijfscontinu�teitsplannen behoren regelmatig te worden getest en ge�pdate, om te bewerkstelligen "
                 "dat ze actueel en doeltreffend blijven.",
            fragments=[
                Verifier(
                    identifier="14.01.05/01",
                    title="",
                    text="Er worden minimaal jaarlijks oefeningen en testen gehouden om de "
                         "bedrijfscontinu�teitsplannen en mate van readiness van de organisatie te toetsen "
                         "(opzet, bestaan en werking). Aan de hand van de resultaten worden de plannen bijgesteld "
                         "en wordt de organisatie bijgeschoold.",
                ),
            ],
        ),
    ],
)


CH14 = Chapter(
    identifier="14",
    title="Bedrijfscontinu�teitsbeheer",
    fragments=[
        S1401,
    ]
)
