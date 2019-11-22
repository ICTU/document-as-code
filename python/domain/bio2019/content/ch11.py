"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH11S01 = Section(
    identifier="11.01",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="11.01.01",
            title="TITLE",
            text="""
Fysieke beveiligingszone;
Beveiligingszones behoren te worden gedefinieerd en gebruikt om gebieden te beschermen die gevoelige of essentiÃ«le informatie en informatie verwerkende faciliteiten bevatten. 
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.01/01",
                    title="",
                    text="""
Er wordt voor het inrichten van beveiligde zones gebruik gemaakt van standaarden.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="11.01.02",
            title="TITLE",
            text="""
Fysieke toegangsbeveiliging;
Beveiligde gebieden behoren te worden beschermd door passende toegangsbeveiliging om ervoor te zorgen dat alleen bevoegd personeel toegang krijgt.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="11.01.02/01",
                    title="",
                    text="""
In geval van concrete beveiligingsrisicoâs worden waarschuwingen, conform onderlinge afspraken, verzonden aan de relevante collegaâs binnen het beveiligingsdomein van de overheid.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="11.01.03",
            title="TITLE",
            text="""
Kantoren, ruimten en faciliteiten beveiligen;
Voor kantoren, ruimten en faciliteiten behoort fysieke beveiliging te worden ontworpen en toegepast.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.03/01",
                    title="",
                    text="""
Sleutelbeheer is ingericht op basis van een sleutelplan.
                    """,
                    bbn=1,
                )
            ],
        )
    ],
)


CH11S02 = Section(
    identifier="11.02",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="11.02.09",
            title="TITLE",
            text="""
âClear deskâ- en âclear screenâ-beleid;
Er behoort een âclear deskâ-beleid voor papieren documenten en verwijderbare opslagmedia en een âclear screenâ-beleid voor informatieverwerkende faciliteiten te worden ingesteld.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="11.02.09/01",
                    title="",
                    text="""
Een onbeheerde werkplek in een ongecontroleerde omgeving is altijd vergrendeld.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="11.02.09/02",
                    title="",
                    text="""
Informatie wordt automatisch ontoegankelijk gemaakt met bijvoorbeeld een screensaver na een inactiviteit van maximaal 15 minuten.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="11.02.09/03",
                    title="",
                    text="""
Sessies op remote desktops worden op het remote platform vergrendeld na 15 minuten. Het overnemen van sessies op remote desktops op een ander client apparaat is alleen mogelijk via dezelfde beveiligde loginprocedure als waarmee de sessie is gecreÃ«erd.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="11.02.09/04",
                    title="",
                    text="""
Bij het gebruik van een chipcardtoken voor toegang tot systemen wordt bij het verwijderen van de token de toegangsbeveiligingslock automatisch geactiveerd.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH11 = Chapter(
    identifier="11",
    title="TITLE",
    fragments=[
        CH11S01,
        CH11S02
    ]
)
