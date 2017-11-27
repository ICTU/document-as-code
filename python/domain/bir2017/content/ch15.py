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

S1501 = Section(
    identifier="15.01",
    title=u"",
    fragments=[

        Norm(
            identifier="15.01.01",
            title=u"",
            text=u"Informatiebeveiligingsbeleid voor leveranciersrelaties: Met de leverancier behoren de "
                 u"informatiebeveiligingseisen om risico?s te verlagen die verband houden met de toegang van de "
                 u"leverancier tot de bedrijfsmiddelen van de organisatie, te worden overeengekomen en gedocumenteerd.",
            fragments=[
                Verifier(
                    identifier="15.01.01/01",
                    title=u"",
                    text=u"Bij offerteaanvragen waar informatie(voorziening) een rol speelt, worden eisen t.a.v. "
                         u"informatiebeveiliging (beschikbaarheid, integriteit en vertrouwelijkheid) benoemd. "
                         u"Deze eisen zijn gebaseerd op een expliciete risicoafweging.",
                ),
                Verifier(
                    identifier="15.01.01/02",
                    title=u"",
                    text=u"Op basis van een expliciete risicoafweging worden de beheersmaatregelen met betrekking "
                         u"tot leverancierstoegang tot bedrijfsinformatie vastgesteld en er wordt voldaan aan het "
                         u"gestelde in het VIR-BI.",
                ),
                Verifier(
                    identifier="15.01.01/03",
                    title=u"",
                    text=u"Met alle leveranciers die als bewerker voor of namens de organisatie persoonsgegevens "
                         u"verwerken, worden verwerkersovereenkomsten gesloten waarin alle wettelijk vereiste "
                         u"afspraken zijn vastgesteld.",
                ),
            ],
        ),

        Norm(
            identifier="15.01.02",
            title=u"",
            text=u"Opnemen van beveiligingsaspecten in leveranciersovereenkomsten: Alle relevante "
                 u"informatiebeveiligingseisen behoren te worden vastgesteld en overeengekomen met elke leverancier "
                 u"die toegang heeft tot IT-infrastructuurelementen ten behoeve van de informatie van de organisatie, "
                 u"of deze verwerkt, opslaat, communiceert of biedt.",
            fragments=[
                Verifier(
                    identifier="15.01.02/01",
                    title=u"",
                    text=u"De beveiligingseisen uit de offerteaanvraag worden expliciet opgenomen in de "
                         u"(inkoop)contracten waar informatie een rol speelt.",
                ),
                Verifier(
                    identifier="15.01.02/02",
                    title=u"",
                    text=u"In de inkoopcontracten worden expliciet prestatie-indicatoren en de bijbehorende "
                         u"verantwoordingsrapportages opgenomen.",
                ),
                Verifier(
                    identifier="15.01.02/03",
                    title=u"",
                    text=u"In situaties waarin contractvoorwaarden worden opgelegd door leveranciers, is voorafgaand "
                         u"aan het tekenen van het contract met een risicoafweging helder gemaakt wat de consequenties "
                         u"hiervan zijn voor de organisatie. Expliciet is gemaakt welke consequenties geaccepteerd "
                         u"worden en welke gemitigeerd moeten zijn bij het aangaan van de overeenkomst.",
                ),
                Verifier(
                    identifier="15.01.02/04",
                    title=u"",
                    text=u"Ter waarborging van vertrouwelijkheid of geheimhouding worden bij IT-inkopen de algemene "
                         u"rijksvoorwaarden voor inkoop (ARBIT) gehanteerd.",
                ),
                Verifier(
                    identifier="15.01.02/05",
                    title=u"",
                    text=u"Voordat een contract wordt afgesloten wordt in een risicoafweging bepaald of de "
                         u"afhankelijkheid van een leverancier beheersbaar is. Een vast onderdeel van het contract "
                         u"is een expliciete uitwerking van de exit-strategie.",
                ),
                Verifier(
                    identifier="15.01.02/06",
                    title=u"",
                    text=u"In inkoopcontracten wordt expliciet de mogelijkheid van een externe audit opgenomen "
                         u"waarmee de betrouwbaarheid van de geleverde dienst kan worden getoetst. Een audit is "
                         u"niet nodig als de contractant d.m.v. certificering aantoont dat de gewenste betrouwbaarheid "
                         u"van de dienst is geborgd.",
                ),
            ],
        ),

        Norm(
            identifier="15.01.03",
            title=u"",
            text=u"Toeleveringsketen van informatie- en communicatietechnologie: Overeenkomsten met leveranciers "
                 u"behoren eisen te bevatten die betrekking hebben op de informatiebeveiligingsrisico?s in verband "
                 u"met de toeleveringsketen van de diensten en producten op het gebied van "
                 u"informatie- en communicatietechnologie.",
            fragments=[
                Verifier(
                    identifier="15.01.03/01",
                    title=u"",
                    text=u"Leveranciers moeten hun keten van toeleveranciers bekend maken en transparant zijn over "
                         u"de maatregelen die zij genomen hebben om de aan hun opgelegde eisen ook door te vertalen "
                         u"naar hun toeleveranciers.",
                ),
            ],
        ),

    ],
)


S1502 = Section(
    identifier="15.02",
    title=u"",
    fragments=[

        Norm(
            identifier="15.02.01",
            title=u"",
            text=u"Monitoring en beoordeling van dienstverlening van leveranciers: Organisaties behoren regelmatig de "
                 u"dienstverlening van leveranciers te monitoren, te beoordelen en te auditen.",
            fragments=[
                Verifier(
                    identifier="15.02.01/01",
                    title=u"",
                    text=u"Jaarlijks wordt de prestatie van leveranciers op het gebied van informatiebeveiliging "
                         u"beoordeeld op vooraf vastgestelde prestatie-indicatoren, zoals in het contract opgenomen "
                         u"is.",
                ),
            ],
        ),

        Norm(
            identifier="15.02.02",
            title=u"",
            text=u"Beheer van veranderingen in dienstverlening van leveranciers: Veranderingen in de dienstverlening "
                 u"van leveranciers, met inbegrip van handhaving en verbetering van bestaande beleidslijnen, "
                 u"procedures en beheersmaatregelen voor informatiebeveiliging, behoren te worden, beheerd, rekening "
                 u"houdend met de kritikaliteit van bedrijfsinformatie, betrokken systemen en processen en "
                 u"herbeoordeling van risico?s.",
            fragments=[
                Verifier(
                    identifier="15.02.02/01",
                    title=u"",
                    text=u"- conform norm -",
                ),
            ],
        ),

    ],
)


CH15 = Chapter(
    identifier="15",
    title=u"Supplier relationships",
    fragments=[
        S1501,
        S1502,
    ]
)

