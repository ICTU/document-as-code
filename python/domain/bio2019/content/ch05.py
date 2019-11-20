"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH05S01 = Section(
    identifier="05.01",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="05.01.01",
            title="TITLE",
            text="""
Beleidsregels voor informatiebeveiliging;
Ten behoeve van informatiebeveiliging behoort een reeks beleidsregels te worden gedefinieerd, goedgekeurd door de directie, gepubliceerd en gecommuniceerd aan medewerkers en relevante externe partijen.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="05.01.01/01",
                    title="",
                    text="""
Er is een informatiebeveiligingsbeleid opgesteld door de organisatie. Dit beleid is vastgesteld door de leiding van de organisatie en bevat tenminste de volgende punten:
 a. de strategische uitgangspunten en randvoorwaarden die de organisatie hanteert voor informatiebeveiliging en in het bijzonder de inbedding in, en afstemming op het algemene beveiligingsbeleid en het informatievoorzieningsbeleid;
b.Â Â Â  de organisatie van de informatiebeveiligingsfunctie, waaronder verantwoordelijkheden, taken en bevoegdheden;
c.Â Â Â Â  de toewijzing van de verantwoordelijkheden voor ketens van informatiesystemen aan lijnmanagers;
d.Â Â Â  de gemeenschappelijke betrouwbaarheidseisen en normen die op de organisatie van toepassing zijn;
e.Â Â Â  de frequentie waarmee het informatiebeveiligingsbeleid wordt geÃ«valueerd;
f.Â Â Â Â  de bevordering van het beveiligingsbewustzijn.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="05.01.02",
            title="TITLE",
            text="""
Beoordeling van het informatiebeveiligingsbeleid;
Het beleid voor informatiebeveiliging behoort met geplande tussenpozen of als zich significante veranderingen voordoen, te worden beoordeeld om te waarborgen dat het voortdurend passend, adequaat en doeltreffend is.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="05.01.02/01",
                    title="",
                    text="""
Het informatiebeveiligingsbeleid wordt minimaal Ã©Ã©n keer per drie jaar, of bij belangrijke wijzigingen als gevolg van reorganisatie of verandering in de verantwoordelijkheidsverdeling, beoordeeld en zo nodig bijgesteld. 
                    """,
                    bbn=1,
                )
            ],
        )
    ],
)


CH05 = Chapter(
    identifier="05",
    title="TITLE",
    fragments=[
        CH05S01
    ]
)
