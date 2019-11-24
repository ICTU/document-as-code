# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH15S01 = Section(
    identifier="15.01",
    title="Informatiebeveiliging in leveranciersrelaties",
    text="Doelstelling: De bescherming waarborgen van bedrijfsmiddelen van de organisatie die toegankelijk zijn voor "
         "leveranciers.",
    fragments=[

        Norm(
            identifier="15.01.01",
            title="Informatiebeveiligingsbeleid voor leveranciersrelaties",
            text="Met de leverancier behoren de informatiebeveiligingseisen om risico's te verlagen die verband "
                 "houden met de toegang van de leverancier tot de bedrijfsmiddelen van de organisatie, te worden "
                 "overeengekomen en gedocumenteerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="15.01.01/01",
                    title="",
                    text="Bij offerteaanvragen waar informatie(voorziening) een rol speelt, worden eisen t.a.v. "
                         "informatiebeveiliging (beschikbaarheid, integriteit en vertrouwelijkheid) benoemd. "
                         "Deze eisen zijn gebaseerd op een expliciete risicoafweging.",
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.01/02",
                    title="",
                    text="Op basis van een expliciete risicoafweging worden de beheersmaatregelen met betrekking "
                         "tot leverancierstoegang tot bedrijfsinformatie vastgesteld.",
                    bbn=2,
                ),
                Verifier(
                    identifier="15.01.01/03",
                    title="",
                    text="Met alle leveranciers die als "
                         "verwerker "
                         "voor of namens de organisatie persoonsgegevens verwerken, worden verwerkersovereenkomsten "
                         "gesloten waarin alle wettelijk vereiste afspraken zijn vastgesteld.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="15.01.02",
            title="Opnemen van beveiligingsaspecten in leveranciersovereenkomsten",
            text="Alle relevante informatiebeveiligingseisen behoren te worden vastgesteld en overeengekomen met elke "
                 "leverancier die toegang heeft tot IT-infrastructuurelementen ten behoeve van de informatie van de "
                 "organisatie, of deze verwerkt, opslaat, communiceert of biedt.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="15.01.02/01",
                    title="",
                    text="De beveiligingseisen uit de offerteaanvraag worden expliciet opgenomen in de "
                         "(inkoop)contracten waar informatie een rol speelt.",
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.02/02",
                    title="",
                    text="In de inkoopcontracten worden expliciet prestatie-indicatoren en de bijbehorende "
                         "verantwoordingsrapportages opgenomen.",
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.02/03",
                    title="",
                    text="In situaties waarin contractvoorwaarden worden opgelegd door leveranciers, is voorafgaand "
                         "aan het tekenen van het contract met een risicoafweging helder gemaakt wat de consequenties "
                         "hiervan zijn voor de organisatie. Expliciet is gemaakt welke consequenties geaccepteerd "
                         "worden en welke gemitigeerd moeten zijn bij het aangaan van de overeenkomst.",
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.02/04",
                    title="",
                    text="Ter waarborging van vertrouwelijkheid of geheimhouding worden bij IT-inkopen "
                         "standaard voorwaarden "
                         "voor inkoop "
                         "gehanteerd.",
                    bbn=1,
                ),
                Verifier(
                    identifier="15.01.02/05",
                    title="",
                    text="Voordat een contract wordt afgesloten wordt in een risicoafweging bepaald of de "
                         "afhankelijkheid van een leverancier beheersbaar is. Een vast onderdeel van het contract "
                         "is een expliciete uitwerking van de exit-strategie.",
                    bbn=2,
                ),
                Verifier(
                    identifier="15.01.02/06",
                    title="",
                    text="In inkoopcontracten wordt expliciet de mogelijkheid van een externe audit opgenomen "
                         "waarmee de betrouwbaarheid van de geleverde dienst kan worden getoetst. Een audit is "
                         "niet nodig als de contractant d.m.v. certificering aantoont dat de gewenste betrouwbaarheid "
                         "van de dienst is geborgd.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="15.01.03",
            title="Toeleveringsketen van informatie- en communicatietechnologie",
            text="Overeenkomsten met leveranciers behoren eisen te bevatten die betrekking hebben op de "
                 "informatiebeveiligingsrisico's in verband met de toeleveringsketen van de diensten en producten op "
                 "het gebied van informatie- en communicatietechnologie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="15.01.03/01",
                    title="",
                    text="Leveranciers moeten hun keten van toeleveranciers bekend maken en transparant zijn over "
                         "de maatregelen die zij genomen hebben om de aan hun opgelegde eisen ook door te vertalen "
                         "naar hun toeleveranciers.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH15S02 = Section(
    identifier="15.02",
    title="Toepassingen op openbare netwerken beveiligen",
    text="Doelstelling: Een overeengekomen viveau van informatiebeveiliging en dienstverlening in overeenstemming met "
         "de leveranciers-overeenkomsten handhaven.",
    fragments=[

        Norm(
            identifier="15.02.01",
            title="Monitoring en beoordeling van dienstverlening van leveranciers",
            text="Organisaties behoren regelmatig de dienstverlening van leveranciers te monitoren, te beoordelen en "
                 "te auditen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="15.02.01/01",
                    title="",
                    text="Jaarlijks wordt de prestatie van leveranciers op het gebied van informatiebeveiliging "
                         "beoordeeld op vooraf vastgestelde prestatie-indicatoren, zoals in het contract opgenomen "
                         "is.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="15.02.02",
            title="Beheer van veranderingen in dienstverlening van leveranciers",
            text="Veranderingen in de dienstverlening van leveranciers, met inbegrip van handhaving en verbetering "
                 "van bestaande beleidslijnen, procedures en beheersmaatregelen voor informatiebeveiliging, behoren "
                 "te worden, beheerd, rekening houdend met de kritikaliteit van bedrijfsinformatie, betrokken "
                 "systemen en processen en herbeoordeling van risico's.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="15.02.02/01",
                    title="",
                    text="- conform norm -",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH15 = Chapter(
    identifier="15",
    title="Leveranciersrelaties",
    fragments=[
        CH15S01,
        CH15S02,
    ]
)
