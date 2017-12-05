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

S1301 = Section(
    identifier="13.01",
    title=u"Beheer van netwerkbeveiliging",
    text=u"Doelstelling: De bescherming van informatie in netwerken en de ondersteunende informatieverwerkende "
         u"faciliteiten waarborgen.",
    fragments=[

        Norm(
            identifier="13.01.01",
            title=u"Beheersmaatregelen voor netwerken",
            text=u"Netwerken behoren te worden beheerd en beheerst om informatie in systemen en toepassingen te "
                 u"beschermen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.01.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="13.01.02",
            title=u"Beveiliging van netwerkdiensten",
            text=u"Beveiligingsmechanismen, dienstverleningsniveaus en beheerseisen voor alle netwerkdiensten behoren "
                 u"te worden geïdentificeerd en opgenomen in overeenkomsten betreffende netwerkdiensten. Dit geldt "
                 u"zowel voor diensten die intern worden geleverd als voor uitbestede diensten.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.01.02/01",
                    title=u"",
                    text=u"Het dataverkeer dat de organisatie binnenkomt of uitgaat wordt bewaakt / geanalyseerd op "
                         u"kwaadaardige elementen middels detectie-voorzieningen (zoals beschreven in de richtlijn "
                         u"voor implementatie van detectie-oplossingen), zoals het Nationaal Detectie Netwerk, die "
                         u"worden ingezet op basis van een risico-inschatting, mede aan de hand van  de aard van de "
                         u"te beschermen gegevens en informatiesystemen.",
                    bbn=2,
                ),
                Verifier(
                    identifier="13.01.02/02",
                    title=u"",
                    text=u"Bij ontdekte nieuwe dreigingen vanuit 13.01.02/01 worden deze, rekening houdend met "
                         u"de geldende juridische kaders, gedeeld binnen de overheid, waaronder met het NCSC, "
                         u"bij voorkeur door geautomatiseerde mechanismen (threat intelligence sharing).",
                    bbn=2,
                ),
                Verifier(
                    identifier="13.01.02/03",
                    title=u"",
                    text=u"Bij draadloze verbindingen zoals wifi en bij bedrade verbindingen buiten "
                         u"het gecontroleerd gebied, wordt gebruik gemaakt van encryptie middelen waarvoor "
                         u"het NBV een positief inzetadvies heeft afgegeven.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="13.01.03",
            title=u"Scheiding in netwerken",
            text=u"Groepen van informatiediensten, -gebruikers en -systemen behoren in netwerken te worden gescheiden.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.01.03/01",
                    title=u"",
                    text=u"Alle gescheiden groepen hebben een gedefinieerd beveiligingsniveau.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


S1302 = Section(
    identifier="13.02",
    title=u"Informatietransport",
    text=u"Doelstelling: Handhaven van de beveiliging van informatie die wordt uitgewisseld binnen een organisatie en "
         u"met een externe entiteit.",
    fragments=[

        Norm(
            identifier="13.02.01",
            title=u"Beleid en procedures voor informatietransport",
            text=u"Ter bescherming van het informatietransport, dat via alle soorten communicatiefaciliteiten "
                 u"verloopt, behoren formele beleidsregels, procedures en beheersmaatregelen voor transport van kracht "
                 u"te zijn.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.02.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="13.02.02",
            title=u"Overeenkomsten over informatietransport",
            text=u"Overeenkomsten behoren betrekking te hebben op het beveiligd transporteren van bedrijfsinformatie "
                 u"tussen de organisatie en externe partijen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.02.02/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="13.02.03",
            title=u"Elektronische berichten",
            text=u"Informatie die is opgenomen in elektronische berichten behoord passend te zijn beschermd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.02.03/01",
                    title=u"",
                    text=u"Voor de beveiliging van elektronische berichten gelden de vastgestelde standaarden tegen "
                         u"phishing en afluisteren op pas-toe-of-leg-uit lijst van het forum standaardisatie.",
                    bbn=1,
                ),
                Verifier(
                    identifier="13.02.03/02",
                    title=u"",
                    text=u"Voor veilige berichtenuitwisseling met basisregistraties, wordt conform "
                         u"de pas-toe-leg-uit-lijst, gebruik gemaakt van de actuele versie van Digikoppeling",
                    bbn=2,
                ),
                Verifier(
                    identifier="13.02.03/03",
                    title=u"",
                    text=u"Maak gebruik van PKI-Overheid certificaten bij web- en mailverkeer van gevoelige gegevens. "
                         u"Gevoelige gegevens zijn o.a. digitale documenten binnen de Rijksdienst waar gebruikers "
                         u"rechten aan kunnen ontlenen.",
                    bbn=2,
                ),
                Verifier(
                    identifier="13.02.03/04",
                    title=u"",
                    text=u"Om zekerheid te bieden over de integriteit van het elektronische bericht wordt voor "
                         u"elektronische handtekeningen gebruik gemaakt van de AdES Baseline Profile standaard.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="13.02.04",
            title=u"Vertrouwelijkheids- of geheimhoudingsovereenkomst",
            text=u"Eisen voor vertrouwelijkheids- of geheimhoudingsovereenkomsten die de behoeften van de organisatie "
                 u"betreffende het beschermen van informatie weerspiegelen, behoren te worden vastgesteld, regelmatig "
                 u"te worden beoordeeld en gedocumenteerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.02.04/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


CH13 = Chapter(
    identifier="13",
    title=u"Communicatiebeveiliging",
    fragments=[
        S1301,
        S1302,
    ]
)
