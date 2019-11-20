# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.bio.model.norm import Norm
from domain.bio.model.verifier import Verifier
from domain.document.model.chapter import Chapter
from domain.document.model.section import Section


CH09S01 = Section(
    identifier="09.01",
    title=u"TITLE",
    text=u"text",
    fragments=[
        
    ],
)


CH09S02 = Section(
    identifier="09.02",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="09.02.01",
            title=u"TITLE",
            text=u"""
Registratie en afmelden van gebruikers;
Een formele registratie- en afmeldingsprocedure behoort te worden geïmplementeerd om toewijzing van toegangsrechten mogelijk te maken.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.01/01",
                    title=u"",
                    text=u"""
Er is een sluitende formele registratie- en afmeldprocedure voor het beheren van gebruikersidentificaties.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="09.02.01/02",
                    title=u"",
                    text=u"""
Het gebruiken van groepsaccounts is niet toegestaan tenzij dit wordt gemotiveerd en vastgelegd door de proceseigenaar..
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="09.02.02",
            title=u"TITLE",
            text=u"""
Gebruikers toegang verlenen;
Een formele gebruikerstoegangsverleningsprocedure behoort te worden geïmplementeerd om toegangsrechten voor alle typen gebruikers en voor alle systemen en diensten toe te wijzen of in te trekken.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.02/01",
                    title=u"",
                    text=u"""
Er is uitsluitend toegang verleend tot informatiesystemen na autorisatie door een bevoegde functionaris.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="09.02.02/02",
                    title=u"",
                    text=u"""
Op basis van een risicoafweging is bepaald waar en op welke wijze functiescheiding wordt toegepast en welke toegangsrechten worden gegeven.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="09.02.02/03",
                    title=u"",
                    text=u"""
Er is een actueel mandaatregister waaruit blijkt welke personen bevoegdheden hebben voor het verlenen van toegangsrechten dan wel functieprofielen.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="09.02.03",
            title=u"TITLE",
            text=u"""
Beheren van speciale toegangsrechten;
Het toewijzen en gebruik van speciale toegangsrechten behoren te worden beperkt en beheerst.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="09.02.03/01",
                    title=u"",
                    text=u"""
De uitgegeven speciale bevoegdheden worden minimaal ieder kwartaal beoordeeld.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH09S03 = Section(
    identifier="09.03",
    title=u"TITLE",
    text=u"text",
    fragments=[
        
    ],
)


CH09S04 = Section(
    identifier="09.04",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="09.04.01",
            title=u"TITLE",
            text=u"""
Beperking toegang tot informatie;
Toegang tot informatie en systeemfuncties van toepassingen behoort te worden beperkt in overeenstemming met het beleid voor toegangsbeveiliging.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="09.04.01/01",
                    title=u"",
                    text=u"""
Er zijn maatregelen genomen die het fysiek en/of logisch isoleren van informatie met specifiek belang waarborgen.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="09.04.01/02",
                    title=u"",
                    text=u"""
Gebruikers kunnen alleen die informatie met specifiek belang inzien en verwerken die ze nodig hebben voor de uitoefening van hun taak.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="09.04.02",
            title=u"TITLE",
            text=u"""
Beveiligde inlogprocedures;
Indien het beleid voor toegangsbeveiliging dit vereist, behoort toegang tot systemen en toepassingen te worden beheerst door een beveiligde inlogprocedure.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.02/01",
                    title=u"",
                    text=u"""
Als vanuit een onvertrouwde zone toegang wordt verleend naar een vertrouwde zone, gebeurt dit alleen op basis van minimaal two-factor authenticatie.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="09.04.02/02",
                    title=u"",
                    text=u"""
Voor het verlenen van toegang tot het netwerk door externe leveranciers wordt vooraf een risicoafweging gemaakt. De risicoafweging bepaalt onder welke voorwaarden de leveranciers toegang krijgen. Uit een registratie blijkt hoe de rechten zijn toegekend.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="09.04.03",
            title=u"TITLE",
            text=u"""
Systeem voor wachtwoordbeheer;
Systemen voor wachtwoordbeheer behoren interactief te zijn en sterke wachtwoorden te waarborgen.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.03/01",
                    title=u"",
                    text=u"""
Als er geen gebruik wordt gemaakt van two-factor authenticatie is de wachtwoordlengte minimaal 8 posities en complex van samenstelling. Vanaf een wachtwoordlengte van 20 posities vervalt de complexiteitseis. Het aantal inlogpogingen is maximaal 10. De tijdsduur dat een account wordt geblokkeerd na overschrijding van het aantal keer foutief inloggen is vastgelegd.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="09.04.03/02",
                    title=u"",
                    text=u"""
In situaties waar geen two-factor authenticatie mogelijk is, wordt minimaal halfjaarlijks het wachtwoord vernieuwd (zie ook 9.4.2.1.).
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="09.04.03/03",
                    title=u"",
                    text=u"""
Het wachtwoordbeleid wordt geautomatiseerd afgedwongen.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="09.04.03/04",
                    title=u"",
                    text=u"""
Initiële wachtwoorden en wachtwoorden die gereset zijn, hebben een maximale geldigheidsduur van een werkdag en moeten bij het eerste gebruik worden gewijzigd.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="09.04.03/05",
                    title=u"",
                    text=u"""
Wachtwoorden die voldoen aan het wachtwoordbeleid hebben een maximale geldigheidsduur van een jaar. Daar waar het beleid niet toepasbaar is, geldt een maximale geldigheidsduur van 6 maanden.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="09.04.04",
            title=u"TITLE",
            text=u"""
Speciale systeemhulpmiddelen gebruiken;
Het gebruik van systeemhulpmiddelen die in staat zijn om beheersmaatregelen voor systemen en toepassingen te omzeilen behoort te worden beperkt en nauwkeurig te worden gecontroleerd.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.04/01",
                    title=u"",
                    text=u"""
Alleen bevoegd personeel heeft toegang tot systeemhulpmiddelen.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="09.04.04/02",
                    title=u"",
                    text=u"""
Het gebruik van systeemhulpmiddelen wordt gelogd. De logging is een halfjaar beschikbaar voor onderzoek
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH09 = Chapter(
    identifier="09",
    title=u"TITLE",
    fragments=[
        CH09S01,
        CH09S02,
        CH09S03,
        CH09S04
    ]
)
