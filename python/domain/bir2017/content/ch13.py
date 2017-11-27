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
    title=u"",
    fragments=[

        Norm(
            identifier="13.01.01",
            title=u"",
            text=u"Beheersmaatregelen voor netwerken: Netwerken behoren te worden beheerd en beheerst om informatie "
                 u"in systemen en toepassingen te beschermen.",
            fragments=[
            ],
        ),

        Norm(
            identifier="13.01.02",
            title=u"",
            text=u"Beveiliging van netwerkdiensten: Beveiligingsmechanismen, dienstverleningsniveaus en beheerseisen "
                 u"voor alle netwerkdiensten behoren te worden geïdentificeerd en opgenomen in overeenkomsten "
                 u"betreffende netwerkdiensten. Dit geldt zowel voor diensten die intern worden geleverd als "
                 u"voor uitbestede diensten.",
            fragments=[
                Verifier(
                    identifier="13.01.02/01",
                    title=u"",
                    text=u"Het dataverkeer dat de organisatie binnenkomt of uitgaat wordt bewaakt / geanalyseerd op "
                         u"kwaadaardige elementen middels detectie-voorzieningen (zoals beschreven in de richtlijn "
                         u"voor implementatie van detectie-oplossingen), zoals het Nationaal Detectie Netwerk, die "
                         u"worden ingezet op basis van een risico-inschatting, mede aan de hand van  de aard van de "
                         u"te beschermen gegevens en informatiesystemen.",
                ),
                Verifier(
                    identifier="13.01.02/02",
                    title=u"",
                    text=u"Bij ontdekte nieuwe dreigingen vanuit 13.01.02/01 worden deze, rekening houdend met "
                         u"de geldende juridische kaders, gedeeld binnen de overheid, waaronder met het NCSC, "
                         u"bij voorkeur door geautomatiseerde mechanismen (threat intelligence sharing).",
                ),
                Verifier(
                    identifier="13.01.02/03",
                    title=u"",
                    text=u"Bij draadloze verbindingen zoals wifi en bij bedrade verbindingen buiten "
                         u"het gecontroleerd gebied, wordt gebruik gemaakt van encryptie middelen waarvoor "
                         u"het NBV een positief inzetadvies heeft afgegeven.",
                ),
            ],
        ),

        Norm(
            identifier="13.01.03",
            title=u"",
            text=u"Scheiding in netwerken: Groepen van informatiediensten, -gebruikers en -systemen behoren "
                 u"in netwerken te worden gescheiden.",
            fragments=[
                Verifier(
                    identifier="13.01.03/01",
                    title=u"",
                    text=u"Alle gescheiden groepen hebben een gedefinieerd beveiligingsniveau.",
                ),
            ],
        ),

    ],
)


S1302 = Section(
    identifier="13.02",
    title=u"",
    fragments=[

        Norm(
            identifier="13.02.01",
            title=u"",
            text=u"Beleid en procedures voor informatietransport: Ter bescherming van het informatietransport, "
                 u"dat via alle soorten communicatiefaciliteiten verloopt, behoren formele beleidsregels, "
                 u"procedures en beheersmaatregelen voor transport van kracht te zijn.",
            fragments=[
            ],
        ),

        Norm(
            identifier="13.02.02",
            title=u"",
            text=u"Overeenkomsten over informatietransport: Overeenkomsten behoren betrekking te hebben op "
                 u"het beveiligd transporteren van bedrijfsinformatie tussen de organisatie en externe partijen.",
            fragments=[
            ],
        ),

        Norm(
            identifier="13.02.03",
            title=u"",
            text=u"Elektronische berichten: Informatie die is opgenomen in elektronische berichten behoord passend "
                 u"te zijn beschermd.",
            fragments=[
                Verifier(
                    identifier="13.02.03/01",
                    title=u"",
                    text=u"Voor de beveiliging van elektronische berichten gelden de vastgestelde standaarden tegen "
                         u"phishing en afluisteren op pas-toe-of-leg-uit lijst van het forum standaardisatie.",
                ),
                Verifier(
                    identifier="13.02.03/02",
                    title=u"",
                    text=u"Voor veilige berichtenuitwisseling met basisregistraties, wordt conform "
                         u"de pas-toe-leg-uit-lijst, gebruik gemaakt van de actuele versie van Digikoppeling",
                ),
                Verifier(
                    identifier="13.02.03/03",
                    title=u"",
                    text=u"Maak gebruik van PKI-Overheid certificaten bij web- en mailverkeer van gevoelige gegevens. "
                         u"Gevoelige gegevens zijn o.a. digitale documenten binnen de Rijksdienst waar gebruikers "
                         u"rechten aan kunnen ontlenen.",
                ),
                Verifier(
                    identifier="13.02.03/04",
                    title=u"",
                    text=u"Om zekerheid te bieden over de integriteit van het elektronische bericht wordt voor "
                         u"elektronische handtekeningen gebruik gemaakt van de AdES Baseline Profile standaard.",
                ),
            ],
        ),

        Norm(
            identifier="13.02.04",
            title=u"",
            text=u"Vertrouwelijkheids- of geheimhoudingsovereenkomst: Eisen voor vertrouwelijkheids- of "
                 u"geheimhoudingsovereenkomsten die de behoeften van de organisatie betreffende het beschermen "
                 u"van informatie weerspiegelen, behoren te worden vastgesteld, regelmatig te worden beoordeeld "
                 u"en gedocumenteerd.",
            fragments=[
            ],
        ),

    ],
)


CH13 = Chapter(
    identifier="13",
    title=u"Communications security",
    fragments=[
        S1301,
        S1302,
    ]
)
