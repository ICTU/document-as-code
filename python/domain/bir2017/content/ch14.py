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
    title=u"",
    fragments=[

        Norm(
            identifier="14.01.01",
            title=u"",
            text=u"Analyse en specificatie van informatiebeveiligingseisen: De eisen die verband houden met informatiebeveiliging behoren te worden opgenomen in de eisen voor nieuwe informatiesystemen of voor uitbreidingen van bestaande informatiesystemen.",
            fragments=[
                Verifier(
                    identifier="14.01.01/01",
                    title=u"",
                    text=u"Bij nieuwe informatiesystemen en bij wijzigingen op bestaande informatiesystemen moet conform het Voorschrift Informatiebeveiliging Rijksdienst artikel 4 een expliciete risicoafweging worden uitgevoerd ten behoeve van het vaststellen van de beveiligingseisen, uitgaande van de BIR.",
                ),
            ],
        ),

        Norm(
            identifier="14.01.02",
            title=u"",
            text=u"Toepassingen op openbare netwerken beveiligen: Informatie die deel uitmaakt van uitvoeringsdiensten en die via openbare netwerken wordt uitgewisseld, behoort te worden beschermd tegen frauduleuze activiteiten, geschillen over contracten en onbevoegde openbaarmaking en wijziging.",
            fragments=[
            ],
        ),

        Norm(
            identifier="14.01.03",
            title=u"",
            text=u"Transacties van toepassingen beschermen: Informatie die deel uitmaakt van transacties van toepassingen behoort te worden beschermd ter voorkoming van onvolledige overdracht, foutieve routering, onbevoegd wijzigen van berichten, onbevoegd openbaar maken, onbevoegd vermenigvuldigen of afspelen.",
            fragments=[
            ],
        ),

    ],
)


S1402 = Section(
    identifier="14.02",
    title=u"",
    fragments=[

        Norm(
            identifier="14.02.01",
            title=u"",
            text=u"Beleid voor beveiligd ontwikkelen: Voor het ontwikkelen van software en systemen behoren regels "
                 u"te worden vastgesteld en op ontwikkelactiviteiten binnen de organisatie te worden toegepast.",
            fragments=[
                Verifier(
                    identifier="14.02.01/01",
                    title=u"",
                    text=u"De gangbare principes rondom Security by design zijn uitgangspunt voor de ontwikkeling "
                         u"van software en systemen",
                ),
            ],
        ),

        Norm(
            identifier="14.02.02",
            title=u"",
            text=u"Procedures voor wijzigingsbeheer met betrekking tot systemen: Wijzigingen aan systemen binnen "
                 u"de levenscyclus van de ontwikkeling behoren te worden beheerst door het gebruik van "
                 u"formele procedures voor wijzigingsbeheer.",
            fragments=[
                Verifier(
                    identifier="14.02.02/01",
                    title=u"",
                    text=u"Voor het wijzigingsbeheer gelden de algemeen geaccepteerde beheerframeworks, "
                         u"zoals ITIL, ASL of BiSL.",
                ),
            ],
        ),

        Norm(
            identifier="14.02.03",
            title=u"",
            text=u"Technische beoordeling van toepassingen na wijzigingen besturingsplatform: Als besturingsplatforms "
                 u"zijn veranderd, behoren bedrijfskritische toepassingen te worden beoordeeld en getest om te "
                 u"waarborgen dat er geen nadelige impact is op de activiteiten of de beveiliging van de organisatie.",
            fragments=[
            ],
        ),

        Norm(
            identifier="14.02.04",
            title=u"",
            text=u"(Vervallen)",
            fragments=[
            ],
        ),

        Norm(
            identifier="14.02.05",
            title=u"",
            text=u"Principes voor engineering van beveiligde systemen: Principes voor de engineering van "
                 u"beveiligde systemen behoren te worden vastgesteld, gedocumenteerd, onderhouden en toegepast voor "
                 u"alle verrichtingen betreffende het implementeren van informatiesystemen.",
            fragments=[
                Verifier(
                    identifier="14.02.05/01",
                    title=u"",
                    text=u"Zie Rijksmaatregel 14.02.01/01",
                ),
            ],
        ),

        Norm(
            identifier="14.02.06",
            title=u"",
            text=u"Beveiligde ontwikkelomgeving: Organisaties behoren beveiligde ontwikkelomgevingen vast te stellen "
                 u"en passend te beveiligen voor verrichtingen op het gebied van systeemontwikkeling en integratie, "
                 u"die betrekking hebben op de gehele levenscyclus van de systeemontwikkeling.",
            fragments=[
                Verifier(
                    identifier="14.02.06/01",
                    title=u"",
                    text=u"Uitgangspunt voor systeemontwikkeltrajecten is een expliciete risicoafweging. Deze heeft "
                         u"zowel de ontwikkelomgeving als ook het te ontwikkelen systeem in scope.",
                ),
            ],
        ),

        Norm(
            identifier="14.02.07",
            title=u"",
            text=u"Uitbestede softwareontwikkeling: Uitbestede systeemontwikkeling behoort onder supervisie te staan "
                 u"van en te worden gemonitord door de organisatie.",
            fragments=[
                Verifier(
                    identifier="14.02.07/01",
                    title=u"",
                    text=u"Een voorwaarde voor uitbestedingstrajecten is een expliciete risicoafweging. "
                         u"De noodzakelijke beveiligingsmaatregelen die daaruit volgen worden aan de leverancier "
                         u"opgelegd.",
                ),
            ],
        ),

        Norm(
            identifier="14.02.08",
            title=u"",
            text=u"Testen van systeembeveiliging: Tijdens ontwikkelactiviteiten behoort de beveiligingsfunctionaliteit "
                 u"te worden getest.",
            fragments=[
            ],
        ),

        Norm(
            identifier="14.02.09",
            title=u"",
            text=u"Systeemacceptatietests: Voor nieuwe informatiesystemen, upgrades en nieuwe versies behoren "
                 u"programma?s voor het uitvoeren van acceptatietests en gerelateerde criteria te worden vastgesteld.",
            fragments=[
                Verifier(
                    identifier="14.02.09/01",
                    title=u"",
                    text=u"Voor acceptatietesten van systemen worden gestructureerde  testmethodieken gebruikt. "
                         u"De testen worden bij voorkeur geautomatiseerd uitgevoerd.",
                ),
                Verifier(
                    identifier="14.02.09/02",
                    title=u"",
                    text=u"Van de resultaten van de testen wordt verslag gemaakt.",
                ),
            ],
        ),

    ],
)


S1403 = Section(
    identifier="14.03",
    title=u"",
    fragments=[

        Norm(
            identifier="14.03.01",
            title=u"",
            text=u"Bescherming van testgegevens: Testgegevens behoren zorgvuldig te worden gekozen, beschermd "
                 u"en gecontroleerd.",
            fragments=[
            ],
        ),

    ],
)


CH14 = Chapter(
    identifier="14",
    title=u"System acquisition, development and maintenance",
    fragments=[
        S1401,
        S1402,
        S1403,
    ]
)
