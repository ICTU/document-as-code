# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH09S01 = Section(
    identifier="09.01",
    title="Bedrijfseisen voor toegangsbeveiliging",
    text="Doelstelling: Toegang tot informatie en informatieverwerkende faciliteiten beperken.",
    fragments=[

        Norm(
            identifier="09.01.01",
            title="Beleid voor toegangsbeveiliging",
            text="Een beleid voor toegangsbeveiliging behoort te worden vastgesteld, gedocumenteerd en beoordeeld op "
                 "basis van bedrijfs- en informatiebeveiligingseisen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.01.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="09.01.02",
            title="Toegang tot netwerken en netwerkdiensten",
            text="Gebruikers behoren alleen toegang te krijgen tot het netwerk en de netwerkdiensten waarvoor zij "
                 "specifiek bevoegd zijn.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.01.02/01",
                    title="",
                    text="Alleen geauthenticeerde apparatuur kan toegang krijgen tot een vertrouwde zone.",
                    bbn=1,
                ),

                Verifier(
                    identifier="09.01.02/02",
                    title="",
                    text="Gebruikers met eigen of ongeauthenticeerde apparatuur (Bring Your Own Device) krijgen "
                         "alleen toegang tot een onvertrouwde zone.",
                    bbn=1,
                ),
            ],
        ),

    ],
)


