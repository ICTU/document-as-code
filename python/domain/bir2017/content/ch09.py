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

S0901 = Section(
    identifier="09.01",
    title=u"",
    fragments=[

        Norm(
            identifier="09.01.01",
            title=u"",
            text=u"Beleid voor toegangsbeveiliging: Een beleid voor toegangsbeveiliging behoort te worden vastgesteld, "
                 u"gedocumenteerd en beoordeeld op basis van bedrijfs- en informatiebeveiligingseisen.",
            fragments=[
            ],
        ),

        Norm(
            identifier="09.01.02",
            title=u"",
            text=u"Toegang tot netwerken en netwerkdiensten: Gebruikers behoren alleen toegang te krijgen tot het "
                 u"netwerk en de netwerkdiensten waarvoor zij specifiek bevoegd zijn.",
            fragments=[
                Verifier(
                    identifier="09.01.02/01",
                    title=u"",
                    text=u"Alleen geauthenticeerde apparatuur kan toegang krijgen tot een vertrouwde zone.",
                ),

                Verifier(
                    identifier="09.01.02/02",
                    title=u"",
                    text=u"Gebruikers met eigen of ongeauthenticeerde apparatuur (Bring Your Own Device) krijgen "
                         u"alleen toegang tot een onvertrouwde zone.",
                ),
            ],
        ),

    ],
)


S0902 = Section(
    identifier="09.02",
    title=u"",
    fragments=[

        Norm(
            identifier="09.02.01",
            title=u"",
            text=u"Registratie en afmelden van gebruikers: Een formele registratie- en afmeldingsprocedure behoort "
                 u"te worden geïmplementeerd om toewijzing van toegangsrechten mogelijk te maken.",
            fragments=[
            ],
        ),

        Verifier(
            identifier="09.02.01/01",
            title=u"",
            text=u"Er is een sluitende formele registratie- en afmeldprocedure voor het beheren van "
                 u"gebruikersidentificaties.",
        ),

        Verifier(
            identifier="09.02.01/02",
            title=u"",
            text=u"Het gebruiken van groepsaccounts is niet toegestaan tenzij dit wordt gemotiveerd en vastgelegd "
                 u"door de proceseigenaar.",
        ),

        Norm(
            identifier="09.02.02",
            title=u"",
            text=u"Gebruikers toegang verlenen: Een formele gebruikerstoegangsverleningsprocedure behoort te worden "
                 u"geïmplementeerd om toegangsrechten voor alle typen gebruikers en voor alle systemen en diensten "
                 u"toe te wijzen of in te trekken.",
            fragments=[
                Verifier(
                    identifier="09.02.02/01",
                    title=u"",
                    text=u"Er is uitsluitend toegang verleend tot informatiesystemen na autorisatie door een "
                         u"bevoegde functionaris.",
                ),
                Verifier(
                    identifier="09.02.02/02",
                    title=u"",
                    text=u"Op basis van een risicoafweging is bepaald waar en op welke wijze functiescheiding wordt "
                         u"toegepast en welke toegangsrechten worden gegeven.",
                ),
                Verifier(
                    identifier="09.02.02/03",
                    title=u"",
                    text=u"Er is een actueel mandaatregister waaruit blijkt welke personen bevoegdheden hebben voor "
                         u"het verlenen van toegangsrechten dan wel functieprofielen.",
                ),
            ],
        ),

        Norm(
            identifier="09.02.03",
            title=u"",
            text=u"Beheren van speciale toegangsrechten: Het toewijzen en gebruik van speciale toegangsrechten "
                 u"behoren te worden beperkt en beheerst.",
            fragments=[
            ],
        ),

        Verifier(
            identifier="09.02.03/01",
            title=u"",
            text=u"De uitgegeven speciale bevoegdheden worden minimaal ieder kwartaal beoordeeld.",
        ),

        Norm(
            identifier="09.02.04",
            title=u"",
            text=u"Beheer van geheime authenticatie-informatie van gebruikers: Het toewijzen van geheime "
                 u"authenticatie-informatie behoort te worden beheerst via een formeel beheersproces.",
            fragments=[
            ],
        ),

        Norm(
            identifier="09.02.05",
            title=u"",
            text=u"Beoordeling van toegangsrechten van gebruikers: Eigenaren van bedrijfsmiddelen behoren "
                 u"toegangsrechten van gebruikers regelmatig te beoordelen.",
            fragments=[
                Verifier(
                    identifier="09.02.05/01",
                    title=u"",
                    text=u"Alle uitgegeven toegangsrechten worden minimaal eenmaal per jaar beoordeeld.",
                ),
                Verifier(
                    identifier="09.02.05/02",
                    title=u"",
                    text=u"De opvolging van bevindingen is gedocumenteerd en wordt behandeld als beveiligingsincident.",
                ),
                Verifier(
                    identifier="09.02.05/03",
                    title=u"",
                    text=u"Alle uitgegeven toegangsrechten worden minimaal eenmaal per halfjaar beoordeeld.",
                ),
            ],
        ),

        Norm(
            identifier="09.02.06",
            title=u"",
            text=u"Toegangsrechten intrekken of aanpassen: De toegangsrechten van alle medewerkers en externe "
                 u"gebruikers voor informatie en informatieverwerkende faciliteiten behoren bij beëindiging van "
                 u"hun dienstverband, contract of overeenkomst te worden verwijderd, en bij wijzigingen behoren ze "
                 u"te worden aangepast.",
            fragments=[
            ],
        ),

    ],
)


