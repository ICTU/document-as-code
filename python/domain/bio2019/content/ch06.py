"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH06S01 = Section(
    identifier="06.01",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="06.01.01",
            title="TITLE",
            text="""
Rollen en verantwoordelijkheden bij informatiebeveiliging;
Alle verantwoordelijkheden bij informatiebeveiliging behoren te worden gedefinieerd en toegewezen.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="06.01.01/01",
                    title="",
                    text="""
De leiding van de organisatie heeft vastgelegd wat de verantwoordelijkheden en rollen zijn op het gebied van informatiebeveiliging binnen haar organisatie.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/02",
                    title="",
                    text="""
De verantwoordelijkheden en rollen ten aanzien van informatiebeveiliging zijn gebaseerd op relevante voorschriften en wetten.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/02",
                    title="",
                    text="""
De verantwoordelijkheden en rollen ten aanzien van informatiebeveiliging zijn gebaseerd op relevante voorschriften en wetten.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/03",
                    title="",
                    text="""
De rol en verantwoordelijkheden van de Chief Information Security Officer (CISO) zijn in een CISO-functieprofiel vastgelegd.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/03",
                    title="",
                    text="""
De rol en verantwoordelijkheden van de Chief Information Security Officer (CISO) zijn in een CISO-functieprofiel vastgelegd.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="06.01.01/04",
                    title="",
                    text="""
Er is een CISO aangesteld conform een vastgesteld CISO-functieprofiel.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="06.01.02",
            title="TITLE",
            text="""
Scheiding van taken;
Conflicterende taken en verantwoordelijkheden behoren te worden gescheiden om de kans op onbevoegd of onbedoeld wijzigen of misbruik van de bedrijfsmiddelen van de organisatie te verminderen.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="06.01.02/01",
                    title="",
                    text="""
Er zijn maatregelen getroffen die onbedoelde of ongeautoriseerde toegang tot bedrijfsmiddelen waarnemen of voorkomen.
                    """,
                    bbn=1,
                )
            ],
        )
    ],
)


CH06S02 = Section(
    identifier="06.02",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="06.02.01",
            title="TITLE",
            text="""
Beleid voor mobiele apparatuur;
Beleid en ondersteunende beveiligingsmaatregelen behoren te worden vastgesteld om de risicoâs die het gebruik van mobiele apparatuur met zich meebrengt te beheren.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="06.02.01/01",
                    title="",
                    text="""
Mobiele apparatuur is zo ingericht dat geen bedrijfsinformatie onbewust wordt opgeslagen (âzero footprintâ). Als zero footprint (nog) niet realiseerbaar is, biedt een mobiel apparaat (zoals een laptop, tablet en smartphone) de mogelijkheid om de toegang te beschermen door middel van een toegangsbeveiligingsmechanisme en, indien vertrouwelijke gegevens worden opgeslagen, versleuteling van die gegevens. In het geval van opslag van vertrouwelijke informatie moet op deze mobiele apparatuur âwissen op afstandâ mogelijk zijn.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="06.02.01/02",
                    title="",
                    text="""
Bij de inzet van mobiele apparatuur zijn minimaal de volgende aspecten geÃ¯mplementeerd:
a.Â Â Â  in bewustwordingsprogrammaâs komen gedragsaspecten van veilig mobiel werken aan de orde; 
b.Â Â Â  het device maakt onderdeel uit van patchmanagement en hardening;
c.Â Â Â Â  het device wordt waar mogelijk beheerd en beveiligd via een MDM Mobile Device Management (MDM)-oplossing; 
d.Â Â Â  gebruikers tekenen een gebruikersovereenkomst voor mobiel werken, waarmee zij verklaren zich bewust te zijn van de gevaren van mobiel werken en verklaren dit veilig te zullen doen. Deze verklaring heeft betrekking op alle mobiele apparatuur die de medewerker zakelijk gebruikt;
e.Â Â Â  periodiek wordt getoetst of de punten in lid b), c) en d) worden nageleefd.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH06 = Chapter(
    identifier="06",
    title="TITLE",
    fragments=[
        CH06S01,
        CH06S02
    ]
)
