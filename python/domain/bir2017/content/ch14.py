# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S1401 = Section(
    identifier="14.01",
    title="Beveiligingseisen voor informatiesystemen",
    text="Doelstelling: Waarborgen dat informatiebeveiliging integraal  deel uitmaakt van informatiesystemen in de "
         "gehele levenscyclus. Hiertoe behoren ook de eisen voor informatiesystemen die diensten verlenen via "
         "openbare netwerken.",
    fragments=[

        Norm(
            identifier="14.01.01",
            title="Analyse en specificatie van informatiebeveiligingseisen",
            text="De eisen die verband houden met informatiebeveiliging behoren te worden opgenomen in de eisen voor "
                 "nieuwe informatiesystemen of voor uitbreidingen van bestaande informatiesystemen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.01.01/01",
                    title="",
                    text="Bij nieuwe informatiesystemen en bij wijzigingen op bestaande informatiesystemen moet "
                         "conform het Voorschrift Informatiebeveiliging Rijksdienst artikel 4 een expliciete "
                         "risicoafweging worden uitgevoerd ten behoeve van het vaststellen van de beveiligingseisen, "
                         "uitgaande van de BIR.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.01.02",
            title="Toepassingen op openbare netwerken beveiligen",
            text="Informatie die deel uitmaakt van uitvoeringsdiensten "
                 "en die via openbare netwerken wordt uitgewisseld, behoort te worden beschermd tegen frauduleuze "
                 "activiteiten, geschillen over contracten en onbevoegde openbaarmaking en wijziging.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.01.02/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.01.03",
            title="Transacties van toepassingen beschermen",
            text="Informatie die deel uitmaakt van transacties van toepassingen behoort te worden beschermd ter "
                 "voorkoming van onvolledige overdracht, foutieve routering, onbevoegd wijzigen van berichten, "
                 "onbevoegd openbaar maken, onbevoegd vermenigvuldigen of afspelen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.01.03/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1402 = Section(
    identifier="14.02",
    title="Beveiliging in ontwikkelings- en ondersteunende processen",
    text="Doelstelling: Bewerkstelligen dat informatiebeveiliging wordt ontworpen en geïmplementeerd binnen de "
         "ontwikkelingslevenscyclus van informatiesystemen.",
    fragments=[

        Norm(
            identifier="14.02.01",
            title="Beleid voor beveiligd ontwikkelen",
            text="Voor het ontwikkelen van software en systemen behoren regels te worden vastgesteld en op "
                 "ontwikkelactiviteiten binnen de organisatie te worden toegepast.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.01/01",
                    title="",
                    text="De gangbare principes rondom Security by design zijn uitgangspunt voor de ontwikkeling "
                         "van software en systemen",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.02.02",
            title="Procedures voor wijzigingsbeheer met betrekking tot systemen",
            text="Wijzigingen aan systemen binnen de levenscyclus van de ontwikkeling behoren te worden beheerst door "
                 "het gebruik van formele procedures voor wijzigingsbeheer.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.02/01",
                    title="",
                    text="Voor het wijzigingsbeheer gelden de algemeen geaccepteerde beheerframeworks, "
                         "zoals ITIL, ASL of BiSL.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.02.03",
            title="Technische beoordeling van toepassingen na wijzigingen besturingsplatform",
            text="Als besturingsplatforms zijn veranderd, behoren bedrijfskritische toepassingen te worden beoordeeld "
                 "en getest om te waarborgen dat er geen nadelige impact is op de activiteiten of de beveiliging van "
                 "de organisatie.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="14.02.03/01",
                    title="",
                    text="- conform norm -",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="14.02.04",
            title=" ",
            text="(Vervallen)",
            fragments=[
            ],
        ),

        Norm(
            identifier="14.02.05",
            title="Principes voor engineering van beveiligde systemen",
            text="Principes voor de engineering van beveiligde systemen behoren te worden vastgesteld, "
                 "gedocumenteerd, onderhouden en toegepast voor alle verrichtingen betreffende het implementeren van "
                 "informatiesystemen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.05/01",
                    title="",
                    text="Zie Rijksmaatregel 14.02.01/01",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.02.06",
            title="Beveiligde ontwikkelomgeving",
            text="Organisaties behoren beveiligde ontwikkelomgevingen vast te stellen en passend te beveiligen voor "
                 "verrichtingen op het gebied van systeemontwikkeling en integratie, die betrekking hebben op de "
                 "gehele levenscyclus van de systeemontwikkeling.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.06/01",
                    title="",
                    text="Uitgangspunt voor systeemontwikkeltrajecten is een expliciete risicoafweging. Deze heeft "
                         "zowel de ontwikkelomgeving als ook het te ontwikkelen systeem in scope.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.02.07",
            title="Uitbestede softwareontwikkeling",
            text="Uitbestede systeemontwikkeling behoort onder supervisie te staan van en te worden gemonitord door "
                 "de organisatie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.07/01",
                    title="",
                    text="Een voorwaarde voor uitbestedingstrajecten is een expliciete risicoafweging. "
                         "De noodzakelijke beveiligingsmaatregelen die daaruit volgen worden aan de leverancier "
                         "opgelegd.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.02.08",
            title="Testen van systeembeveiliging",
            text="Tijdens ontwikkelactiviteiten behoort de beveiligingsfunctionaliteit te worden getest.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.08/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.02.09",
            title="Systeemacceptatietests",
            text="Voor nieuwe informatiesystemen, upgrades en nieuwe versies behoren programma's voor het uitvoeren "
                 "van acceptatietests en gerelateerde criteria te worden vastgesteld.",
            fragments=[
                Verifier(
                    identifier="14.02.09/01",
                    title="",
                    text="Voor acceptatietesten van systemen worden gestructureerde  testmethodieken gebruikt. "
                         "De testen worden bij voorkeur geautomatiseerd uitgevoerd.",
                    bbn=1,
                ),
                Verifier(
                    identifier="14.02.09/02",
                    title="",
                    text="Van de resultaten van de testen wordt verslag gemaakt.",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1403 = Section(
    identifier="14.03",
    title="Testgegevens",
    text="Doelstelling: Bescherming waarborgen van gegevens die voor het testen zijn gebruikt.",
    fragments=[

        Norm(
            identifier="14.03.01",
            title="Bescherming van testgegevens",
            text="Testgegevens behoren zorgvuldig te worden gekozen, beschermd en gecontroleerd.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="14.03.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH14 = Chapter(
    identifier="14",
    title="Acquisitie, ontwikkeling en onderhoud van informatiesystemen",
    fragments=[
        S1401,
        S1402,
        S1403,
    ]
)
