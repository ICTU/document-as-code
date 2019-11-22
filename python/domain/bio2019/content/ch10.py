"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH10S01 = Section(
    identifier="10.01",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="10.01.01",
            title="TITLE",
            text="""
Beleid inzake het gebruik van cryptografische beheersmaatregelen Ter bescherming van informatie behoort een beleid voor het gebruik van cryptografische beheersmaatregelen te worden ontwikkeld en geÃ¯mplementeerd.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="10.01.01/01",
                    title="",
                    text="""
In het cryptografiebeleid zijn minimaal de volgende onderwerpen uitgewerkt:
(a) wanneer cryptografie ingezet wordt;
(b) wie verantwoordelijk is voor de implementatie;
(c) wie verantwoordelijk is voor het sleutelbeheer;
(d)welke normen als basis dienen voor cryptografie en de wijze waarop de normen van het forum standaardisatie worden toegepast;
(e) de wijze waarop het beschermingsniveau vastgesteld wordt;
(f) bij inter-organisatie communicatie wordt het beleid onderling vastgesteld.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="10.01.01/02",
                    title="",
                    text="""
Cryptografische toepassingen voldoen aan passende standaarden.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="10.01.02",
            title="TITLE",
            text="""
Sleutelbeheer;
Met betrekking tot het gebruik, de bescherming en de levensduur van cryptografische sleutels behoort tijdens hun gehele levenscyclus een beleid te worden ontwikkeld en geÃ¯mplementeerd. 
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="10.01.02/01",
                    title="",
                    text="""
Ingeval van PKI-overheid certificaten: hanteer de PKI-Overheid-eisen t.a.v. het sleutelbeheer. In overige situaties: hanteer de standaard ISO-11770 voor het beheer van cryptografische sleutels.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="10.01.02/02",
                    title="",
                    text="""
Er zijn (contractuele) afspraken over reservecertificaten van een alternatieve leverancier als uit risicoafweging blijkt dat deze noodzakelijk zijn.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH10 = Chapter(
    identifier="10",
    title="TITLE",
    fragments=[
        CH10S01
    ]
)
