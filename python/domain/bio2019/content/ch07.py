"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH07S01 = Section(
    identifier="07.01",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="07.01.01",
            title="TITLE",
            text="""
Screening;
Verificatie van de achtergrond van alle kandidaten voor een dienstverband behoort te worden uitgevoerd in overeenstemming met relevante wet- en regelgeving en ethische overwegingen en behoort in verhouding te staan tot de bedrijfseisen, de classificatie van de informatie waartoe toegang wordt verleend en de vastgestelde risicoâs te zijn.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="07.01.01/01",
                    title="",
                    text="""
Bij indiensttreding overleggen alle medewerkers (intern en extern) een specifiek voor de functie verstrekte Verklaring Omtrent het Gedrag (VOG).
                    """,
                    bbn=1,
                )
            ],
        )
    ],
)


CH07S02 = Section(
    identifier="07.02",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="07.02.01",
            title="TITLE",
            text="""
Directieverantwoordelijkheden;
De directie behoort van alle medewerkers en contractanten te eisen dat ze informatie beveiliging toepassen in overeenstemming met de vastgestelde beleidsregels en procedures van de organisatie.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="07.02.01/01",
                    title="",
                    text="""
Er is aansluiting bij een klokkenluidersregeling, zodat iedereen in staat is om anoniem en veilig beveiligingsissues te kunnen melden.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="07.02.02",
            title="TITLE",
            text="""
Bewustzijn, opleiding en training ten aanzien van informatiebeveiliging;
 Alle medewerkers van de organisatie en, voor zover relevant, contractanten behoren een passende bewustzijnsopleiding en -training te krijgen en regelmatige bijscholing van beleidsregels en procedures van de organisatie, voor zover relevant voor hun functie.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="07.02.02/01",
                    title="",
                    text="""
Alle medewerkers hebben de verantwoordelijkheid bedrijfsinformatie te beschermen. Iedereen kent de regels en verplichtingen met betrekking tot informatiebeveiliging en daar waar relevant de speciale eisen voor gerubriceerde omgevingen
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="07.02.02/02",
                    title="",
                    text="""
Alle medewerkers en contractanten die gebruikmaken van de informatiesystemen- en diensten hebben binnen drie maanden na indiensttreding een training I-bewustzijn succesvol gevolgd.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="07.02.02/03",
                    title="",
                    text="""
Het management benadrukt bij aanstelling en interne overplaatsing en bijvoorbeeld in werkoverleggen of in personeelsgesprekken bij haar medewerkers en contractanten het belang van opleiding en training op het gebied van informatiebeveiliging en stimuleert hen actief deze periodiek te volgen
                    """,
                    bbn=1,
                )
            ],
        )
    ],
)


CH07 = Chapter(
    identifier="07",
    title="TITLE",
    fragments=[
        CH07S01,
        CH07S02
    ]
)