S0903 = Section(
    identifier="09.03",
    title=u"",
    fragments=[

        Norm(
            identifier="09.03.01",
            title=u"",
            text=u"Geheime authenticatie-informatie gebruiken: Van gebruikers behoort te worden verlangd dat zij zich "
                 u"bij het gebruiken van geheime authenticatie-informatie houden aan de praktijk van de organisatie.",
            fragments=[
                Verifier(
                    identifier="09.03.01/01",
                    title=u"",
                    text=u"Medewerkers worden ondersteund in het beheren van hun wachtwoorden door het beschikbaar "
                         u"stellen van een wachtwoordenkluis.",
                ),
            ],
        ),

    ],
)


S0904 = Section(
    identifier="09.04",
    title=u"",
    fragments=[

        Norm(
            identifier="09.04.01",
            title=u"",
            text=u"Beperking toegang tot informatie: Toegang tot informatie en systeemfuncties van toepassingen "
                 u"behoort te worden beperkt in overeenstemming met het beleid voor toegangsbeveiliging.",
            fragments=[
                Verifier(
                    identifier="09.04.01/01",
                    title=u"",
                    text=u"Er zijn maatregelen genomen die het fysiek en/of logisch isoleren van informatie met "
                         u"specifiek belang waarborgen.",
                ),
                Verifier(
                    identifier="09.04.01/02",
                    title=u"",
                    text=u"Gebruikers kunnen alleen die informatie met specifiek belang inzien en verwerken die "
                         u"ze nodig hebben voor de uitoefening van hun taak.",
                ),
            ],
        ),

        Norm(
            identifier="09.04.02",
            title=u"",
            text=u"Beveiligde inlogprocedures: Indien het beleid voor toegangsbeveiliging dit vereist, behoort toegang "
                 u"tot systemen en toepassingen te worden beheerst door een beveiligde inlogprocedure.",
            fragments=[
                Verifier(
                    identifier="09.04.02/01",
                    title=u"",
                    text=u"Als vanuit een onvertrouwde zone toegang wordt verleend naar een vertrouwde zone, gebeurt "
                         u"dit alleen op basis van minimaal two-factor authenticatie.",
                ),
                Verifier(
                    identifier="09.04.02/02",
                    title=u"",
                    text=u"Voor het verlenen van toegang tot het netwerk door externe leveranciers wordt vooraf een "
                         u"risicoafweging gemaakt. De risicoafweging bepaalt onder welke voorwaarden de leveranciers "
                         u"toegang krijgen. Uit een registratie  blijkt hoe de rechten zijn toegekend.",
                ),
            ],
        ),

        Norm(
            identifier="09.04.03",
            title=u"",
            text=u"Systeem voor wachtwoordbeheer: Systemen voor wachtwoordbeheer behoren interactief te zijn en "
                 u"sterke wachtwoorden te waarborgen.",
            fragments=[
                Verifier(
                    identifier="09.04.03/01",
                    title=u"",
                    text=u"Als er geen gebruik wordt gemaakt van two factor authentication is de wachtwoordlengte "
                         u"minimaal 8 posities en complex van samenstelling. Vanaf een wachtwoordlengte van "
                         u"20 posities vervalt de complexiteitseis. Het aantal inlogpogingen is maximaal 10. "
                         u"De tijdsduur dat een account wordt geblokkeerd na overschrijding van het aantal keer "
                         u"foutief inloggen is vastgelegd.",
                ),
                Verifier(
                    identifier="09.04.03/02",
                    title=u"",
                    text=u" In situaties waar geen two-factor authenticatie mogelijk is, wordt minimaal halfjaarlijks "
                         u"het wachtwoord vernieuwd (zie ook 9.04.02/01.).",
                ),
                Verifier(
                    identifier="09.04.03/03",
                    title=u"",
                    text=u"Het wachtwoordbeleid wordt geautomatiseerd afgedwongen.",
                ),
                Verifier(
                    identifier="09.04.03/04",
                    title=u"",
                    text=u"Initiële wachtwoorden en wachtwoorden die gereset zijn, hebben een maximale geldigheidsduur "
                         u"van een werkdag en moeten bij het eerste gebruik worden gewijzigd.",
                ),
                Verifier(
                    identifier="09.04.03/05",
                    title=u"",
                    text=u"Wachtwoorden die voldoen aan het wachtwoordbeleid hebben een maximale geldigheidsduur "
                         u"van een jaar. Daar waar het beleid niet toepasbaar is, geldt een maximale geldigheidsduur "
                         u"van 6 maanden.",
                ),
            ],
        ),

        Norm(
            identifier="09.04.04",
            title=u"",
            text=u"Speciale systeemhulpmiddelen gebruiken: Het gebruik van systeemhulpmiddelen die in staat zijn "
                 u"om beheersmaatregelen voor systemen en toepassingen te omzeilen behoort te worden beperkt en "
                 u"nauwkeurig te worden gecontroleerd.",
            fragments=[
                Verifier(
                    identifier="09.04.04/01",
                    title=u"",
                    text=u"Alleen bevoegd personeel heeft toegang tot systeemhulpmiddelen.",
                ),
                Verifier(
                    identifier="09.04.04/02",
                    title=u"",
                    text=u"Het gebruik van systeemhulpmiddelen wordt gelogd. "
                         u"De logging is een halfjaar beschikbaar voor onderzoek.",
                ),
            ],
        ),

        Norm(
            identifier="09.04.05",
            title=u"",
            text=u"Toegangsbeveiliging op programmabroncode: Toegang tot de programmabroncode behoort "
                 u"te worden beperkt.",
            fragments=[
            ],
        ),

    ],
)


CH09 = Chapter(
    identifier="09",
    title=u"Access control",
    fragments=[
        S0901,
        S0902,
        S0903,
        S0904,
    ]
)
