"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH14S01 = Section(
    identifier="14.01",
    title="TITLE",
    text="text",
    fragments=[
        
    ],
)


CH14S02 = Section(
    identifier="14.02",
    title="TITLE",
    text="text",
    fragments=[
        Norm(
            identifier="14.02.01",
            title="TITLE",
            text="""
Beleid voor beveiligd ontwikkelen;
Voor het ontwikkelen van software en systemen behoren regels te worden vastgesteld en op ontwikkelactiviteiten binnen de organisatie te worden toegepast.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.01/01",
                    title="",
                    text="""
De gangbare principes rondom Security by design zijn uitgangspunt voor de ontwikkeling van software en systemen
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="14.02.02",
            title="TITLE",
            text="""
Procedures voor wijzigingsbeheer met betrekking tot systemen;
Wijzigingen aan systemen binnen de levenscyclus van de ontwikkeling behoren te worden beheerst door het gebruik van formele procedures voor wijzigingsbeheer.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.02/01",
                    title="",
                    text="""
Voor het wijzigingsbeheer gelden de algemeen geaccepteerde beheerframeworks, zoals ITIL, ASL of BiSL.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="14.02.05",
            title="TITLE",
            text="""
Principes voor engineering van beveiligde systemen;
Principes voor de engineering van beveiligde systemen behoren te worden vastgesteld, gedocumenteerd, onderhouden en toegepast voor alle verrichtingen betreffende het implementeren van informatiesystemen.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.05/01",
                    title="",
                    text="""
Zie overheidsmaatregel 14.2.1.1 
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="14.02.06",
            title="TITLE",
            text="""
Beveiligde ontwikkelomgeving;
Organisaties behoren beveiligde ontwikkelomgevingen vast te stellen en passend te beveiligen voor verrichtingen op het gebied van systeemontwikkeling en integratie, die betrekking hebben op de gehele levenscyclus van de systeemontwikkeling.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.06/01",
                    title="",
                    text="""
Uitgangspunt voor systeemontwikkeling trajecten is een expliciete risicoafweging.
Deze heeft zowel de ontwikkelomgeving als ook het te ontwikkelen systeem in scope.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="14.02.07",
            title="TITLE",
            text="""
Uitbestede softwareontwikkeling;
Uitbestede systeemontwikkeling behoort onder supervisie te staan van en te worden gemonitord door de organisatie.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.07/01",
                    title="",
                    text="""
Een voorwaarde voor uitbestedingstrajecten is een expliciete risicoafweging. De noodzakelijke beveiligingsmaatregelen die daaruit volgen worden aan de leverancier opgelegd.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="14.02.09",
            title="TITLE",
            text="""
Systeemacceptatietests;
Voor nieuwe informatiesystemen, upgrades en nieuwe versies behoren programmaâs voor het uitvoeren van acceptatietests en gerelateerde criteria te worden vastgesteld.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.09/01",
                    title="",
                    text="""
Voor acceptatietesten van systemen worden gestructureerde testmethodieken gebruikt. De testen worden bij voorkeur geautomatiseerd uitgevoerd.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="14.02.09/02",
                    title="",
                    text="""
Van de resultaten van de testen wordt verslag gemaakt.
                    """,
                    bbn=1,
                )
            ],
        )
    ],
)


CH14 = Chapter(
    identifier="14",
    title="TITLE",
    fragments=[
        CH14S01,
        CH14S02
    ]
)
