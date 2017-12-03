# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function

from domain.bir.model.norm import Norm
from domain.bir.model.verifier import Verifier
from domain.document.model.chapter import Chapter
from domain.document.model.section import Section

S1401 = Section(
    identifier="14.01",
    title=u"Beveiligingseisen voor informatiesystemen",
    text=u"Doelstelling: Waarborgen dat informatiebeveiliging integraal  deel uitmaakt van informatiesystemen in de "
         u"gehele levenscyclus. Hiertoe behoren ook de eisen voor informatiesystemen die diensten verlenen via "
         u"openbare netwerken.",
    fragments=[

        Norm(
            identifier="14.01.01",
            title=u"Analyse en specificatie van informatiebeveiligingseisen",
            text=u"De eisen die verband houden met informatiebeveiliging behoren te worden opgenomen in de eisen voor "
                 u"nieuwe informatiesystemen of voor uitbreidingen van bestaande informatiesystemen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.01.01/01",
                    title=u"",
                    text=u"Bij nieuwe informatiesystemen en bij wijzigingen op bestaande informatiesystemen moet "
                         u"conform het Voorschrift Informatiebeveiliging Rijksdienst artikel 4 een expliciete "
                         u"risicoafweging worden uitgevoerd ten behoeve van het vaststellen van de beveiligingseisen, "
                         u"uitgaande van de BIR.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.01.02",
            title=u"Toepassingen op openbare netwerken beveiligen",
            text=u"Informatie die deel uitmaakt van uitvoeringsdiensten "
                 u"en die via openbare netwerken wordt uitgewisseld, behoort te worden beschermd tegen frauduleuze "
                 u"activiteiten, geschillen over contracten en onbevoegde openbaarmaking en wijziging.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.01.02/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.01.03",
            title=u"Transacties van toepassingen beschermen",
            text=u"Informatie die deel uitmaakt van transacties van toepassingen behoort te worden beschermd ter "
                 u"voorkoming van onvolledige overdracht, foutieve routering, onbevoegd wijzigen van berichten, "
                 u"onbevoegd openbaar maken, onbevoegd vermenigvuldigen of afspelen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.01.03/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1402 = Section(
    identifier="14.02",
    title=u"Beveiliging in ontwikkelings- en ondersteunende processen",
    text=u"Doelstelling: Bewerkstelligen dat informatiebeveiliging wordt ontworpen en geïmplementeerd binnen de "
         u"ontwikkelingslevenscyclus van informatiesystemen.",
    fragments=[

        Norm(
            identifier="14.02.01",
            title=u"Beleid voor beveiligd ontwikkelen",
            text=u"Voor het ontwikkelen van software en systemen behoren regels te worden vastgesteld en op "
                 u"ontwikkelactiviteiten binnen de organisatie te worden toegepast.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.01/01",
                    title=u"",
                    text=u"De gangbare principes rondom Security by design zijn uitgangspunt voor de ontwikkeling "
                         u"van software en systemen",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.02.02",
            title=u"Procedures voor wijzigingsbeheer met betrekking tot systemen",
            text=u"Wijzigingen aan systemen binnen de levenscyclus van de ontwikkeling behoren te worden beheerst door "
                 u"het gebruik van formele procedures voor wijzigingsbeheer.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.02/01",
                    title=u"",
                    text=u"Voor het wijzigingsbeheer gelden de algemeen geaccepteerde beheerframeworks, "
                         u"zoals ITIL, ASL of BiSL.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.02.03",
            title=u"Technische beoordeling van toepassingen na wijzigingen besturingsplatform",
            text=u"Als besturingsplatforms zijn veranderd, behoren bedrijfskritische toepassingen te worden beoordeeld "
                 u"en getest om te waarborgen dat er geen nadelige impact is op de activiteiten of de beveiliging van "
                 u"de organisatie.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="14.02.03/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="14.02.04",
            title=u" ",
            text=u"(Vervallen)",
            fragments=[
            ],
        ),

        Norm(
            identifier="14.02.05",
            title=u"Principes voor engineering van beveiligde systemen",
            text=u"Principes voor de engineering van beveiligde systemen behoren te worden vastgesteld, "
                 u"gedocumenteerd, onderhouden en toegepast voor alle verrichtingen betreffende het implementeren van "
                 u"informatiesystemen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.05/01",
                    title=u"",
                    text=u"Zie Rijksmaatregel 14.02.01/01",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.02.06",
            title=u"Beveiligde ontwikkelomgeving",
            text=u"Organisaties behoren beveiligde ontwikkelomgevingen vast te stellen en passend te beveiligen voor "
                 u"verrichtingen op het gebied van systeemontwikkeling en integratie, die betrekking hebben op de "
                 u"gehele levenscyclus van de systeemontwikkeling.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.06/01",
                    title=u"",
                    text=u"Uitgangspunt voor systeemontwikkeltrajecten is een expliciete risicoafweging. Deze heeft "
                         u"zowel de ontwikkelomgeving als ook het te ontwikkelen systeem in scope.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.02.07",
            title=u"Uitbestede softwareontwikkeling",
            text=u"Uitbestede systeemontwikkeling behoort onder supervisie te staan van en te worden gemonitord door "
                 u"de organisatie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.07/01",
                    title=u"",
                    text=u"Een voorwaarde voor uitbestedingstrajecten is een expliciete risicoafweging. "
                         u"De noodzakelijke beveiligingsmaatregelen die daaruit volgen worden aan de leverancier "
                         u"opgelegd.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.02.08",
            title=u"Testen van systeembeveiliging",
            text=u"Tijdens ontwikkelactiviteiten behoort de beveiligingsfunctionaliteit te worden getest.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="14.02.08/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="14.02.09",
            title=u"Systeemacceptatietests",
            text=u"Voor nieuwe informatiesystemen, upgrades en nieuwe versies behoren programma's voor het uitvoeren "
                 u"van acceptatietests en gerelateerde criteria te worden vastgesteld.",
            fragments=[
                Verifier(
                    identifier="14.02.09/01",
                    title=u"",
                    text=u"Voor acceptatietesten van systemen worden gestructureerde  testmethodieken gebruikt. "
                         u"De testen worden bij voorkeur geautomatiseerd uitgevoerd.",
                    bbn=1,
                ),
                Verifier(
                    identifier="14.02.09/02",
                    title=u"",
                    text=u"Van de resultaten van de testen wordt verslag gemaakt.",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1403 = Section(
    identifier="14.03",
    title=u"Testgegevens",
    text=u"Doelstelling: Bescherming waarborgen van gegevens die voor het testen zijn gebruikt.",
    fragments=[

        Norm(
            identifier="14.03.01",
            title=u"Bescherming van testgegevens",
            text=u"Testgegevens behoren zorgvuldig te worden gekozen, beschermd en gecontroleerd.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="14.03.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH14 = Chapter(
    identifier="14",
    title=u"Acquisitie, ontwikkeling en onderhoud van informatiesystemen",
    fragments=[
        S1401,
        S1402,
        S1403,
    ]
)
