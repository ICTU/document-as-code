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


CH11S01 = Section(
    identifier="11.01",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="11.01.01",
            title=u"TITLE",
            text=u"""
Fysieke beveiligingszone;
Beveiligingszones behoren te worden gedefinieerd en gebruikt om gebieden te beschermen die gevoelige of essentiële informatie en informatie verwerkende faciliteiten bevatten. 
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.01/01",
                    title=u"",
                    text=u"""
Er wordt voor het inrichten van beveiligde zones gebruik gemaakt van standaarden.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="11.01.02",
            title=u"TITLE",
            text=u"""
Fysieke toegangsbeveiliging;
Beveiligde gebieden behoren te worden beschermd door passende toegangsbeveiliging om ervoor te zorgen dat alleen bevoegd personeel toegang krijgt.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="11.01.02/01",
                    title=u"",
                    text=u"""
In geval van concrete beveiligingsrisico’s worden waarschuwingen, conform onderlinge afspraken, verzonden aan de relevante collega’s binnen het beveiligingsdomein van de overheid.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="11.01.03",
            title=u"TITLE",
            text=u"""
Kantoren, ruimten en faciliteiten beveiligen;
Voor kantoren, ruimten en faciliteiten behoort fysieke beveiliging te worden ontworpen en toegepast.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.03/01",
                    title=u"",
                    text=u"""
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
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="11.02.09",
            title=u"TITLE",
            text=u"""
‘Clear desk’- en ‘clear screen’-beleid;
Er behoort een ‘clear desk’-beleid voor papieren documenten en verwijderbare opslagmedia en een ‘clear screen’-beleid voor informatieverwerkende faciliteiten te worden ingesteld.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="11.02.09/01",
                    title=u"",
                    text=u"""
Een onbeheerde werkplek in een ongecontroleerde omgeving is altijd vergrendeld.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="11.02.09/02",
                    title=u"",
                    text=u"""
Informatie wordt automatisch ontoegankelijk gemaakt met bijvoorbeeld een screensaver na een inactiviteit van maximaal 15 minuten.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="11.02.09/03",
                    title=u"",
                    text=u"""
Sessies op remote desktops worden op het remote platform vergrendeld na 15 minuten. Het overnemen van sessies op remote desktops op een ander client apparaat is alleen mogelijk via dezelfde beveiligde loginprocedure als waarmee de sessie is gecreëerd.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="11.02.09/04",
                    title=u"",
                    text=u"""
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
    title=u"TITLE",
    fragments=[
        CH11S01,
        CH11S02
    ]
)
