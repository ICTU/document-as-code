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

S1201 = Section(
    identifier="12.01",
    title=u"",
    fragments=[

        Norm(
            identifier="12.01.01",
            title=u"",
            text=u"Gedocumenteerde bedieningsprocedures: Bedieningsprocedures behoren te worden gedocumenteerd en "
                 u"beschikbaar te worden gesteld aan alle gebruikers die ze nodig hebben.",
            fragments=[
            ],
        ),

        Norm(
            identifier="12.01.02",
            title=u"",
            text=u"Wijzigingsbeheer: Veranderingen in de organisatie, bedrijfsprocessen, informatieverwerkende "
                 u"faciliteiten en systemen die van invloed zijn op de informatiebeveiliging behoren te worden beheerst.",
            fragments=[
                Verifier(
                    identifier="12.01.02/01",
                    title=u"",
                    text=u"In de procedure voor wijzigingenbeheer is minimaal aandacht besteed aan: "
                         u"(a) het administreren van wijzigingen; "
                         u"(b) risicoafweging van mogelijke gevolgen van de wijzigingen; "
                         u"(c) goedkeuringsprocedure voor wijzigingen.",
                ),
            ],
        ),

        Norm(
            identifier="12.01.03",
            title=u"",
            text=u"Capaciteitsbeheer: Het gebruik van middelen behoort te worden gemonitord en afgestemd, en er "
                 u"behoren verwachtingen te worden opgesteld voor toekomstige capaciteitseisen om de vereiste "
                 u"systeemprestaties te waarborgen.",
            fragments=[
                Verifier(
                    identifier="12.01.03/01",
                    title=u"",
                    text=u"In koppelpunten met externe of onvertrouwde zones zijn maatregelen getroffen om mogelijke "
                         u"aanvallen die de beschikbaarheid van de informatievoorziening negatief beïnvloeden "
                         u"(bijv. DDoS attacks, Distributed Denial of Service) te signaleren en hierop te reageren.",
                ),
            ],
        ),

        Norm(
            identifier="12.01.04",
            title=u"",
            text=u"Scheiding van ontwikkel-, test- en productieomgevingen: Ontwikkel-, test- en productieomgevingen "
                 u"behoren te worden gescheiden om het risico van onbevoegde toegang tot of veranderingen aan de "
                 u"productieomgeving te verlagen.",
            fragments=[
                Verifier(
                    identifier="12.01.04/01",
                    title=u"",
                    text=u"In de productieomgeving wordt niet getest. Alleen met voorafgaande goedkeuring door de "
                         u"proceseigenaar en schriftelijke vastlegging hiervan, kan hierop worden afgeweken.",
                ),
                Verifier(
                    identifier="12.01.04/02",
                    title=u"",
                    text=u"Wijzigingen op de productieomgeving worden altijd getest voordat zij in productie "
                         u"gebracht worden. Alleen met voorafgaande goedkeuring door de proceseigenaar en "
                         u"schriftelijke vastlegging hiervan, kan hierop worden afgeweken.",
                ),
            ],
        ),

    ],
)


S1202 = Section(
    identifier="12.02",
    title=u"",
    fragments=[

        Norm(
            identifier="12.02.01",
            title=u"",
            text=u"Beheersmaatregelen tegen malware: Ter bescherming tegen malware behoren beheersmaatregelen voor "
                 u"detectie, preventie en herstel te worden geïmplementeerd, in combinatie met een passend bewustzijn "
                 u"van gebruikers.",
            fragments=[
                Verifier(
                    identifier="12.02.01/01",
                    title=u"",
                    text=u"Het downloaden van bestanden is beheerst en beperkt op basis van risico en need-of-use.",
                ),
                Verifier(
                    identifier="12.02.01/02",
                    title=u"",
                    text=u"Gebruikers zijn voorgelicht over de risico?s ten aanzien van surfgedrag en het klikken op "
                         u"onbekende linken.",
                ),
                Verifier(
                    identifier="12.02.01/03",
                    title=u"",
                    text=u"Software en bijbehorende herstelsoftware die malware opspoort  zijn geïnstalleerd en "
                         u"worden regelmatig geüpdate.",
                ),
                Verifier(
                    identifier="12.02.01/04",
                    title=u"",
                    text=u"Computers en media worden als voorzorgsmaatregel routinematig gescand. "
                         u"De uitgevoerde scan behoort te omvatten: "
                         u"(a) alle bestanden die via netwerken of via elke vorm van opslagmedium zijn ontvangen, "
                         u"vóór gebruik op malware scannen; "
                         u"(b) bijlagen en downloads vóór gebruik.",
                ),
                Verifier(
                    identifier="12.02.01/05",
                    title=u"",
                    text=u"De malware scan wordt op verschillende omgevingen uitgevoerd, bijv. op mailservers, "
                         u"desktopcomputers en bij de toegang tot het netwerk van de organisatie.",
                ),
            ],
        ),

    ],
)