CH09S02 = Section(
    identifier="09.02",
    title="Beheer van toegangsrechten van gebruikers",
    text="Doelstelling: Toegang voor bevoegde gebruikers bewerkstelligen en onbevoegde toegang tot systemen en "
         "diensten voorkomen.",
    fragments=[

        Norm(
            identifier="09.02.01",
            title="Registratie en afmelden van gebruikers",
            text="Een formele registratie- en afmeldingsprocedure behoort te worden ge&iuml;mplementeerd om toewijzing "
                 "van toegangsrechten mogelijk te maken.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.01/01",
                    title="",
                    text="Er is een sluitende formele registratie- en afmeldprocedure voor het beheren van "
                         "gebruikersidentificaties.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.02.01/02",
                    title="",
                    text="Het gebruiken van groepsaccounts is niet toegestaan tenzij dit wordt gemotiveerd en "
                         "vastgelegd door de proceseigenaar.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="09.02.02",
            title="Gebruikers toegang verlenen",
            text="Een formele gebruikerstoegangsverleningsprocedure behoort te worden ge&iuml;mplementeerd om "
                 "toegangsrechten voor alle typen gebruikers en voor alle systemen en diensten toe te wijzen of "
                 "in te trekken.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.02/01",
                    title="",
                    text="Er is uitsluitend toegang verleend tot informatiesystemen na autorisatie door een "
                         "bevoegde functionaris.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.02.02/02",
                    title="",
                    text="Op basis van een risicoafweging is bepaald waar en op welke wijze functiescheiding wordt "
                         "toegepast en welke toegangsrechten worden gegeven.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.02.02/03",
                    title="",
                    text="Er is een actueel mandaatregister waaruit blijkt welke personen bevoegdheden hebben voor "
                         "het verlenen van toegangsrechten dan wel functieprofielen.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.02.03",
            title="Beheren van speciale toegangsrechten",
            text="Het toewijzen en gebruik van speciale toegangsrechten behoren te worden beperkt en beheerst.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.03/01",
                    title="",
                    text="De uitgegeven speciale bevoegdheden worden minimaal ieder kwartaal beoordeeld.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.02.04",
            title="Beheer van geheime authenticatie-informatie van gebruikers",
            text="Het toewijzen van geheime authenticatie-informatie behoort te worden beheerst via een formeel "
                 "beheersproces.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.04/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="09.02.05",
            title="Beoordeling van toegangsrechten van gebruikers",
            text="Eigenaren van bedrijfsmiddelen behoren toegangsrechten van gebruikers regelmatig te beoordelen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.05/01",
                    title="",
                    text="Alle uitgegeven toegangsrechten worden minimaal eenmaal per jaar beoordeeld.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.02.05/02",
                    title="",
                    text="De opvolging van bevindingen is gedocumenteerd en wordt behandeld als beveiligingsincident.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.02.05/03",
                    title="",
                    text="Alle uitgegeven toegangsrechten worden minimaal eenmaal per halfjaar beoordeeld.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.02.06",
            title="Toegangsrechten intrekken of aanpassen",
            text="De toegangsrechten van alle medewerkers en externe gebruikers voor informatie en "
                 "informatieverwerkende faciliteiten behoren bij be&euml;indiging van hun dienstverband, contract of "
                 "overeenkomst te worden verwijderd, en bij wijzigingen behoren ze te worden aangepast.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.02.06/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


CH09S03 = Section(
    identifier="09.03",
    title="Verantwoordelijkheden van gebruikers",
    text="Doelstelling: Gebruikers verantwoordelijk maken voor het beschermen van hun authenticatie-informatie.",
    fragments=[

        Norm(
            identifier="09.03.01",
            title="Geheime authenticatie-informatie gebruiken",
            text="Van gebruikers behoort te worden verlangd dat zij zich bij het gebruiken van geheime "
                 "authenticatie-informatie houden aan de praktijk van de organisatie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.03.01/01",
                    title="",
                    text="Medewerkers worden ondersteund in het beheren van hun wachtwoorden door het beschikbaar "
                         "stellen van een wachtwoordenkluis.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH09S04 = Section(
    identifier="09.04",
    title="Toegangsbeveiliging van systeem en toepassing",
    text="Doelstelling: Onbevoegde toegang tot systemen en toepassingen voorkomen.",
    fragments=[

        Norm(
            identifier="09.04.01",
            title="Beperking toegang tot informatie",
            text="Toegang tot informatie en systeemfuncties van toepassingen behoort te worden beperkt in "
                 "overeenstemming met het beleid voor toegangsbeveiliging.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.01/01",
                    title="",
                    text="Er zijn maatregelen genomen die het fysiek en/of logisch isoleren van informatie met "
                         "specifiek belang waarborgen.",
                    bbn=2,
                ),
                Verifier(
                    identifier="09.04.01/02",
                    title="",
                    text="Gebruikers kunnen alleen die informatie met specifiek belang inzien en verwerken die "
                         "ze nodig hebben voor de uitoefening van hun taak.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.04.02",
            title="Beveiligde inlogprocedures",
            text="Indien het beleid voor toegangsbeveiliging dit vereist, behoort toegang tot systemen en "
                 "toepassingen te worden beheerst door een beveiligde inlogprocedure.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.02/01",
                    title="",
                    text="Als vanuit een onvertrouwde zone toegang wordt verleend naar een vertrouwde zone, gebeurt "
                         "dit alleen op basis van minimaal two-factor authenticatie.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.04.02/02",
                    title="",
                    text="Voor het verlenen van toegang tot het netwerk door externe leveranciers wordt vooraf een "
                         "risicoafweging gemaakt. De risicoafweging bepaalt onder welke voorwaarden de leveranciers "
                         "toegang krijgen. Uit een registratie blijkt hoe de rechten zijn toegekend.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.04.03",
            title="Systeem voor wachtwoordbeheer",
            text="Systemen voor wachtwoordbeheer behoren interactief te zijn en sterke wachtwoorden te waarborgen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.03/01",
                    title="",
                    text="Als er geen gebruik wordt gemaakt van two-factor authenticatie is de wachtwoordlengte "
                         "minimaal 8 posities en complex van samenstelling. Vanaf een wachtwoordlengte van "
                         "20 posities vervalt de complexiteitseis. Het aantal inlogpogingen is maximaal 10. "
                         "De tijdsduur dat een account wordt geblokkeerd na overschrijding van het aantal keer "
                         "foutief inloggen is vastgelegd.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.04.03/02",
                    title="",
                    text="In situaties waar geen two-factor authenticatie mogelijk is, wordt minimaal halfjaarlijks "
                         "het wachtwoord vernieuwd (zie ook 09.04.02/01).",
                    bbn=2,
                ),
                Verifier(
                    identifier="09.04.03/03",
                    title="",
                    text="Het wachtwoordbeleid wordt geautomatiseerd afgedwongen.",
                    bbn=2,
                ),
                Verifier(
                    identifier="09.04.03/04",
                    title="",
                    text="Initi&euml;le wachtwoorden en wachtwoorden die gereset zijn, hebben een maximale geldigheidsduur "
                         "van een werkdag en moeten bij het eerste gebruik worden gewijzigd.",
                    bbn=2,
                ),
                Verifier(
                    identifier="09.04.03/05",
                    title="",
                    text="Wachtwoorden die voldoen aan het wachtwoordbeleid hebben een maximale geldigheidsduur "
                         "van een jaar. Daar waar het beleid niet toepasbaar is, geldt een maximale geldigheidsduur "
                         "van 6 maanden.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.04.04",
            title="Speciale systeemhulpmiddelen gebruiken",
            text="Het gebruik van systeemhulpmiddelen die in staat zijn om beheersmaatregelen voor systemen en "
                 "toepassingen te omzeilen behoort te worden beperkt en nauwkeurig te worden gecontroleerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.04/01",
                    title="",
                    text="Alleen bevoegd personeel heeft toegang tot systeemhulpmiddelen.",
                    bbn=1,
                ),
                Verifier(
                    identifier="09.04.04/02",
                    title="",
                    text="Het gebruik van systeemhulpmiddelen wordt gelogd. "
                         "De logging is een halfjaar beschikbaar voor onderzoek.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="09.04.05",
            title="Toegangsbeveiliging op programmabroncode",
            text="Toegang tot de programmabroncode behoort te worden beperkt.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="09.04.05/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


CH09 = Chapter(
    identifier="09",
    title="Toegangsbeveiliging",
    fragments=[
        CH09S01,
        CH09S02,
        CH09S03,
        CH09S04,
    ]
)
