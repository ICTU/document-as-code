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


CH06S01 = Section(
    identifier="06.01",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="06.01.01",
            title=u"TITLE",
            text=u"""
Rollen en verantwoordelijkheden bij informatiebeveiliging;
Alle verantwoordelijkheden bij informatiebeveiliging behoren te worden gedefinieerd en toegewezen.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="06.01.01/01",
                    title=u"",
                    text=u"""
De leiding van de organisatie heeft vastgelegd wat de verantwoordelijkheden en rollen zijn op het gebied van informatiebeveiliging binnen haar organisatie.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/02",
                    title=u"",
                    text=u"""
De verantwoordelijkheden en rollen ten aanzien van informatiebeveiliging zijn gebaseerd op relevante voorschriften en wetten.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/02",
                    title=u"",
                    text=u"""
De verantwoordelijkheden en rollen ten aanzien van informatiebeveiliging zijn gebaseerd op relevante voorschriften en wetten.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/03",
                    title=u"",
                    text=u"""
De rol en verantwoordelijkheden van de Chief Information Security Officer (CISO) zijn in een CISO-functieprofiel vastgelegd.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/03",
                    title=u"",
                    text=u"""
De rol en verantwoordelijkheden van de Chief Information Security Officer (CISO) zijn in een CISO-functieprofiel vastgelegd.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/04",
                    title=u"",
                    text=u"""
Er is een CISO aangesteld conform een vastgesteld CISO-functieprofiel.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="06.01.02",
            title=u"TITLE",
            text=u"""
Scheiding van taken;
Conflicterende taken en verantwoordelijkheden behoren te worden gescheiden om de kans op onbevoegd of onbedoeld wijzigen of misbruik van de bedrijfsmiddelen van de organisatie te verminderen.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="06.01.02/01",
                    title=u"",
                    text=u"""
Er zijn maatregelen getroffen die onbedoelde of ongeautoriseerde toegang tot bedrijfsmiddelen waarnemen of voorkomen.
                    """,
                    bbn=1,
                )
            ],
        )
    ],
)


CH06S02 = Section(
    identifier="06.02",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="06.02.01",
            title=u"TITLE",
            text=u"""
Beleid voor mobiele apparatuur;
Beleid en ondersteunende beveiligingsmaatregelen behoren te worden vastgesteld om de risico’s die het gebruik van mobiele apparatuur met zich meebrengt te beheren.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="06.02.01/01",
                    title=u"",
                    text=u"""
Mobiele apparatuur is zo ingericht dat geen bedrijfsinformatie onbewust wordt opgeslagen (‘zero footprint’). Als zero footprint (nog) niet realiseerbaar is, biedt een mobiel apparaat (zoals een laptop, tablet en smartphone) de mogelijkheid om de toegang te beschermen door middel van een toegangsbeveiligingsmechanisme en, indien vertrouwelijke gegevens worden opgeslagen, versleuteling van die gegevens. In het geval van opslag van vertrouwelijke informatie moet op deze mobiele apparatuur ‘wissen op afstand’ mogelijk zijn.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="06.02.01/02",
                    title=u"",
                    text=u"""
Bij de inzet van mobiele apparatuur zijn minimaal de volgende aspecten geïmplementeerd:
a.    in bewustwordingsprogramma’s komen gedragsaspecten van veilig mobiel werken aan de orde; 
b.    het device maakt onderdeel uit van patchmanagement en hardening;
c.     het device wordt waar mogelijk beheerd en beveiligd via een MDM Mobile Device Management (MDM)-oplossing; 
d.    gebruikers tekenen een gebruikersovereenkomst voor mobiel werken, waarmee zij verklaren zich bewust te zijn van de gevaren van mobiel werken en verklaren dit veilig te zullen doen. Deze verklaring heeft betrekking op alle mobiele apparatuur die de medewerker zakelijk gebruikt;
e.    periodiek wordt getoetst of de punten in lid b), c) en d) worden nageleefd.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH06 = Chapter(
    identifier="06",
    title=u"TITLE",
    fragments=[
        CH06S01,
        CH06S02
    ]
)
