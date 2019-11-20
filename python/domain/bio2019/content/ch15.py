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


CH15S01 = Section(
    identifier="15.01",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="15.01.01",
            title=u"TITLE",
            text=u"""
Informatiebeveiligingsbeleid voor leveranciersrelaties;
Met de leverancier behoren de informatiebeveiligingseisen om risico’s te verlagen die verband houden met de toegang van de leverancier tot de bedrijfsmiddelen van de organisatie, te worden overeengekomen en gedocumenteerd.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="15.01.01/01",
                    title=u"",
                    text=u"""
Bij offerteaanvragen waar informatie(voorziening) een rol speelt, worden eisen t.a.v. informatiebeveiliging (beschikbaarheid, integriteit en vertrouwelijkheid) benoemd. Deze eisen zijn gebaseerd op een expliciete risicoafweging.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.01/02",
                    title=u"",
                    text=u"""
Op basis van een expliciete risicoafweging worden de beheersmaatregelen met betrekken tot leverancierstoegang tot bedrijfsinformatie vastgesteld.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="15.01.01/03",
                    title=u"",
                    text=u"""
Met alle leveranciers die als verwerker voor of namens de organisatie persoonsgegevens verwerken, worden verwerkersovereenkomsten gesloten waarin alle wettelijk vereiste afspraken zijn vastgesteld.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="15.01.02",
            title=u"TITLE",
            text=u"""
Opnemen van beveiligingsaspecten in leveranciersovereenkomsten;
Alle relevante informatiebeveiligingseisen behoren te worden vastgesteld en overeengekomen met elke leverancier die toegang heeft tot IT-infrastructuurelementen ten behoeve van de informatie van de organisatie, of deze verwerkt, opslaat, communiceert of biedt.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="15.01.02/01",
                    title=u"",
                    text=u"""
De beveiligingseisen uit de offerteaanvraag worden expliciet opgenomen in de (inkoop)contracten waar informatie een rol speelt.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.02/02",
                    title=u"",
                    text=u"""
In de inkoopcontracten worden expliciet prestatie-indicatoren en de bijbehorende verantwoordingsrapportages opgenomen.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.02/03",
                    title=u"",
                    text=u"""
In situaties waarin contractvoorwaarden worden opgelegd door leveranciers, is voorafgaand aan het tekenen van het contract met een risicoafweging helder gemaakt wat de consequenties hiervan zijn voor de organisatie. Expliciet is gemaakt welke consequenties geaccepteerd worden en welke gemitigeerd moeten zijn bij het aangaan van de overeenkomst.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.02/04",
                    title=u"",
                    text=u"""
Ter waarborging van vertrouwelijkheid of geheimhouding worden bij IT-inkopen standaard voorwaarden voor inkoop gehanteerd.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.02/05",
                    title=u"",
                    text=u"""
Voordat een contract wordt afgesloten wordt in een risicoafweging bepaald of de afhankelijkheid van een leverancier beheersbaar is. Een vast onderdeel van het contract is een expliciete uitwerking van de exit-strategie.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="15.01.02/06",
                    title=u"",
                    text=u"""
In inkoopcontracten wordt expliciet de mogelijkheid van een externe audit opgenomen waarmee de betrouwbaarheid van de geleverde dienst kan worden getoetst. Een audit is niet nodig als de contractant d.m.v. certificering aantoont dat de gewenste betrouwbaarheid van de dienst is geborgd.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH15S02 = Section(
    identifier="15.02",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="15.02.01",
            title=u"TITLE",
            text=u"""
Monitoring en beoordeling van dienstverlening van leveranciers;
Organisaties behoren regelmatig de dienstverlening van leveranciers te monitoren, te beoordelen en te auditen.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="15.02.01/01",
                    title=u"",
                    text=u"""
Jaarlijks wordt de prestatie van leveranciers op het gebied van informatiebeveiliging beoordeeld op vooraf vastgestelde prestatieindicatoren, zoals in het contract opgenomen is.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH15 = Chapter(
    identifier="15",
    title=u"TITLE",
    fragments=[
        CH15S01,
        CH15S02
    ]
)
