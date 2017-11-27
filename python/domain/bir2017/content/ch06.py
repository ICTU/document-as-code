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


S0601 = Section(
    identifier="06.01",
    title=u"",
    fragments=[

        Norm(
            identifier="06.01.01",
            title=u"",
            text=u"Rollen en verantwoordelijkheden bij informatiebeveiliging: Alle verantwoordelijkheden bij "
                 u"informatiebeveiliging behoren te worden gedefinieerd en toegewezen.",
            fragments=[
                Verifier(
                    identifier="06.01.01/01",
                    title=u"",
                    text=u"De leiding van de organisatie heeft vastgelegd wat de verantwoordelijkheden en rollen zijn "
                         u"op het gebied van informatiebeveiliging binnen haar organisatie.",
                ),
                Verifier(
                    identifier="06.01.01/02",
                    title=u"",
                    text=u"De verantwoordelijkheden en rollen ten aanzien van informatiebeveiliging zijn gebaseerd "
                         u"op relevante voorschriften en wetten, zoals het VIR, VIR-BI, BVR en AVG.",
                ),
                Verifier(
                    identifier="06.01.01/03",
                    title=u"",
                    text=u"De rol en verantwoordelijkheden van de Chief Information Security Officer (CISO) zijn "
                         u"in een CISO-functieprofiel vastgelegd.",
                ),
                Verifier(
                    identifier="06.01.01/04",
                    title=u"",
                    text=u"Er is een CISO aangesteld conform een vastgesteld CISO-functieprofiel.",
                ),
            ],
        ),

        Norm(
            identifier="06.01.02",
            title=u"",
            text=u"Scheiding van taken: Conflicterende taken en verantwoordelijkheden behoren te worden gescheiden om "
                 u"de kans op onbevoegd of onbedoeld wijzigen of misbruik van de bedrijfsmiddelen van de organisatie "
                 u"te verminderen.",
            fragments=[
                Verifier(
                    identifier="06.01.02/01",
                    title=u"",
                    text=u"Er zijn maatregelen getroffen die onbedoelde of ongeautoriseerde toegang tot "
                         u"bedrijfsmiddelen waarnemen of voorkomen.",
                ),
            ],
        ),

        Norm(
            identifier="06.01.03",
            title=u"",
            text=u"Contact met overheidsinstanties: Er behoren passende contacten met relevante overheidsinstanties "
                 u"te worden onderhouden.",
            fragments=[
                Verifier(
                    identifier="06.01.03/01",
                    title=u"",
                    text=u"Er is door de organisatie uitgewerkt wie met welke (overheids)instanties en "
                         u"toezichthouders contact heeft ten aanzien van informatiebeveiligingsaangelegenheden "
                         u"(vergunningen/incidenten/calamiteiten) en welke eisen voor deze aangelegenheden relevant "
                         u"zijn.",
                ),
                Verifier(
                    identifier="06.01.03/02",
                    title=u"",
                    text=u"Het contactoverzicht wordt jaarlijks geactualiseerd.",
                ),
            ],
        ),

        Norm(
            identifier="06.01.04",
            title=u"",
            text=u"(Vervallen)",
            fragments=[
            ],
        ),

        Norm(
            identifier="06.01.05",
            title=u"",
            text=u"Informatiebeveiliging in projectbeheer: Informatiebeveiliging behoort aan de orde te komen in "
                 u"projectbeheer, ongeacht het soort project.",
            fragments=[
            ],
        ),

    ],
)

S0602 = Section(
    identifier="06.02",
    title=u"",
    fragments=[

        Norm(
            identifier="06.02.01",
            title=u"",
            text=u"Beleid voor mobiele apparatuur: Beleid en ondersteunende beveiligingsmaatregelen behoren te worden "
                 u"vastgesteld om de risico?s die het gebruik van mobiele apparatuur met zich meebrengt te beheren.",
            fragments=[
                Verifier(
                    identifier="06.02.01/01",
                    title=u"",
                    text=u"Mobiele apparatuur is zo ingericht dat geen bedrijfsinformatie onbewust wordt opgeslagen "
                         u"(?zero footprint?). Als zero footprint (nog) niet realiseerbaar is, biedt een mobiel "
                         u"apparaat (zoals een laptop, tablet en smartphone) de mogelijkheid om de toegang te "
                         u"beschermen door middel van een toegangsbeveiligingsmechanisme en, indien vertrouwelijke "
                         u"gegevens worden opgeslagen, versleuteling van die gegevens. In het geval van opslag van "
                         u"vertrouwelijke informatie moet op deze mobiele apparatuur ?wissen op afstand? mogelijk "
                         u"zijn.",
                ),
                Verifier(
                    identifier="06.02.01/02",
                    title=u"",
                    text=u"Bij de inzet van mobiele apparatuur zijn minimaal de volgende aspecten geïmplementeerd: "
                         u"(a) in bewustwordingsprogramma?s komen gedragsaspecten van veilig mobiel werken aan de "
                         u"orde; (b) het device maakt onderdeel uit van patchmanagement en hardening; (c) het device "
                         u"wordt waar mogelijk beheerd en beveiligd via een Mobile Device management (MDM) -oplossing; "
                         u"(d) gebruikers tekenen een gebruikersovereenkomst voor mobiel werken, waarmee zij verklaren "
                         u"zich bewust te zijn van de gevaren van mobiel werken en verklaren dit veilig te zullen "
                         u"doen. Deze verklaring heeft betrekking op alle mobiele apparatuur die de medewerker "
                         u"zakelijk gebruikt; (e) periodiek wordt getoetst of de punten in lid b), c) en d) worden "
                         u"nageleefd.",
                ),
            ],
        ),

        Norm(
            identifier="06.02.02",
            title=u"",
            text=u"Telewerken: Beleid en ondersteunende beveiligingsmaatregelen behoren te worden geïmplementeerd ter "
                 u"beveiliging van informatie die vanaf telewerklocaties wordt benaderd, verwerkt of opgeslagen.",
            fragments=[
            ],
        ),

    ],
)

# ---


CH06 = Chapter(
    identifier="06",
    title=u"",
    fragments=[
        S0601,
        S0602,
    ]
)
