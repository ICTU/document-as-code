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


S1201 = Section(
    identifier="12.01",
    title=u"Bedieningsprocedures en verantwoordelijkheden",
    text=u"Doelstelling: Correcte en veilige bediening van informatie-verwerkende faciliteiten waarborgen.",
    fragments=[

        Norm(
            identifier="12.01.01",
            title=u"Gedocumenteerde bedieningsprocedures",
            text=u"Bedieningsprocedures behoren te worden gedocumenteerd en beschikbaar te worden gesteld aan alle "
                 u"gebruikers die ze nodig hebben.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.01.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="12.01.02",
            title=u"Wijzigingsbeheer",
            text=u"Veranderingen in de organisatie, bedrijfsprocessen, informatieverwerkende faciliteiten en systemen "
                 u"die van invloed zijn op de informatiebeveiliging behoren te worden beheerst.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.01.02/01",
                    title=u"",
                    text=u"In de procedure voor wijzigingenbeheer is minimaal aandacht besteed aan: "
                         u"(a) het administreren van wijzigingen; "
                         u"(b) risicoafweging van mogelijke gevolgen van de wijzigingen; "
                         u"(c) goedkeuringsprocedure voor wijzigingen.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="12.01.03",
            title=u"Capaciteitsbeheer",
            text=u"Het gebruik van middelen behoort te worden gemonitord en afgestemd, en er behoren verwachtingen te "
                 u"worden opgesteld voor toekomstige capaciteitseisen om de vereiste systeemprestaties te waarborgen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.01.03/01",
                    title=u"",
                    text=u"In koppelpunten met externe of onvertrouwde zones zijn maatregelen getroffen om mogelijke "
                         u"aanvallen die de beschikbaarheid van de informatievoorziening negatief beïnvloeden "
                         u"(bijv. DDoS attacks, Distributed Denial of Service) te signaleren en hierop te reageren.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="12.01.04",
            title=u"Scheiding van ontwikkel-, test- en productieomgevingen",
            text=u"Ontwikkel-, test- en productieomgevingen behoren te worden gescheiden om het risico van onbevoegde "
                 u"toegang tot of veranderingen aan de productieomgeving te verlagen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.01.04/01",
                    title=u"",
                    text=u"In de productieomgeving wordt niet getest. Alleen met voorafgaande goedkeuring door de "
                         u"proceseigenaar en schriftelijke vastlegging hiervan, kan hierop worden afgeweken.",
                    bbn=2,
                ),
                Verifier(
                    identifier="12.01.04/02",
                    title=u"",
                    text=u"Wijzigingen op de productieomgeving worden altijd getest voordat zij in productie "
                         u"gebracht worden. Alleen met voorafgaande goedkeuring door de proceseigenaar en "
                         u"schriftelijke vastlegging hiervan, kan hierop worden afgeweken.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S1202 = Section(
    identifier="12.02",
    title=u"Bescherming tegen malware",
    text=u"Doelstelling: Waarborgen dat informatie en informatieverwerkende faciliteiten beschermd zijn tegen malware.",
    fragments=[

        Norm(
            identifier="12.02.01",
            title=u"Beheersmaatregelen tegen malware",
            text=u"Ter bescherming tegen malware behoren beheersmaatregelen voor detectie, preventie en herstel te "
                 u"worden geïmplementeerd, in combinatie met een passend bewustzijn van gebruikers.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.02.01/01",
                    title=u"",
                    text=u"Het downloaden van bestanden is beheerst en beperkt op basis van risico en need-of-use.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.02.01/02",
                    title=u"",
                    text=u"Gebruikers zijn voorgelicht over de risico?s ten aanzien van surfgedrag en het klikken op "
                         u"onbekende linken.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.02.01/03",
                    title=u"",
                    text=u"Software en bijbehorende herstelsoftware die malware opspoort  zijn geïnstalleerd en "
                         u"worden regelmatig geüpdate.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.02.01/04",
                    title=u"",
                    text=u"Computers en media worden als voorzorgsmaatregel routinematig gescand. "
                         u"De uitgevoerde scan behoort te omvatten: "
                         u"(a) alle bestanden die via netwerken of via elke vorm van opslagmedium zijn ontvangen, "
                         u"vóór gebruik op malware scannen; "
                         u"(b) bijlagen en downloads vóór gebruik.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.02.01/05",
                    title=u"",
                    text=u"De malware scan wordt op verschillende omgevingen uitgevoerd, bijv. op mailservers, "
                         u"desktopcomputers en bij de toegang tot het netwerk van de organisatie.",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1203 = Section(
    identifier="12.03",
    title=u"Back-up",
    text=u"Doelstelling: Beschermen tegen het verlies van gegevens.",
    fragments=[

        Norm(
            identifier="12.03.01",
            title=u"Back-up van informatie",
            text=u"Regelmatig behoren back-upkopieën van informatie, software en systeemafbeeldingen te worden gemaakt "
                 u"en getest in overeenstemming met een overeengekomen back-upbeleid.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.03.01/01",
                    title=u"",
                    text=u"Er is een back-up beleid waarin de eisen voor het bewaren en beschermen zijn gedefinieerd "
                         u"en vastgesteld.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.03.01/02",
                    title=u"",
                    text=u"Op basis van een expliciete risicoafweging is bepaald wat het maximaal toegestane "
                         u"dataverlies is en wat de maximale hersteltijd is na een incident.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.03.01/03",
                    title=u"",
                    text=u"In het back-up beleid staan minimaal de volgende eisen: "
                         u"(a) dataverlies bedraagt maximaal 28 uur; "
                         u"(b) hersteltijd in geval van incidenten is maximaal 16 werkuren "
                         u"(2 dagen van 8 uur) in 85% van de gevallen.",
                    bbn=2,
                ),
                Verifier(
                    identifier="12.03.01/04",
                    title=u"",
                    text=u"Het back-up proces voorziet in opslag van de back-up op een locatie, waarbij een incident "
                         u"op de ene locatie niet kan leiden tot schade op de andere.",
                    bbn=2,
                ),
                Verifier(
                    identifier="12.03.01/05",
                    title=u"",
                    text=u"De restore procedure wordt minimaal jaarlijks getest of na een grote wijziging om de "
                         u"betrouwbaarheid te waarborgen als ze in noodgevallen uitgevoerd moet worden.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S1204 = Section(
    identifier="12.04",
    title=u"Verslaglegging en monitoren",
    text=u"Doelstelling: Gebeurtenissen vastleggen en bewijs verzamelen.",
    fragments=[

        Norm(
            identifier="12.04.01",
            title=u"Gebeurtenissen registreren",
            text=u"Logbestanden van gebeurtenissen die gebruikersactiviteiten, uitzonderingen en "
                 u"informatiebeveiligingsgebeurtenissen registreren, behoren te worden gemaakt, bewaard en regelmatig "
                 u"te worden beoordeeld.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.04.01/01",
                    title=u"",
                    text=u"Een logregel bevat minimaal de gebeurtenis; de benodigde informatie die nodig is om het "
                         u"incident met hoge mate van zekerheid te herleiden tot een natuurlijk persoon; "
                         u"het gebruikte apparaat; "
                         u"het resultaat van de handeling; "
                         u"een datum en tijdstip van de gebeurtenis.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.04.01/02",
                    title=u"",
                    text=u"Een logregel bevat in geen geval gegevens die tot het doorbreken van de beveiliging "
                         u"kunnen leiden.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.04.01/03",
                    title=u"",
                    text=u"De informatieverwerkende omgeving wordt gemonitord door een SIEM  en/of SOC middels "
                         u"detectie-voorzieningen, zoals het Nationaal Detectie Netwerk, die worden ingezet op "
                         u"basis van een risico-inschatting, mede aan de hand van  en de aard van de te beschermen "
                         u"gegevens en informatiesystemen, zodat aanvallen kunnen worden gedetecteerd.",
                    bbn=2,
                ),
                Verifier(
                    identifier="12.04.01/04",
                    title=u"",
                    text=u"Bij ontdekte nieuwe dreigingen (aanvallen) via 12.04.01/03 worden deze binnen geldende "
                         u"juridische kaders gedeeld binnen de overheid, waaronder met het NCSC, "
                         u"middels (geautomatiseerde) threat intelligence sharing mechanismen.",
                    bbn=2,
                ),
                Verifier(
                    identifier="12.04.01/05",
                    title=u"",
                    text=u"De SIEM en/of SOC hebben heldere regels over wanneer een incident moet worden "
                         u"gerapporteerd aan het verantwoordelijk management.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="12.04.02",
            title=u"Beschermen van informatie in logbestanden",
            text=u"Logfaciliteiten en informatie in logbestanden behoren te worden beschermd tegen vervalsing en "
                 u"onbevoegde toegang.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.04.02/01",
                    title=u"",
                    text=u"Er is een overzicht van logbestanden die worden gegenereerd.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.04.02/02",
                    title=u"",
                    text=u"Ten behoeve van de loganalyse is op basis van een expliciete risicoafweging de "
                         u"bewaarperiode van de logging bepaald. Binnen deze periode is de beschikbaarheid "
                         u"van de loginformatie gewaarborgd.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.04.02/03",
                    title=u"",
                    text=u"Er is een (onafhankelijke)  interne audit procedure die minimaal half jaarlijks toetst "
                         u"op het ongewijzigd bestaan van logbestanden.",
                    bbn=2,
                ),
                Verifier(
                    identifier="12.04.02/04",
                    title=u"",
                    text=u"Oneigenlijk wijzigen, verwijderen of pogingen daartoe van loggegevens worden "
                         u"zo snel mogelijk gemeld als beveiligingsincident via de procedure voor "
                         u"informatiebeveiligingsincidenten conform hoofdstuk 16.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="12.04.03",
            title=u"Logbestanden van beheerders en operators",
            text=u"Activiteiten van systeembeheerders en -operators behoren te worden vastgelegd en de logbestanden "
                 u"behoren te worden beschermd en regelmatig te worden beoordeeld.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.04.03/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="12.04.04",
            title=u"Kloksynchronisatie",
            text=u"De klokken van alle relevante informatieverwerkende systemen binnen een organisatie of "
                 u"beveiligingsdomein behoren te worden gesynchroniseerd met één referentietijdbron.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.04.04/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1205 = Section(
    identifier="12.05",
    title=u"Beheersing van operationele sofware",
    text=u"Doelstelling: De integriteit van operationele systemen waarborgen.",
    fragments=[

        Norm(
            identifier="12.05.01",
            title=u"Software installeren op operationele systemen",
            text=u"Om het op operationele systemen installeren van software te beheersen behoren procedures te worden "
                 u"geïmplementeerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.05.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1206 = Section(
    identifier="12.06",
    title=u"Beheer van technische kwetsbaarheden",
    text=u"Doelstelling: Benutting van technische kwetsbaarheden voorkomen.",
    fragments=[

        Norm(
            identifier="12.06.01",
            title=u"Beheer van technische kwetsbaarheden",
            text=u"Informatie over technische kwetsbaarheden van informatiesystemen die worden gebruikt behoort tijdig "
                 u"te worden verkregen, de blootstelling van de organisatie aan dergelijke kwetsbaarheden te worden "
                 u"geëvalueerd en passende maatregelen te worden genomen om het risico dat ermee samenhangt aan te "
                 u"pakken.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.06.01/01",
                    title=u"",
                    text=u"Als de kans op misbruik en de verwachte schade beide hoog zijn (NCSC classificatie), "
                         u"worden patches zo snel mogelijk, maar uiterlijk binnen een week geïnstalleerd. "
                         u"In de tussentijd worden op basis van een expliciete risicoafweging mitigerende "
                         u"maatregelen getroffen.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="12.06.02",
            title=u"Beperkingen voor het installeren van software",
            text=u"Voor het door gebruikers installeren van software behoren regels te worden vastgesteld en te worden "
                 u"geïmplementeerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.06.02/01",
                    title=u"",
                    text=u"Gebruikers kunnen op hun werkomgeving niets zelf installeren, anders dan via de "
                         u"ICT-leverancier wordt aangeboden of wordt toegestaan (whitelist).",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S1207 = Section(
    identifier="12.07",
    title=u"Overwegingen betreffende audits van informatiesystemen",
    text=u"Doelstelling: De impact van auditactiviteiten op uitvoeringssystemen zo gering mogelijk maken",
    fragments=[

        Norm(
            identifier="12.07.01",
            title=u"Beheersmaatregelen betreffende audits van informatiesystemen",
            text=u"Auditeisen en -activiteiten die verificatie van uitvoeringssystemen met zich meebrengen, behoren "
                 u"zorgvuldig te worden gepland en afgestemd om bedrijfsprocessen zo min mogelijk te verstoren.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.07.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


CH12 = Chapter(
    identifier="12",
    title=u"Beveiliging bedrijfsvoering",
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
