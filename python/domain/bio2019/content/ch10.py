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


CH10S01 = Section(
    identifier="10.01",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="10.01.01",
            title=u"TITLE",
            text=u"""
Beleid inzake het gebruik van cryptografische beheersmaatregelen Ter bescherming van informatie behoort een beleid voor het gebruik van cryptografische beheersmaatregelen te worden ontwikkeld en geïmplementeerd.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="10.01.01/01",
                    title=u"",
                    text=u"""
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
                    title=u"",
                    text=u"""
Cryptografische toepassingen voldoen aan passende standaarden.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="10.01.02",
            title=u"TITLE",
            text=u"""
Sleutelbeheer;
Met betrekking tot het gebruik, de bescherming en de levensduur van cryptografische sleutels behoort tijdens hun gehele levenscyclus een beleid te worden ontwikkeld en geïmplementeerd. 
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="10.01.02/01",
                    title=u"",
                    text=u"""
Ingeval van PKI-overheid certificaten: hanteer de PKI-Overheid-eisen t.a.v. het sleutelbeheer. In overige situaties: hanteer de standaard ISO-11770 voor het beheer van cryptografische sleutels.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="10.01.02/02",
                    title=u"",
                    text=u"""
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
    title=u"TITLE",
    fragments=[
        CH10S01
    ]
)
