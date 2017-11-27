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

S1001 = Section(
    identifier="10.01",
    title=u"",
    fragments=[

        Norm(
            identifier="10.01.01",
            title=u"",
            text=u"Beleid inzake het gebruik van cryptografische beheersmaatregelen: Ter bescherming van informatie "
                 u"behoort een beleid voor het gebruik van cryptografische beheersmaatregelen te worden ontwikkeld en "
                 u"geïmplementeerd.",
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
                ),
                Verifier(
                    identifier="10.01.01/02",
                    title=u"",
                    text=u"Crypografische toepassingen voldoen aan passende standaarden.",
                ),
            ],
        ),

        Norm(
            identifier="10.01.02",
            title=u"",
            text=u"Sleutelbeheer: Met betrekking tot het gebruik, de bescherming en de levensduur van cryptografische "
                 u"sleutels behoort tijdens hun gehele levenscyclus een beleid te worden ontwikkeld en geïmplementeerd.",
            fragments=[
                Verifier(
                    identifier="10.01.02/01",
                    title=u"",
                    text=u"Ingeval van PKI-overheid certificaten: hanteer de PKI-Overheid-eisen t.a.v. het "
                         u"sleutelbeheer. In overige situaties: hanteer de standaard ISO-11770 voor het beheer van "
                         u"cryptografische sleutels.",
                ),
                Verifier(
                    identifier="10.01.02/02",
                    title=u"",
                    text=u"Er zijn (contractuele) afspraken over reservecertificaten van een alternatieve leverancier "
                         u"als uit risicoafweging blijkt dat deze noodzakelijk zijn.",
                ),
            ],
        ),

    ],
)


CH10 = Chapter(
    identifier="10",
    title=u"Cryptography",
    fragments=[
        S1001,
    ]
)
