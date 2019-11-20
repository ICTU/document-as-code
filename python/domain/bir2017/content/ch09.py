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


S0901 = Section(
    identifier="09.01",
    title=u"Bedrijfseisen voor toegangsbeveiliging",
    text=u"Doelstelling: Toegang tot informatie en informatieverwerkende faciliteiten beperken.",
    fragments=[

        Norm(
            identifier="09.01.01",
            title=u"Beleid voor toegangsbeveiliging",
            text=u"Een beleid voor toegangsbeveiliging behoort te worden vastgesteld, gedocumenteerd en beoordeeld op "
                 u"basis van bedrijfs- en informatiebeveiligingseisen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.01.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="09.01.02",
            title=u"Toegang tot netwerken en netwerkdiensten",
            text=u"Gebruikers behoren alleen toegang te krijgen tot het netwerk en de netwerkdiensten waarvoor zij "
                 u"specifiek bevoegd zijn.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.01.02/01",
                    title=u"",
                    text=u"Alleen geauthenticeerde apparatuur kan toegang krijgen tot een vertrouwde zone.",
                    bbn=1,
                ),

                Verifier(
                    identifier="09.01.02/02",
                    title=u"",
                    text=u"Gebruikers met eigen of ongeauthenticeerde apparatuur (Bring Your Own Device) krijgen "
                         u"alleen toegang tot een onvertrouwde zone.",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S0902 = Section(
    identifier="09.02",
    title=u"Beheer van toegangsrechten van gebruikers",
    text=u"Doelstelling: Toegang voor bevoegde gebruikers bewerkstelligen en onbevoegde toegang tot systemen en "
         u"diensten voorkomen.",
    fragments=[

        Norm(
            identifier="09.02.01",
            title=u"Registratie en afmelden van gebruikers",
            text=u"Een formele registratie- en afmeldingsprocedure behoort te worden geïmplementeerd om toewijzing "
                 u"van toegangsrechten mogelijk te maken.",
            bbn=1,
            fragments=[

                Verifier(
                    identifier="09.02.01/01",
                    title=u"",
                    text=u"Er is een sluitende formele registratie- en afmeldprocedure voor het beheren van "
                         u"gebruikersidentificaties.",
                    bbn=1,
                ),

                Verifier(
                    identifier="09.02.01/02",
                    title=u"",
                    text=u"Het gebruiken van groepsaccounts is niet toegestaan tenzij dit wordt gemotiveerd en "
                         u"vastgelegd door de proceseigenaar.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="09.02.02",
            title=u"Gebruikers toegang verlenen",
            text=u"Een formele gebruikerstoegangsverleningsprocedure behoort te worden geïmplementeerd om "
                 u"toegangsrechten voor alle typen gebruikers en voor alle systemen en diensten toe te wijzen of "
                 u"in te trekken.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.02/01",
                    title=u"",
                    text=u"Er is uitsluitend toegang verleend tot informatiesystemen na autorisatie door een "
                         u"bevoegde functionaris.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.02.02/02",
                    title=u"",
                    text=u"Op basis van een risicoafweging is bepaald waar en op welke wijze functiescheiding wordt "
                         u"toegepast en welke toegangsrechten worden gegeven.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.02.02/03",
                    title=u"",
                    text=u"Er is een actueel mandaatregister waaruit blijkt welke personen bevoegdheden hebben voor "
                         u"het verlenen van toegangsrechten dan wel functieprofielen.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.02.03",
            title=u"Beheren van speciale toegangsrechten",
            text=u"Het toewijzen en gebruik van speciale toegangsrechten behoren te worden beperkt en beheerst.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.03/01",
                    title=u"",
                    text=u"De uitgegeven speciale bevoegdheden worden minimaal ieder kwartaal beoordeeld.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.02.04",
            title=u"Beheer van geheime authenticatie-informatie van gebruikers",
            text=u"Het toewijzen van geheime authenticatie-informatie behoort te worden beheerst via een formeel "
                 u"beheersproces.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.04/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="09.02.05",
            title=u"Beoordeling van toegangsrechten van gebruikers",
            text=u"Eigenaren van bedrijfsmiddelen behoren toegangsrechten van gebruikers regelmatig te beoordelen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.05/01",
                    title=u"",
                    text=u"Alle uitgegeven toegangsrechten worden minimaal eenmaal per jaar beoordeeld.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.02.05/02",
                    title=u"",
                    text=u"De opvolging van bevindingen is gedocumenteerd en wordt behandeld als beveiligingsincident.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.02.05/03",
                    title=u"",
                    text=u"Alle uitgegeven toegangsrechten worden minimaal eenmaal per halfjaar beoordeeld.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.02.06",
            title=u"Toegangsrechten intrekken of aanpassen",
            text=u"De toegangsrechten van alle medewerkers en externe gebruikers voor informatie en "
                 u"informatieverwerkende faciliteiten behoren bij beëindiging van hun dienstverband, contract of "
                 u"overeenkomst te worden verwijderd, en bij wijzigingen behoren ze te worden aangepast.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.06/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S0903 = Section(
    identifier="09.03",
    title=u"Verantwoordelijkheden van gebruikers",
    text=u"Doelstelling: Gebruikers verantwoordelijk maken voor het beschermen van hun authenticatie-informatie.",
    fragments=[

        Norm(
            identifier="09.03.01",
            title=u"Geheime authenticatie-informatie gebruiken",
            text=u"Van gebruikers behoort te worden verlangd dat zij zich bij het gebruiken van geheime "
                 u"authenticatie-informatie houden aan de praktijk van de organisatie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.03.01/01",
                    title=u"",
                    text=u"Medewerkers worden ondersteund in het beheren van hun wachtwoorden door het beschikbaar "
                         u"stellen van een wachtwoordenkluis.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S0904 = Section(
    identifier="09.04",
    title=u"Toegangsbeveiliging van systeem en toepassing",
    text=u"Doelstelling: Onbevoegde toegang tot systemen en toepassingen voorkomen.",
    fragments=[

        Norm(
            identifier="09.04.01",
            title=u"Beperking toegang tot informatie",
            text=u"Toegang tot informatie en systeemfuncties van toepassingen behoort te worden beperkt in "
                 u"overeenstemming met het beleid voor toegangsbeveiliging.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.01/01",
                    title=u"",
                    text=u"Er zijn maatregelen genomen die het fysiek en/of logisch isoleren van informatie met "
                         u"specifiek belang waarborgen.",
                    bbn=2,
                ),
                Verifier(
                    identifier="09.04.01/02",
                    title=u"",
                    text=u"Gebruikers kunnen alleen die informatie met specifiek belang inzien en verwerken die "
                         u"ze nodig hebben voor de uitoefening van hun taak.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.04.02",
            title=u"Beveiligde inlogprocedures",
            text=u"Indien het beleid voor toegangsbeveiliging dit vereist, behoort toegang tot systemen en "
                 u"toepassingen te worden beheerst door een beveiligde inlogprocedure.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.02/01",
                    title=u"",
                    text=u"Als vanuit een onvertrouwde zone toegang wordt verleend naar een vertrouwde zone, gebeurt "
                         u"dit alleen op basis van minimaal two-factor authenticatie.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.04.02/02",
                    title=u"",
                    text=u"Voor het verlenen van toegang tot het netwerk door externe leveranciers wordt vooraf een "
                         u"risicoafweging gemaakt. De risicoafweging bepaalt onder welke voorwaarden de leveranciers "
                         u"toegang krijgen. Uit een registratie  blijkt hoe de rechten zijn toegekend.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.04.03",
            title=u"Systeem voor wachtwoordbeheer",
            text=u"Systemen voor wachtwoordbeheer behoren interactief te zijn en sterke wachtwoorden te waarborgen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.03/01",
                    title=u"",
                    text=u"Als er geen gebruik wordt gemaakt van two factor authentication is de wachtwoordlengte "
                         u"minimaal 8 posities en complex van samenstelling. Vanaf een wachtwoordlengte van "
                         u"20 posities vervalt de complexiteitseis. Het aantal inlogpogingen is maximaal 10. "
                         u"De tijdsduur dat een account wordt geblokkeerd na overschrijding van het aantal keer "
                         u"foutief inloggen is vastgelegd.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.04.03/02",
                    title=u"",
                    text=u"In situaties waar geen two-factor authenticatie mogelijk is, wordt minimaal halfjaarlijks "
                         u"het wachtwoord vernieuwd (zie ook 09.04.02/01.).",
                    bbn=2,
                ),
                Verifier(
                    identifier="09.04.03/03",
                    title=u"",
                    text=u"Het wachtwoordbeleid wordt geautomatiseerd afgedwongen.",
                    bbn=2,
                ),
                Verifier(
                    identifier="09.04.03/04",
                    title=u"",
                    text=u"Initiële wachtwoorden en wachtwoorden die gereset zijn, hebben een maximale geldigheidsduur "
                         u"van een werkdag en moeten bij het eerste gebruik worden gewijzigd.",
                    bbn=2,
                ),
                Verifier(
                    identifier="09.04.03/05",
                    title=u"",
                    text=u"Wachtwoorden die voldoen aan het wachtwoordbeleid hebben een maximale geldigheidsduur "
                         u"van een jaar. Daar waar het beleid niet toepasbaar is, geldt een maximale geldigheidsduur "
                         u"van 6 maanden.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.04.04",
            title=u"Speciale systeemhulpmiddelen gebruiken",
            text=u"Het gebruik van systeemhulpmiddelen die in staat zijn om beheersmaatregelen voor systemen en "
                 u"toepassingen te omzeilen behoort te worden beperkt en nauwkeurig te worden gecontroleerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.04/01",
                    title=u"",
                    text=u"Alleen bevoegd personeel heeft toegang tot systeemhulpmiddelen.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.04.04/02",
                    title=u"",
                    text=u"Het gebruik van systeemhulpmiddelen wordt gelogd. "
                         u"De logging is een halfjaar beschikbaar voor onderzoek.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.04.05",
            title=u"Toegangsbeveiliging op programmabroncode",
            text=u"Toegang tot de programmabroncode behoort te worden beperkt.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.05/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


CH09 = Chapter(
    identifier="09",
    title=u"Toegangsbeveiliging",
    fragments=[
        S0901,
        S0902,
        S0903,
        S0904,
    ]
)
