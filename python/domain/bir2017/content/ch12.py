# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S1201 = Section(
    identifier="12.01",
    title="Bedieningsprocedures en verantwoordelijkheden",
    text="Doelstelling: Correcte en veilige bediening van informatie-verwerkende faciliteiten waarborgen.",
    fragments=[

        Norm(
            identifier="12.01.01",
            title="Gedocumenteerde bedieningsprocedures",
            text="Bedieningsprocedures behoren te worden gedocumenteerd en beschikbaar te worden gesteld aan alle "
                 "gebruikers die ze nodig hebben.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.01.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="12.01.02",
            title="Wijzigingsbeheer",
            text="Veranderingen in de organisatie, bedrijfsprocessen, informatieverwerkende faciliteiten en systemen "
                 "die van invloed zijn op de informatiebeveiliging behoren te worden beheerst.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.01.02/01",
                    title="",
                    text="In de procedure voor wijzigingenbeheer is minimaal aandacht besteed aan: "
                         "(a) het administreren van wijzigingen; "
                         "(b) risicoafweging van mogelijke gevolgen van de wijzigingen; "
                         "(c) goedkeuringsprocedure voor wijzigingen.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="12.01.03",
            title="Capaciteitsbeheer",
            text="Het gebruik van middelen behoort te worden gemonitord en afgestemd, en er behoren verwachtingen te "
                 "worden opgesteld voor toekomstige capaciteitseisen om de vereiste systeemprestaties te waarborgen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.01.03/01",
                    title="",
                    text="In koppelpunten met externe of onvertrouwde zones zijn maatregelen getroffen om mogelijke "
                         "aanvallen die de beschikbaarheid van de informatievoorziening negatief beïnvloeden "
                         "(bijv. DDoS attacks, Distributed Denial of Service) te signaleren en hierop te reageren.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="12.01.04",
            title="Scheiding van ontwikkel-, test- en productieomgevingen",
            text="Ontwikkel-, test- en productieomgevingen behoren te worden gescheiden om het risico van onbevoegde "
                 "toegang tot of veranderingen aan de productieomgeving te verlagen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.01.04/01",
                    title="",
                    text="In de productieomgeving wordt niet getest. Alleen met voorafgaande goedkeuring door de "
                         "proceseigenaar en schriftelijke vastlegging hiervan, kan hierop worden afgeweken.",
                    bbn=2,
                ),
                Verifier(
                    identifier="12.01.04/02",
                    title="",
                    text="Wijzigingen op de productieomgeving worden altijd getest voordat zij in productie "
                         "gebracht worden. Alleen met voorafgaande goedkeuring door de proceseigenaar en "
                         "schriftelijke vastlegging hiervan, kan hierop worden afgeweken.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S1202 = Section(
    identifier="12.02",
    title="Bescherming tegen malware",
    text="Doelstelling: Waarborgen dat informatie en informatieverwerkende faciliteiten beschermd zijn tegen malware.",
    fragments=[

        Norm(
            identifier="12.02.01",
            title="Beheersmaatregelen tegen malware",
            text="Ter bescherming tegen malware behoren beheersmaatregelen voor detectie, preventie en herstel te "
                 "worden geïmplementeerd, in combinatie met een passend bewustzijn van gebruikers.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.02.01/01",
                    title="",
                    text="Het downloaden van bestanden is beheerst en beperkt op basis van risico en need-of-use.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.02.01/02",
                    title="",
                    text="Gebruikers zijn voorgelicht over de risico?s ten aanzien van surfgedrag en het klikken op "
                         "onbekende linken.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.02.01/03",
                    title="",
                    text="Software en bijbehorende herstelsoftware die malware opspoort  zijn geïnstalleerd en "
                         "worden regelmatig geüpdate.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.02.01/04",
                    title="",
                    text="Computers en media worden als voorzorgsmaatregel routinematig gescand. "
                         "De uitgevoerde scan behoort te omvatten: "
                         "(a) alle bestanden die via netwerken of via elke vorm van opslagmedium zijn ontvangen, "
                         "vóór gebruik op malware scannen; "
                         "(b) bijlagen en downloads vóór gebruik.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.02.01/05",
                    title="",
                    text="De malware scan wordt op verschillende omgevingen uitgevoerd, bijv. op mailservers, "
                         "desktopcomputers en bij de toegang tot het netwerk van de organisatie.",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1203 = Section(
    identifier="12.03",
    title="Back-up",
    text="Doelstelling: Beschermen tegen het verlies van gegevens.",
    fragments=[

        Norm(
            identifier="12.03.01",
            title="Back-up van informatie",
            text="Regelmatig behoren back-upkopieën van informatie, software en systeemafbeeldingen te worden gemaakt "
                 "en getest in overeenstemming met een overeengekomen back-upbeleid.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.03.01/01",
                    title="",
                    text="Er is een back-up beleid waarin de eisen voor het bewaren en beschermen zijn gedefinieerd "
                         "en vastgesteld.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.03.01/02",
                    title="",
                    text="Op basis van een expliciete risicoafweging is bepaald wat het maximaal toegestane "
                         "dataverlies is en wat de maximale hersteltijd is na een incident.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.03.01/03",
                    title="",
                    text="In het back-up beleid staan minimaal de volgende eisen: "
                         "(a) dataverlies bedraagt maximaal 28 uur; "
                         "(b) hersteltijd in geval van incidenten is maximaal 16 werkuren "
                         "(2 dagen van 8 uur) in 85% van de gevallen.",
                    bbn=2,
                ),
                Verifier(
                    identifier="12.03.01/04",
                    title="",
                    text="Het back-up proces voorziet in opslag van de back-up op een locatie, waarbij een incident "
                         "op de ene locatie niet kan leiden tot schade op de andere.",
                    bbn=2,
                ),
                Verifier(
                    identifier="12.03.01/05",
                    title="",
                    text="De restore procedure wordt minimaal jaarlijks getest of na een grote wijziging om de "
                         "betrouwbaarheid te waarborgen als ze in noodgevallen uitgevoerd moet worden.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S1204 = Section(
    identifier="12.04",
    title="Verslaglegging en monitoren",
    text="Doelstelling: Gebeurtenissen vastleggen en bewijs verzamelen.",
    fragments=[

        Norm(
            identifier="12.04.01",
            title="Gebeurtenissen registreren",
            text="Logbestanden van gebeurtenissen die gebruikersactiviteiten, uitzonderingen en "
                 "informatiebeveiligingsgebeurtenissen registreren, behoren te worden gemaakt, bewaard en regelmatig "
                 "te worden beoordeeld.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.04.01/01",
                    title="",
                    text="Een logregel bevat minimaal de gebeurtenis; de benodigde informatie die nodig is om het "
                         "incident met hoge mate van zekerheid te herleiden tot een natuurlijk persoon; "
                         "het gebruikte apparaat; "
                         "het resultaat van de handeling; "
                         "een datum en tijdstip van de gebeurtenis.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.04.01/02",
                    title="",
                    text="Een logregel bevat in geen geval gegevens die tot het doorbreken van de beveiliging "
                         "kunnen leiden.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.04.01/03",
                    title="",
                    text="De informatieverwerkende omgeving wordt gemonitord door een SIEM  en/of SOC middels "
                         "detectie-voorzieningen, zoals het Nationaal Detectie Netwerk, die worden ingezet op "
                         "basis van een risico-inschatting, mede aan de hand van  en de aard van de te beschermen "
                         "gegevens en informatiesystemen, zodat aanvallen kunnen worden gedetecteerd.",
                    bbn=2,
                ),
                Verifier(
                    identifier="12.04.01/04",
                    title="",
                    text="Bij ontdekte nieuwe dreigingen (aanvallen) via 12.04.01/03 worden deze binnen geldende "
                         "juridische kaders gedeeld binnen de overheid, waaronder met het NCSC, "
                         "middels (geautomatiseerde) threat intelligence sharing mechanismen.",
                    bbn=2,
                ),
                Verifier(
                    identifier="12.04.01/05",
                    title="",
                    text="De SIEM en/of SOC hebben heldere regels over wanneer een incident moet worden "
                         "gerapporteerd aan het verantwoordelijk management.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="12.04.02",
            title="Beschermen van informatie in logbestanden",
            text="Logfaciliteiten en informatie in logbestanden behoren te worden beschermd tegen vervalsing en "
                 "onbevoegde toegang.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.04.02/01",
                    title="",
                    text="Er is een overzicht van logbestanden die worden gegenereerd.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.04.02/02",
                    title="",
                    text="Ten behoeve van de loganalyse is op basis van een expliciete risicoafweging de "
                         "bewaarperiode van de logging bepaald. Binnen deze periode is de beschikbaarheid "
                         "van de loginformatie gewaarborgd.",
                    bbn=1,
                ),
                Verifier(
                    identifier="12.04.02/03",
                    title="",
                    text="Er is een (onafhankelijke)  interne audit procedure die minimaal half jaarlijks toetst "
                         "op het ongewijzigd bestaan van logbestanden.",
                    bbn=2,
                ),
                Verifier(
                    identifier="12.04.02/04",
                    title="",
                    text="Oneigenlijk wijzigen, verwijderen of pogingen daartoe van loggegevens worden "
                         "zo snel mogelijk gemeld als beveiligingsincident via de procedure voor "
                         "informatiebeveiligingsincidenten conform hoofdstuk 16.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="12.04.03",
            title="Logbestanden van beheerders en operators",
            text="Activiteiten van systeembeheerders en -operators behoren te worden vastgelegd en de logbestanden "
                 "behoren te worden beschermd en regelmatig te worden beoordeeld.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.04.03/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="12.04.04",
            title="Kloksynchronisatie",
            text="De klokken van alle relevante informatieverwerkende systemen binnen een organisatie of "
                 "beveiligingsdomein behoren te worden gesynchroniseerd met één referentietijdbron.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.04.04/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1205 = Section(
    identifier="12.05",
    title="Beheersing van operationele sofware",
    text="Doelstelling: De integriteit van operationele systemen waarborgen.",
    fragments=[

        Norm(
            identifier="12.05.01",
            title="Software installeren op operationele systemen",
            text="Om het op operationele systemen installeren van software te beheersen behoren procedures te worden "
                 "geïmplementeerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.05.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1206 = Section(
    identifier="12.06",
    title="Beheer van technische kwetsbaarheden",
    text="Doelstelling: Benutting van technische kwetsbaarheden voorkomen.",
    fragments=[

        Norm(
            identifier="12.06.01",
            title="Beheer van technische kwetsbaarheden",
            text="Informatie over technische kwetsbaarheden van informatiesystemen die worden gebruikt behoort tijdig "
                 "te worden verkregen, de blootstelling van de organisatie aan dergelijke kwetsbaarheden te worden "
                 "geëvalueerd en passende maatregelen te worden genomen om het risico dat ermee samenhangt aan te "
                 "pakken.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.06.01/01",
                    title="",
                    text="Als de kans op misbruik en de verwachte schade beide hoog zijn (NCSC classificatie), "
                         "worden patches zo snel mogelijk, maar uiterlijk binnen een week geïnstalleerd. "
                         "In de tussentijd worden op basis van een expliciete risicoafweging mitigerende "
                         "maatregelen getroffen.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="12.06.02",
            title="Beperkingen voor het installeren van software",
            text="Voor het door gebruikers installeren van software behoren regels te worden vastgesteld en te worden "
                 "geïmplementeerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.06.02/01",
                    title="",
                    text="Gebruikers kunnen op hun werkomgeving niets zelf installeren, anders dan via de "
                         "ICT-leverancier wordt aangeboden of wordt toegestaan (whitelist).",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S1207 = Section(
    identifier="12.07",
    title="Overwegingen betreffende audits van informatiesystemen",
    text="Doelstelling: De impact van auditactiviteiten op uitvoeringssystemen zo gering mogelijk maken",
    fragments=[

        Norm(
            identifier="12.07.01",
            title="Beheersmaatregelen betreffende audits van informatiesystemen",
            text="Auditeisen en -activiteiten die verificatie van uitvoeringssystemen met zich meebrengen, behoren "
                 "zorgvuldig te worden gepland en afgestemd om bedrijfsprocessen zo min mogelijk te verstoren.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.07.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


CH12 = Chapter(
    identifier="12",
    title="Beveiliging bedrijfsvoering",
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
