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


CH12S01 = Section(
    identifier="12.01",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="12.01.02",
            title=u"TITLE",
            text=u"""
Wijzigingsbeheer;
Veranderingen in de organisatie, bedrijfsprocessen, informatie verwerkende faciliteiten en systemen die van invloed zijn op de informatiebeveiliging behoren te worden beheerst.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.01.02/01",
                    title=u"",
                    text=u"""
In de procedure voor wijzigingenbeheer is minimaal aandacht besteed aan:
(a) het administreren van wijzigingen;
(b) risicoafweging van mogelijke gevolgen van de wijzigingen; 
(c) goedkeuringsprocedure voor wijzigingen.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="12.01.03",
            title=u"TITLE",
            text=u"""
Capaciteitsbeheer;
Het gebruik van middelen behoort te worden gemonitord en afgestemd, en er behoren verwachtingen te worden opgesteld voor toekomstige capaciteitseisen om de vereiste systeemprestaties te waarborgen.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.01.03/01",
                    title=u"",
                    text=u"""
In koppelpunten met externe of onvertrouwde zones zijn maatregelen getroffen om mogelijke aanvallen die de beschikbaarheid van de informatievoorziening negatief beïnvloeden (bijv. DDoS attacks, Distributed Denial of Service attacks) te signaleren en hierop te reageren. 
                    """,
                    bbn=1,
                )
            ],
        )
    ],
)


CH12S02 = Section(
    identifier="12.02",
    title=u"TITLE",
    text=u"text",
    fragments=[
        
    ],
)


CH12S03 = Section(
    identifier="12.03",
    title=u"TITLE",
    text=u"text",
    fragments=[
        
    ],
)


CH12S04 = Section(
    identifier="12.04",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="12.04.01",
            title=u"TITLE",
            text=u"""
Gebeurtenissen registreren;
Logbestanden van gebeurtenissen die gebruikersactiviteiten, uitzonderingen en informatiebeveiligingsgebeurtenissen registreren, behoren te worden gemaakt, bewaard en regelmatig te worden beoordeeld.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.04.01/01",
                    title=u"",
                    text=u"""
Een logregel bevat minimaal de gebeurtenis; de benodigde informatie die nodig is om het incident met hoge mate van zekerheid te herleiden tot een natuurlijk persoon; het gebruikte apparaat; het resultaat van de handeling; een datum en tijdstip van de gebeurtenis.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="12.04.01/02",
                    title=u"",
                    text=u"""
Een logregel bevat in geen geval gegevens die tot het doorbreken van de beveiliging kunnen leiden.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="12.04.01/03",
                    title=u"",
                    text=u"""
De informatie verwerkende omgeving wordt gemonitord door een SIEM en/ of SOC middels detectie-voorzieningen, zoals het Nationaal Detectie Netwerk (alleen voor rijksoverheidsorganisaties), die worden ingezet op basis van een risico-inschatting, mede aan de hand van en de aard van de te beschermen gegevens en informatiesystemen, zodat aanvallen kunnen worden gedetecteerd.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="12.04.01/04",
                    title=u"",
                    text=u"""
Bij ontdekte nieuwe dreigingen (aanvallen) via 12.4.1.3 worden deze binnen geldende juridische kaders verplicht gedeeld binnen de overheid, waaronder met het NCSC (alleen voor rijksoverheidsorganisaties) of via de sectorale CERT (voor andere overheidsorganisaties), middels (bij voorkeur geautomatiseerde) threat intelligence sharing mechanismen.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="12.04.01/05",
                    title=u"",
                    text=u"""
De SIEM en/of SOC hebben heldere regels over wanneer een incident moet worden gerapporteerd aan het verantwoordelijk management.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH12S06 = Section(
    identifier="12.06",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="12.06.01",
            title=u"TITLE",
            text=u"""
Beheer van technische kwetsbaarheden:
Informatie over technische kwetsbaarheden van informatiesystemen die worden gebruikt behoort tijdig te worden verkregen, de blootstelling van de organisatie aan dergelijke kwetsbaarheden te worden geëvalueerd en passende maatregelen te worden genomen om het risico dat ermee samenhangt aan te pakken.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="12.06.01/01",
                    title=u"",
                    text=u"""
Als de kans op misbruik en de verwachte schade beide hoog zijn (NCSC classificatie kwetsbaarheidswaarschuwingen), worden patches zo snel mogelijk, maar uiterlijk binnen een week geïnstalleerd. In de tussentijd worden op basis van een expliciete risicoafweging mitigerende maatregelen getroffen.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="12.06.02",
            title=u"TITLE",
            text=u"""
Beperkingen voor het installeren van software;
Voor het door gebruikers installeren van software behoren regels te worden vastgesteld en te worden geïmplementeerd.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="12.06.02/01",
                    title=u"",
                    text=u"""
Gebruikers kunnen op hun werkomgeving niets zelf installeren, anders dan via de ICT-leverancier wordt aangeboden of wordt toegestaan (whitelist).
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH12 = Chapter(
    identifier="12",
    title=u"TITLE",
    fragments=[
        CH12S01,
        CH12S02,
        CH12S03,
        CH12S04,
        CH12S06
    ]
)
