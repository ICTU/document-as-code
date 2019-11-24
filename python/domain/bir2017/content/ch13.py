# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S1301 = Section(
    identifier="13.01",
    title="Beheer van netwerkbeveiliging",
    text="Doelstelling: De bescherming van informatie in netwerken en de ondersteunende informatieverwerkende "
         "faciliteiten waarborgen.",
    fragments=[

        Norm(
            identifier="13.01.01",
            title="Beheersmaatregelen voor netwerken",
            text="Netwerken behoren te worden beheerd en beheerst om informatie in systemen en toepassingen te "
                 "beschermen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.01.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="13.01.02",
            title="Beveiliging van netwerkdiensten",
            text="Beveiligingsmechanismen, dienstverleningsniveaus en beheerseisen voor alle netwerkdiensten behoren "
                 "te worden ge&iuml;dentificeerd en opgenomen in overeenkomsten betreffende netwerkdiensten. Dit geldt "
                 "zowel voor diensten die intern worden geleverd als voor uitbestede diensten.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.01.02/01",
                    title="",
                    text="Het dataverkeer dat de organisatie binnenkomt of uitgaat wordt bewaakt / geanalyseerd op "
                         "kwaadaardige elementen middels detectie-voorzieningen (zoals beschreven in de richtlijn "
                         "voor implementatie van detectie-oplossingen), zoals het "
                         "Nationaal Detectie Netwerk, "
                         "die worden ingezet op basis van een risico-inschatting, mede aan de hand van de aard van "
                         "de te beschermen gegevens en informatiesystemen.",
                    bbn=2,
                ),
                Verifier(
                    identifier="13.01.02/02",
                    title="",
                    text="Bij ontdekte nieuwe dreigingen vanuit 13.01.02/01 worden deze, rekening houdend met "
                         "de geldende juridische kaders, "
                         "gedeeld binnen de overheid, waaronder met het "
                         "NCSC, "
                         "bij voorkeur door geautomatiseerde mechanismen (threat intelligence sharing).",
                    bbn=2,
                ),
                Verifier(
                    identifier="13.01.02/03",
                    title="",
                    text="Bij draadloze verbindingen zoals wifi en bij bedrade verbindingen buiten "
                         "het gecontroleerd gebied, wordt gebruik gemaakt van encryptie middelen waarvoor "
                         "het NBV een positief inzetadvies heeft afgegeven.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="13.01.03",
            title="Scheiding in netwerken",
            text="Groepen van informatiediensten, -gebruikers en -systemen behoren in netwerken te worden gescheiden.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.01.03/01",
                    title="",
                    text="Alle gescheiden groepen hebben een gedefinieerd beveiligingsniveau.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S1302 = Section(
    identifier="13.02",
    title="Informatietransport",
    text="Doelstelling: Handhaven van de beveiliging van informatie die wordt uitgewisseld binnen een organisatie en "
         "met een externe entiteit.",
    fragments=[

        Norm(
            identifier="13.02.01",
            title="Beleid en procedures voor informatietransport",
            text="Ter bescherming van het informatietransport, dat via alle soorten communicatiefaciliteiten "
                 "verloopt, behoren formele beleidsregels, procedures en beheersmaatregelen voor transport van kracht "
                 "te zijn.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.02.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="13.02.02",
            title="Overeenkomsten over informatietransport",
            text="Overeenkomsten behoren betrekking te hebben op het beveiligd transporteren van bedrijfsinformatie "
                 "tussen de organisatie en externe partijen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.02.02/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="13.02.03",
            title="Elektronische berichten",
            text="Informatie die is opgenomen in elektronische berichten behoord passend te zijn beschermd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.02.03/01",
                    title="",
                    text="Voor de beveiliging van elektronische berichten gelden de vastgestelde standaarden tegen "
                         "phishing en afluisteren op pas-toe-of-leg-uit lijst van het forum standaardisatie.",
                    bbn=1,
                ),
                Verifier(
                    identifier="13.02.03/02",
                    title="",
                    text="Voor veilige berichtenuitwisseling met basisregistraties, wordt conform "
                         "de pas-toe-of-leg-uit-lijst, gebruik gemaakt van de actuele versie van Digikoppeling.",
                    bbn=2,
                ),
                Verifier(
                    identifier="13.02.03/03",
                    title="",
                    text="Maak gebruik van PKI-Overheid certificaten bij web- en mailverkeer van gevoelige gegevens. "
                         "Gevoelige gegevens zijn o.a. digitale documenten binnen de "
                         "Rijksdienst "
                         "waar gebruikers rechten aan kunnen ontlenen.",
                    bbn=2,
                ),
                Verifier(
                    identifier="13.02.03/04",
                    title="",
                    text="Om zekerheid te bieden over de integriteit van het elektronische bericht wordt voor "
                         "elektronische handtekeningen gebruik gemaakt van de AdES Baseline Profile standaard.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="13.02.04",
            title="Vertrouwelijkheids- of geheimhoudingsovereenkomst",
            text="Eisen voor vertrouwelijkheids- of geheimhoudingsovereenkomsten die de behoeften van de organisatie "
                 "betreffende het beschermen van informatie weerspiegelen, behoren te worden vastgesteld, regelmatig "
                 "te worden beoordeeld en gedocumenteerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.02.04/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


CH13 = Chapter(
    identifier="13",
    title="Communicatiebeveiliging",
    fragments=[
        S1301,
        S1302,
    ]
)