S1203 = Section(
    identifier="12.03",
    title=u"",
    fragments=[

        Norm(
            identifier="12.03.01",
            title=u"",
            text=u"Back-up van informatie: Regelmatig behoren back-upkopieën van informatie, software en "
                 u"systeemafbeeldingen te worden gemaakt en getest in overeenstemming met een overeengekomen "
                 u"back-upbeleid.",
            fragments=[
                Verifier(
                    identifier="12.03.01/01",
                    title=u"",
                    text=u"Er is een back-up beleid waarin de eisen voor het bewaren en beschermen zijn gedefinieerd "
                         u"en vastgesteld.",
                ),
                Verifier(
                    identifier="12.03.01/02",
                    title=u"",
                    text=u"Op basis van een expliciete risicoafweging is bepaald wat het maximaal toegestane "
                         u"dataverlies is en wat de maximale hersteltijd is na een incident.",
                ),
                Verifier(
                    identifier="12.03.01/03",
                    title=u"",
                    text=u"In het back-up beleid staan minimaal de volgende eisen: "
                         u"(a) dataverlies bedraagt maximaal 28 uur; "
                         u"(b) hersteltijd in geval van incidenten is maximaal 16 werkuren "
                         u"(2 dagen van 8 uur) in 85% van de gevallen.",
                ),
                Verifier(
                    identifier="12.03.01/04",
                    title=u"",
                    text=u"Het back-up proces voorziet in opslag van de back-up op een locatie, waarbij een incident "
                         u"op de ene locatie niet kan leiden tot schade op de andere.",
                ),
                Verifier(
                    identifier="12.03.01/05",
                    title=u"",
                    text=u"De restore procedure wordt minimaal jaarlijks getest of na een grote wijziging om de "
                         u"betrouwbaarheid te waarborgen als ze in noodgevallen uitgevoerd moet worden.",
                ),
            ],
        ),

    ],
)


S1204 = Section(
    identifier="12.04",
    title=u"",
    fragments=[

        Norm(
            identifier="12.04.01",
            title=u"",
            text=u"Gebeurtenissen registreren: Logbestanden van gebeurtenissen die gebruikersactiviteiten, "
                 u"uitzonderingen en informatiebeveiligingsgebeurtenissen registreren, behoren te worden gemaakt, "
                 u"bewaard en regelmatig te worden beoordeeld.",
            fragments=[
                Verifier(
                    identifier="12.04.01/01",
                    title=u"",
                    text=u"Een logregel bevat minimaal de gebeurtenis; de benodigde informatie die nodig is om het "
                         u"incident met hoge mate van zekerheid te herleiden tot een natuurlijk persoon; "
                         u"het gebruikte apparaat; "
                         u"het resultaat van de handeling; "
                         u"een datum en tijdstip van de gebeurtenis.",
                ),
                Verifier(
                    identifier="12.04.01/02",
                    title=u"",
                    text=u"Een logregel bevat in geen geval gegevens die tot het doorbreken van de beveiliging "
                         u"kunnen leiden.",
                ),
                Verifier(
                    identifier="12.04.01/03",
                    title=u"",
                    text=u"De informatieverwerkende omgeving wordt gemonitord door een SIEM  en/of SOC middels "
                         u"detectie-voorzieningen, zoals het Nationaal Detectie Netwerk, die worden ingezet op "
                         u"basis van een risico-inschatting, mede aan de hand van  en de aard van de te beschermen "
                         u"gegevens en informatiesystemen, zodat aanvallen kunnen worden gedetecteerd.",
                ),
                Verifier(
                    identifier="12.04.01/04",
                    title=u"",
                    text=u"Bij ontdekte nieuwe dreigingen (aanvallen) via 12.04.01/03 worden deze binnen geldende "
                         u"juridische kaders gedeeld binnen de overheid, waaronder met het NCSC, "
                         u"middels (geautomatiseerde) threat intelligence sharing mechanismen.",
                ),
                Verifier(
                    identifier="12.04.01/05",
                    title=u"",
                    text=u"De SIEM en/of SOC hebben heldere regels over wanneer een incident moet worden "
                         u"gerapporteerd aan het verantwoordelijk management.",
                ),
            ],
        ),

        Norm(
            identifier="12.04.02",
            title=u"",
            text=u"Beschermen van informatie in logbestanden: Logfaciliteiten en informatie in logbestanden behoren "
                 u"te worden beschermd tegen vervalsing en onbevoegde toegang.",
            fragments=[
                Verifier(
                    identifier="12.04.02/01",
                    title=u"",
                    text=u"Er is een overzicht van logbestanden die worden gegenereerd.",
                ),
                Verifier(
                    identifier="12.04.02/02",
                    title=u"",
                    text=u"Ten behoeve van de loganalyse is op basis van een expliciete risicoafweging de "
                         u"bewaarperiode van de logging bepaald. Binnen deze periode is de beschikbaarheid "
                         u"van de loginformatie gewaarborgd.",
                ),
                Verifier(
                    identifier="12.04.02/03",
                    title=u"",
                    text=u"Er is een (onafhankelijke)  interne audit procedure die minimaal half jaarlijks toetst "
                         u"op het ongewijzigd bestaan van logbestanden.",
                ),
                Verifier(
                    identifier="12.04.02/04",
                    title=u"",
                    text=u"Oneigenlijk wijzigen, verwijderen of pogingen daartoe van loggegevens worden "
                         u"zo snel mogelijk gemeld als beveiligingsincident via de procedure voor "
                         u"informatiebeveiligingsincidenten conform hoofdstuk 16.",
                ),
            ],
        ),

        Norm(
            identifier="12.04.03",
            title=u"",
            text=u"Logbestanden van beheerders en operators: Activiteiten van systeembeheerders en -operators "
                 u"behoren te worden vastgelegd en de logbestanden behoren te worden beschermd en regelmatig "
                 u"te worden beoordeeld.",
            fragments=[
            ],
        ),

        Norm(
            identifier="12.04.04",
            title=u"",
            text=u"Kloksynchronisatie: De klokken van alle relevante informatieverwerkende systemen binnen een "
                 u"organisatie of beveiligingsdomein behoren te worden gesynchroniseerd met één referentietijdbron.",
            fragments=[
            ],
        ),

    ],
)


