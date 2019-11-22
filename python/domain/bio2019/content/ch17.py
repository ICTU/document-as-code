"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH17S01 = Section(
    identifier="17.01",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="17.01.03",
            title="TITLE",
            text="""
InformatiebeveiligingscontinuÃ¯teit verifiÃ«ren, beoordelen en evalueren;
De organisatie behoort de ten behoeve van informatiebeveiligingscontinuÃ¯teit vastgestelde en geÃ¯mplementeerde beheersmaatregelen regelmatig te verifiÃ«ren om te waarborgen dat ze deugdelijk en doeltreffend zijn tijdens ongunstige situaties.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="17.01.03/01",
                    title="",
                    text="""
ContinuÃ¯teitsplannen worden jaarlijks getest op geldigheid en bruikbaarheid.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="17.01.03/02",
                    title="",
                    text="""
Door het uitvoeren van een expliciete risicoafweging worden de bedrijfskritische procesonderdelen met hun bijbehorende betrouwbaarheidseisen geÃ¯dentificeerd.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="17.01.03/03",
                    title="",
                    text="""
De dienstverlening van de bedrijfskritische onderdelen wordt bij calamiteiten minimaal binnen een week hersteld.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH17 = Chapter(
    identifier="17",
    title="TITLE",
    fragments=[
        CH17S01
    ]
)
