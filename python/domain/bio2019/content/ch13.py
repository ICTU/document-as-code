"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH13S01 = Section(
    identifier="13.01",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="13.01.02",
            title="TITLE",
            text="""
Beveiliging van netwerkdiensten;
Beveiligingsmechanismen, dienstverleningsniveaus en beheer eisen voor alle netwerkdiensten behoren te worden geÃ¯dentificeerd en opgenomen in overeenkomsten betreffende netwerkdiensten. Dit geldt zowel voor diensten die intern worden geleverd als voor uitbestede diensten.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="13.01.02/01",
                    title="",
                    text="""
Het dataverkeer dat de organisatie binnenkomt of uitgaat wordt bewaakt / geanalyseerd op kwaadaardige elementen middels detectie-voorzieningen (zoals beschreven in de richtlijn voor implementatie van detectie-oplossingen), zoals het Nationaal Detectie Netwerk (alleen voor rijksoverheidsorganisaties) of GDI, die worden ingezet op basis van een risico-inschatting, mede aan de hand van de aard van de te beschermen gegevens en informatiesystemen.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="13.01.02/02",
                    title="",
                    text="""
Bij ontdekte nieuwe dreigingen vanuit 13.1.2.1 worden deze, rekening houdend met de geldende juridische kaders, verplicht gedeeld binnen de overheid, waaronder met het NCSC (alleen voor rijksoverheidsorganisaties) of de sectorale CERT, bij voorkeur door geautomatiseerde mechanismen (threat intelligence sharing).
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="13.01.02/03",
                    title="",
                    text="""
Bij draadloze verbindingen zoals wifi en bij bedrade verbindingen buiten het gecontroleerd gebied, wordt gebruik gemaakt van encryptie middelen waarvoor het NBV een positief inzetadvies heeft afgegeven.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH13S02 = Section(
    identifier="13.02",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="13.02.03",
            title="TITLE",
            text="""
Elektronische berichten;
Informatie die is opgenomen in elektronische berichten behoord passend te zijn beschermd.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="13.02.03/01",
                    title="",
                    text="""
Voor de beveiliging van elektronische berichten gelden de vastgestelde standaarden tegen phishing en afluisteren op pas-toe-of-leg-uit lijst van het forum standaardisatie.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="13.02.03/02",
                    title="",
                    text="""
Voor veilige berichtenuitwisseling met basisregistraties, wordt conform de pastoe-of-leg-uit lijst, gebruik gemaakt van de actuele versie van Digikoppeling
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="13.02.03/03",
                    title="",
                    text="""
Maak gebruik van PKI-Overheid certificaten bij web- en mailverkeer van gevoelige gegevens. Gevoelige gegevens zijn o.a. digitale documenten binnen de overheid waar gebruikers rechten aan kunnen ontlenen.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="13.02.03/04",
                    title="",
                    text="""
Om zekerheid te bieden over de integriteit van het elektronische bericht wordt voor elektronische handtekeningen gebruik gemaakt van de AdES Baseline Profile standaard of de of de ETSI TS 102 176-1.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH13 = Chapter(
    identifier="13",
    title="TITLE",
    fragments=[
        CH13S01,
        CH13S02
    ]
)