S1205 = Section(
    identifier="12.05",
    title=u"",
    fragments=[

        Norm(
            identifier="12.05.01",
            title=u"",
            text=u"Software installeren op operationele systemen: Om het op operationele systemen installeren van "
                 u"software te beheersen behoren procedures te worden geïmplementeerd.",
            fragments=[
            ],
        ),

    ],
)


S1206 = Section(
    identifier="12.06",
    title=u"",
    fragments=[

        Norm(
            identifier="12.06.01",
            title=u"",
            text=u"Beheer van technische kwetsbaarheden: Informatie over technische kwetsbaarheden van "
                 u"informatiesystemen die worden gebruikt behoort tijdig te worden verkregen, de blootstelling van de "
                 u"organisatie aan dergelijke kwetsbaarheden te worden geëvalueerd en passende maatregelen te worden "
                 u"genomen om het risico dat ermee samenhangt aan te pakken.",
            fragments=[
                Verifier(
                    identifier="12.06.01/01",
                    title=u"",
                    text=u"Als de kans op misbruik en de verwachte schade beide hoog zijn (NCSC classificatie), "
                         u"worden patches zo snel mogelijk, maar uiterlijk binnen een week geïnstalleerd. "
                         u"In de tussentijd worden op basis van een expliciete risicoafweging mitigerende "
                         u"maatregelen getroffen.",
                ),
            ],
        ),

        Norm(
            identifier="12.06.02",
            title=u"",
            text=u"Beperkingen voor het installeren van software: Voor het door gebruikers installeren van software "
                 u"behoren regels te worden vastgesteld en te worden geïmplementeerd.",
            fragments=[
                Verifier(
                    identifier="12.06.02/01",
                    title=u"",
                    text=u"Gebruikers kunnen op hun werkomgeving niets zelf installeren, anders dan via de "
                         u"ICT-leverancier wordt aangeboden of wordt toegestaan (whitelist).",
                ),
            ],
        ),

    ],
)


S1207 = Section(
    identifier="12.07",
    title=u"",
    fragments=[

        Norm(
            identifier="12.07.01",
            title=u"",
            text=u"Beheersmaatregelen betreffende audits van informatiesystemen: Auditeisen en -activiteiten die "
                 u"verificatie van uitvoeringssystemen met zich meebrengen, behoren zorgvuldig te worden gepland "
                 u"en afgestemd om bedrijfsprocessen zo min mogelijk te verstoren.",
            fragments=[
            ],
        ),

    ],
)


CH12 = Chapter(
    identifier="12",
    title=u"Operations security",
    fragments=[
        S1201,
        S1202,
        S1203,
        S1204,
        S1205,
        S1206,
        S1207,
    ]
)
