"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH18S01 = Section(
    identifier="18.01",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="18.01.03",
            title="TITLE",
            text="""
Beschermen van registraties;
Registraties behoren in overeenstemming met wettelijke, regelgevende, contractuele en bedrijfseisen te worden beschermd tegen verlies, vernietiging, vervalsing, onbevoegde toegang en onbevoegde vrijgave.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="18.01.03/01",
                    title="",
                    text="""
De proceseigenaar heeft per soort informatie inzichtelijk gemaakt wat de bewaartermijn is.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="18.01.04",
            title="TITLE",
            text="""
Privacy en bescherming van persoonsgegevens;
Privacy en bescherming van persoonsgegevens behoren, voor zover van toepassing, te worden gewaarborgd in overeenstemming met relevante wet- en regelgeving.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.01.04/01",
                    title="",
                    text="""
In overeenstemming met de AVG heeft iedere organisatie een Functionaris Gegevensbescherming (FG) met voldoende mandaat om zijn/haar functie uit te voeren.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="18.01.04/02",
                    title="",
                    text="""
Organisaties controleren regelmatig de naleving van de privacy regels en informatieverwerking en âprocedures binnen haar verantwoordelijkheidsgebied aan de hand van de desbetreffende beleidsregels, normen en andere eisen betreffende beveiliging.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH18S02 = Section(
    identifier="18.02",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="18.02.01",
            title="TITLE",
            text="""
Onafhankelijke beoordeling van informatiebeveiliging;
De aanpak van de organisatie ten aanzien van het beheer van informatiebeveiliging en de implementatie ervan (bijv. beheerdoelstellingen, beheersmaatregelen, beleidsregels, processen en procedures voor informatiebeveiliging), behoren onafhankelijk en met geplande tussenpozen of zodra zich belangrijke veranderingen voordoen te worden beoordeeld.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="18.02.01/01",
                    title="",
                    text="""
Er is een information security information system (ISMS) waarmee aantoonbaar de gehele plan-do-check-act cyclus op gestructureerde wijze wordt afgedekt.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="18.02.01/02",
                    title="",
                    text="""
Er is een vastgesteld auditplan waarin jaarlijks keuzes worden gemaakt voor welke systemen welk soort beveiligingsaudits worden uitgevoerd.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="18.02.02",
            title="TITLE",
            text="""
Naleving van beveiligingsbeleid en -normen;
De directie behoort regelmatig de naleving van de informatieverwerking en - procedures binnen haar verantwoordelijkheidsgebied te beoordelen aan de hand van de desbetreffende beleidsregels, normen en andere eisen betreffende beveiliging.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.02.02/01",
                    title="",
                    text="""
In de P&C cyclus wordt gerapporteerd over informatiebeveiliging, resulterend in een jaarlijks af te geven In Control Verklaring (ICV) over de informatiebeveiliging. Indien voldoende herkenbaar kan de ICV voor informatiebeveiliging onderdeel zijn van de reguliere, generieke verantwoording.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="18.02.03",
            title="TITLE",
            text="""
Beoordeling van technische naleving;
Informatiesystemen behoren regelmatig te worden beoordeeld op naleving van de beleidsregels en normen van de organisatie voor informatiebeveiliging.
            """,
            bbn=666,
            fragments=[
                Verifier(
                    identifier="18.02.03/01",
                    title="",
                    text="""
Informatiesystemen worden jaarlijks gecontroleerd op technische naleving van beveiligingsnormen en risicoâs ten aanzien van de feitelijke veiligheid. Dit kan bijvoorbeeld door (geautomatiseerde) kwetsbaarheidsanalyses of pentesten.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="18.02.03/01",
                    title="",
                    text="""
Informatiesystemen worden jaarlijks gecontroleerd op technische naleving van beveiligingsnormen en risicoâs ten aanzien van de feitelijke veiligheid. Dit kan bijvoorbeeld door (geautomatiseerde) kwetsbaarheidsanalyses of pentesten.
                    """,
                    bbn=666,
                ),
                Verifier(
                    identifier="18.02.03/01",
                    title="",
                    text="""
Informatiesystemen worden jaarlijks gecontroleerd op technische naleving van beveiligingsnormen en risicoâs ten aanzien van de feitelijke veiligheid. Dit kan bijvoorbeeld door (geautomatiseerde) kwetsbaarheidsanalyses of pentesten.
                    """,
                    bbn=666,
                ),
                Verifier(
                    identifier="18.02.03/01",
                    title="",
                    text="""
Informatiesystemen worden jaarlijks gecontroleerd op technische naleving van beveiligingsnormen en risicoâs ten aanzien van de feitelijke veiligheid. Dit kan bijvoorbeeld door (geautomatiseerde) kwetsbaarheidsanalyses of pentesten.
                    """,
                    bbn=666,
                )
            ],
        )
    ],
)


CH18 = Chapter(
    identifier="18",
    title="TITLE",
    fragments=[
        CH18S01,
        CH18S02
    ]
)
