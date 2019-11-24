# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S0601 = Section(
    identifier="06.01",
    title="Interne organisatie",
    text="Doelstelling: Een beheerkader vaststellen om de implementatie en uitvoering van de informatiebeveiliging "
         "binnen de organisatie te initi&euml;ren en te beheersen.",
    fragments=[

        Norm(
            identifier="06.01.01",
            title="Rollen en verantwoordelijkheden bij informatiebeveiliging",
            text="Alle verantwoordelijkheden bij informatiebeveiliging behoren te worden gedefinieerd en toegewezen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="06.01.01/01",
                    title="",
                    text="De leiding van de organisatie heeft vastgelegd wat de verantwoordelijkheden en rollen zijn "
                         "op het gebied van informatiebeveiliging binnen haar organisatie.",
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/02",
                    title="",
                    text="De verantwoordelijkheden en rollen ten aanzien van informatiebeveiliging zijn gebaseerd "
                         "op relevante voorschriften en wetten, zoals het VIR, VIR-BI, BVR en AVG.",
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/03",
                    title="",
                    text="De rol en verantwoordelijkheden van de Chief Information Security Officer (CISO) zijn "
                         "in een CISO-functieprofiel vastgelegd.",
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/04",
                    title="",
                    text="Er is een CISO aangesteld conform een vastgesteld CISO-functieprofiel.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="06.01.02",
            title="Scheiding van taken",
            text="Conflicterende taken en verantwoordelijkheden behoren te worden gescheiden om "
                 "de kans op onbevoegd of onbedoeld wijzigen of misbruik van de bedrijfsmiddelen van de organisatie "
                 "te verminderen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="06.01.02/01",
                    title="",
                    text="Er zijn maatregelen getroffen die onbedoelde of ongeautoriseerde toegang tot "
                         "bedrijfsmiddelen waarnemen of voorkomen.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="06.01.03",
            title="Contact met overheidsinstanties",
            text="Er behoren passende contacten met relevante overheidsinstanties "
                 "te worden onderhouden.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="06.01.03/01",
                    title="",
                    text="Er is door de organisatie uitgewerkt wie met welke (overheids)instanties en "
                         "toezichthouders contact heeft ten aanzien van informatiebeveiligingsaangelegenheden "
                         "(vergunningen/incidenten/calamiteiten) en welke eisen voor deze aangelegenheden relevant "
                         "zijn.",
                    bbn=2,
                ),
                Verifier(
                    identifier="06.01.03/02",
                    title="",
                    text="Het contactoverzicht wordt jaarlijks geactualiseerd.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="06.01.04",
            title=" ",
            text="(Vervallen)",
            fragments=[
            ],
        ),

        Norm(
            identifier="06.01.05",
            title="Informatiebeveiliging in projectbeheer",
            text="Informatiebeveiliging behoort aan de orde te komen in "
                 "projectbeheer, ongeacht het soort project.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="06.01.05/01",
                    title="",
                    text="- conform norm -",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S0602 = Section(
    identifier="06.02",
    title="Mobiele apparatuur en telewerken",
    text="Doelstelling: Het waarborgen van de veiligheid van telewerken en het gebruik van mobiele apparatuur.",
    fragments=[

        Norm(
            identifier="06.02.01",
            title="Beleid voor mobiele apparatuur",
            text="Beleid en ondersteunende beveiligingsmaatregelen behoren te worden "
                 "vastgesteld om de risico's die het gebruik van mobiele apparatuur met zich meebrengt te beheren.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="06.02.01/01",
                    title="",
                    text="Mobiele apparatuur is zo ingericht dat geen bedrijfsinformatie onbewust wordt opgeslagen "
                         "('zero footprint'). Als zero footprint (nog) niet realiseerbaar is, biedt een mobiel "
                         "apparaat (zoals een laptop, tablet en smartphone) de mogelijkheid om de toegang te "
                         "beschermen door middel van een toegangsbeveiligingsmechanisme en, indien vertrouwelijke "
                         "gegevens worden opgeslagen, versleuteling van die gegevens. In het geval van opslag van "
                         "vertrouwelijke informatie moet op deze mobiele apparatuur 'wissen op afstand' mogelijk "
                         "zijn.",
                    bbn=2,
                ),
                Verifier(
                    identifier="06.02.01/02",
                    title="",
                    text="Bij de inzet van mobiele apparatuur zijn minimaal de volgende aspecten ge&iuml;mplementeerd: "
                         "<ol style='list-style-type: lower-alpha;'>"
                         "<li>in bewustwordingsprogramma's komen gedragsaspecten van veilig mobiel werken aan de "
                         "orde;</li>"
                         "<li>het device maakt onderdeel uit van patchmanagement en hardening;</li>"
                         "<li>het device wordt waar mogelijk beheerd en beveiligd via een MDM Mobile Device Management "
                         "(MDM)-oplossing;</li>"
                         "<li>gebruikers tekenen een gebruikersovereenkomst voor mobiel werken, waarmee zij verklaren "
                         "zich bewust te zijn van de gevaren van mobiel werken en verklaren dit veilig te zullen "
                         "doen. Deze verklaring heeft betrekking op alle mobiele apparatuur die de medewerker "
                         "zakelijk gebruikt;</li>"
                         "<li>periodiek wordt getoetst of de punten in lid b, c en d worden nageleefd.</li>"
                         "</ol>",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="06.02.02",
            title="Telewerken",
            text="Beleid en ondersteunende beveiligingsmaatregelen behoren te worden ge&iuml;mplementeerd ter "
                 "beveiliging van informatie die vanaf telewerklocaties wordt benaderd, verwerkt of opgeslagen.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="06.02.02/01",
                    title="",
                    text="- conform norm -",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH06 = Chapter(
    identifier="06",
    title="Organiseren van informatiebeveiliging",
    fragments=[
        S0601,
        S0602,
    ]
)
