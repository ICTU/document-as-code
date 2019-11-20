# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.document.model.chapter import Chapter
from domain.document.model.section import Section
from domain.norm_specification.model.norm import Norm
from domain.norm_specification.model.verifier import Verifier


CH08S01 = Section(
    identifier="08.01",
    title=u"TITLE",
    text=u"text",
    fragments=[
        
    ],
)


CH08S02 = Section(
    identifier="08.02",
    title=u"TITLE",
    text=u"text",
    fragments=[
        
    ],
)


CH08S03 = Section(
    identifier="08.03",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="08.03.01",
            title=u"TITLE",
            text=u"""
Beheer van verwijderbare media;
Voor het beheren van verwijderbare media behoren procedures te worden geïmplementeerd in overeenstemming met het classificatieschema dat door de organisatie is vastgesteld.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.03.01/01",
                    title=u"",
                    text=u"""
Er is een verwijderinstructie waarin is opgenomen dat van herbruikbare media die de organisatie verlaten de onnodige inhoud onherstelbaar verwijderd (ISO27002 – implementatierichtlijn 8.3.1.a).
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="08.03.01/02",
                    title=u"",
                    text=u"""
De wijze waarop vertrouwelijk of hoger geclassificeerde informatie is opgeslagen, voldoet aan de eisen van het NBV.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="08.03.02",
            title=u"TITLE",
            text=u"""
Verwijderen van media;
Media behoren op een veilige en beveiligde manier te worden verwijderd als ze niet langer nodig zijn, overeenkomstig formele procedures.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="08.03.02/01",
                    title=u"",
                    text=u"""
Media die vertrouwelijke informatie bevatten zijn opgeslagen op een plek die niet toegankelijk is voor onbevoegden. Verwijdering vindt plaats op een veilige manier, bijv. door verbranding of versnippering. Verwijdering van alleen gegevens is ook mogelijk door het wissen van de gegevens voordat de media worden gebruikt voor een andere toepassing in de organisatie (ISO27002 – implementatierichtlijn 8.3.2.a)
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="08.03.02/02",
                    title=u"",
                    text=u"""
Voor het wissen van alle data op het medium, wordt de data onherstelbaar verwijderd,
bijvoorbeeld door minimaal twee keer te overschrijven met vaste data en één keer
met random data. Er wordt gecontroleerd of alle data onherstelbaar verwijderd is.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="08.03.03",
            title=u"TITLE",
            text=u"""
Media fysiek overdragen;
Media die informatie bevatten, behoren te worden beschermd tegen onbevoegde toegang, misbruik of corruptie tijdens transport.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="08.03.03/01",
                    title=u"",
                    text=u"""
Er is voor de gehele organisatie beleid voor het fysiek transport van media vastgesteld.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="08.03.03/02",
                    title=u"",
                    text=u"""
Het gebruik van koeriers of transporteurs voor vertrouwelijk of hoger geclassificeerde informatie voldoet aan vooraf opgestelde betrouwbaarheidseisen.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH08 = Chapter(
    identifier="08",
    title=u"TITLE",
    fragments=[
        CH08S01,
        CH08S02,
        CH08S03
    ]
)
