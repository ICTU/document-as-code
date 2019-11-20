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


S1001 = Section(
    identifier="10.01",
    title=u"Cryptografsche beheersmaatregelen",
    text=u"Doelstelling: Zorgen voor correct en doeltreffend gebruik van cryptografie om de verrtrouwelijkheid, "
         u"authenticiteit en/of integriteit van informatie te beschermen.",
    fragments=[

        Norm(
            identifier="10.01.01",
            title=u"Beleid inzake het gebruik van cryptografische beheersmaatregelen",
            text=u"Ter bescherming van informatie behoort een beleid voor het gebruik van cryptografische "
                 u"beheersmaatregelen te worden ontwikkeld en geïmplementeerd.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="10.01.01/01",
                    title=u"",
                    text=u"In het cryptografiebeleid zijn minimaal de volgende onderwerpen uitgewerkt: "
                         u"(a) wanneer cryptografie ingezet wordt; "
                         u"(b) wie verantwoordelijk is voor de implementatie; "
                         u"(c) wie verantwoordelijk is voor het sleutelbeheer; "
                         u"(d) welke normen als basis dienen voor cryptografie en de wijze waarop de normen van het "
                         u"forum standaardisatie worden toegepast; "
                         u"(e) de wijze waarop het beschermingsniveau vastgesteld wordt; "
                         u"(f) bij interdepartementale communicatie wordt het beleid centraal vastgesteld.",
                    bbn=2,
                ),
                Verifier(
                    identifier="10.01.01/02",
                    title=u"",
                    text=u"Crypografische toepassingen voldoen aan passende standaarden.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="10.01.02",
            title=u"Sleutelbeheer",
            text=u"Met betrekking tot het gebruik, de bescherming en de levensduur van cryptografische sleutels "
                 u"behoort tijdens hun gehele levenscyclus een beleid te worden ontwikkeld en geïmplementeerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="10.01.02/01",
                    title=u"",
                    text=u"Ingeval van PKI-overheid certificaten: hanteer de PKI-Overheid-eisen t.a.v. het "
                         u"sleutelbeheer. In overige situaties: hanteer de standaard ISO-11770 voor het beheer van "
                         u"cryptografische sleutels.",
                    bbn=2,
                ),
                Verifier(
                    identifier="10.01.02/02",
                    title=u"",
                    text=u"Er zijn (contractuele) afspraken over reservecertificaten van een alternatieve leverancier "
                         u"als uit risicoafweging blijkt dat deze noodzakelijk zijn.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH10 = Chapter(
    identifier="10",
    title=u"Cryptografie",
    fragments=[
        S1001,
    ]
)
