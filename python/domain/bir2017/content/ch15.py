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
    title=u"Informatiebeveiliging in leveranciersrelaties",
    text=u"Doelstelling: De bescherming waarborgen van bedrijfsmiddelen van de organisatie die toegankelijk zijn voor "
         u"leveranciers.",
    fragments=[

        Norm(
            identifier="15.01.01",
            title=u"Informatiebeveiligingsbeleid voor leveranciersrelaties",
            text=u"Met de leverancier behoren de informatiebeveiligingseisen om risico's te verlagen die verband "
                 u"houden met de toegang van de leverancier tot de bedrijfsmiddelen van de organisatie, te worden "
                 u"overeengekomen en gedocumenteerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="15.01.01/01",
                    title=u"",
                    text=u"Bij offerteaanvragen waar informatie(voorziening) een rol speelt, worden eisen t.a.v. "
                         u"informatiebeveiliging (beschikbaarheid, integriteit en vertrouwelijkheid) benoemd. "
                         u"Deze eisen zijn gebaseerd op een expliciete risicoafweging.",
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.01/02",
                    title=u"",
                    text=u"Op basis van een expliciete risicoafweging worden de beheersmaatregelen met betrekking "
                         u"tot leverancierstoegang tot bedrijfsinformatie vastgesteld en er wordt voldaan aan het "
                         u"gestelde in het VIR-BI.",
                    bbn=2,
                ),
                Verifier(
                    identifier="15.01.01/03",
                    title=u"",
                    text=u"Met alle leveranciers die als bewerker voor of namens de organisatie persoonsgegevens "
                         u"verwerken, worden verwerkersovereenkomsten gesloten waarin alle wettelijk vereiste "
                         u"afspraken zijn vastgesteld.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="15.01.02",
            title=u"Opnemen van beveiligingsaspecten in leveranciersovereenkomsten",
            text=u"Alle relevante informatiebeveiligingseisen behoren te worden vastgesteld en overeengekomen met elke "
                 u"leverancier die toegang heeft tot IT-infrastructuurelementen ten behoeve van de informatie van de "
                 u"organisatie, of deze verwerkt, opslaat, communiceert of biedt.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="15.01.02/01",
                    title=u"",
                    text=u"De beveiligingseisen uit de offerteaanvraag worden expliciet opgenomen in de "
                         u"(inkoop)contracten waar informatie een rol speelt.",
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.02/02",
                    title=u"",
                    text=u"In de inkoopcontracten worden expliciet prestatie-indicatoren en de bijbehorende "
                         u"verantwoordingsrapportages opgenomen.",
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.02/03",
                    title=u"",
                    text=u"In situaties waarin contractvoorwaarden worden opgelegd door leveranciers, is voorafgaand "
                         u"aan het tekenen van het contract met een risicoafweging helder gemaakt wat de consequenties "
                         u"hiervan zijn voor de organisatie. Expliciet is gemaakt welke consequenties geaccepteerd "
                         u"worden en welke gemitigeerd moeten zijn bij het aangaan van de overeenkomst.",
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.02/04",
                    title=u"",
                    text=u"Ter waarborging van vertrouwelijkheid of geheimhouding worden bij IT-inkopen de algemene "
                         u"rijksvoorwaarden voor inkoop (ARBIT) gehanteerd.",
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.02/05",
                    title=u"",
                    text=u"Voordat een contract wordt afgesloten wordt in een risicoafweging bepaald of de "
                         u"afhankelijkheid van een leverancier beheersbaar is. Een vast onderdeel van het contract "
                         u"is een expliciete uitwerking van de exit-strategie.",
                    bbn=2,
                ),
                Verifier(
                    identifier="15.01.02/06",
                    title=u"",
                    text=u"In inkoopcontracten wordt expliciet de mogelijkheid van een externe audit opgenomen "
                         u"waarmee de betrouwbaarheid van de geleverde dienst kan worden getoetst. Een audit is "
                         u"niet nodig als de contractant d.m.v. certificering aantoont dat de gewenste betrouwbaarheid "
                         u"van de dienst is geborgd.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="15.01.03",
            title=u"Toeleveringsketen van informatie- en communicatietechnologie",
            text=u"Overeenkomsten met leveranciers behoren eisen te bevatten die betrekking hebben op de "
                 u"informatiebeveiligingsrisico's in verband met de toeleveringsketen van de diensten en producten op "
                 u"het gebied van informatie- en communicatietechnologie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="15.01.03/01",
                    title=u"",
                    text=u"Leveranciers moeten hun keten van toeleveranciers bekend maken en transparant zijn over "
                         u"de maatregelen die zij genomen hebben om de aan hun opgelegde eisen ook door te vertalen "
                         u"naar hun toeleveranciers.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S1502 = Section(
    identifier="15.02",
    title=u"Toepassingen op openbare netwerken beveiligen",
    text=u"Doelstelling: Een overeengekomen viveau van informatiebeveiliging en dienstverlening in overeenstemming met "
         u"de leveranciers-overeenkomsten handhaven.",
    fragments=[

        Norm(
            identifier="15.02.01",
            title=u"Monitoring en beoordeling van dienstverlening van leveranciers",
            text=u"Organisaties behoren regelmatig de dienstverlening van leveranciers te monitoren, te beoordelen en "
                 u"te auditen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="15.02.01/01",
                    title=u"",
                    text=u"Jaarlijks wordt de prestatie van leveranciers op het gebied van informatiebeveiliging "
                         u"beoordeeld op vooraf vastgestelde prestatie-indicatoren, zoals in het contract opgenomen "
                         u"is.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="15.02.02",
            title=u"Beheer van veranderingen in dienstverlening van leveranciers",
            text=u"Veranderingen in de dienstverlening van leveranciers, met inbegrip van handhaving en verbetering "
                 u"van bestaande beleidslijnen, procedures en beheersmaatregelen voor informatiebeveiliging, behoren "
                 u"te worden, beheerd, rekening houdend met de kritikaliteit van bedrijfsinformatie, betrokken "
                 u"systemen en processen en herbeoordeling van risico's.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="15.02.02/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH15 = Chapter(
    identifier="15",
    title=u"Leveranciersrelaties",
    fragments=[
        S1501,
        S1502,
    ]
)

