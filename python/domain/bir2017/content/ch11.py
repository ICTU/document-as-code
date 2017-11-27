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

S1101 = Section(
    identifier="11.01",
    title=u"",
    fragments=[

        Norm(
            identifier="11.01.01",
            title=u"",
            text=u"Fysieke beveiligingszone: Beveiligingszones behoren te worden gedefinieerd en gebruikt om gebieden te beschermen die gevoelige of essentiële informatie en informatieverwerkende faciliteiten bevatten.",
            fragments=[
                Verifier(
                    identifier="11.01.01/01",
                    title=u"",
                    text=u"Er wordt voor het inrichten van beveiligde zones gebruik gemaakt van de volgende voorschriften: (a) het Kader Rijkstoegangsbeleid (2010); (b) het Normenkader Beveiliging Rijkskantoren (NkBR 2015); (c) het Beveiligingsvoorschrift Rijk (BVR 2013).",
                ),
            ],
        ),

        Norm(
            identifier="11.01.02",
            title=u"",
            text=u"Fysieke toegangsbeveiliging: Beveiligde gebieden behoren te worden beschermd door passende toegangsbeveiliging om ervoor te zorgen dat alleen bevoegd personeel toegang krijgt.",
            fragments=[
                Verifier(
                    identifier="11.01.02/01",
                    title=u"",
                    text=u"In geval van concrete beveiligingsrisico?s worden waarschuwingen, conform onderlinge afspraken, verzonden aan de relevante collega?s binnen het beveiligingsdomein van het Rijk.",
                ),
            ],
        ),

        Norm(
            identifier="11.01.03",
            title=u"",
            text=u"Kantoren, ruimten en faciliteiten beveiligen: Voor kantoren, ruimten en faciliteiten behoort fysieke beveiliging te worden ontworpen en toegepast.",
            fragments=[
                Verifier(
                    identifier="11.01.03/01",
                    title=u"",
                    text=u"Sleutelbeheer is ingericht op basis van een sleutelplan (NkBR 5.4).",
                ),
            ],
        ),

        Norm(
            identifier="11.01.04",
            title=u"",
            text=u"Beschermen tegen bedreigingen van buitenaf: Tegen natuurrampen, kwaadwillige aanvallen of ongelukken behoort fysieke bescherming te worden ontworpen en toegepast.",
            fragments=[
                Verifier(
                    identifier="11.01.04/01",
                    title=u"",
                    text=u"De organisatie heeft geïnventariseerd welke papieren archieven en apparatuur bedrijfskritisch zijn. Tegen bedreigingen van buitenaf zijn beveiligingsmaatregelen genomen op basis van een expliciete risicoafweging.",
                ),
                Verifier(
                    identifier="11.01.04/02",
                    title=u"",
                    text=u"Bij huisvesting van IT-apparatuur wordt rekening gehouden met de kans op gevolgen van rampen veroorzaakt door de natuur en menselijk handelen.",
                ),
            ],
        ),

        Norm(
            identifier="11.01.05",
            title=u"",
            text=u"Werken in beveiligde gebieden: Voor het werken in beveiligde gebieden behoren procedures te worden ontwikkeld en toegepast.",
            fragments=[
            ],
        ),

        Norm(
            identifier="11.01.06",
            title=u"",
            text=u"Laad- en loslocatie: Toegangspunten zoals laad- en loslocaties en andere punten waar onbevoegde personen het terrein kunnen betreden, behoren te worden beheerst, en zo mogelijk te worden afgeschermd van informatieverwerkende faciliteiten om onbevoegde toegang te vermijden.",
            fragments=[
            ],
        ),

    ],
)


S1102 = Section(
    identifier="11.02",
    title=u"",
    fragments=[

        Norm(
            identifier="11.02.01",
            title=u"",
            text=u"Plaatsing en bescherming van apparatuur: Apparatuur behoort zo te worden geplaatst en beschermd dat risico?s van bedreigingen en gevaren van buitenaf, alsook de kans op onbevoegde toegang worden verkleind.",
            fragments=[
            ],
        ),

        Norm(
            identifier="11.02.02",
            title=u"",
            text=u"Nutsvoorzieningen: Apparatuur behoort te worden beschermd tegen stroomuitval en andere verstoringen die worden veroorzaakt door ontregelingen in nutsvoorzieningen.",
            fragments=[
            ],
        ),

        Norm(
            identifier="11.02.03",
            title=u"",
            text=u"Beveiliging van bekabeling: Voedings- en telecommunicatiekabels voor het versturen van gegevens of die informatiediensten ondersteunen, behoren te worden beschermd tegen interceptie, verstoring of schade.",
            fragments=[
            ],
        ),

        Norm(
            identifier="11.02.04",
            title=u"",
            text=u"Onderhoud van apparatuur: Apparatuur behoort correct te worden onderhouden om de continue beschikbaarheid en integriteit ervan te waarborgen.",
            fragments=[
            ],
        ),

        Norm(
            identifier="11.02.05",
            title=u"",
            text=u"Verwijdering van bedrijfsmiddelen: Apparatuur, informatie en software behoren niet van de locatie te worden meegenomen zonder voorafgaande goedkeuring.",
            fragments=[
            ],
        ),

        Norm(
            identifier="11.02.06",
            title=u"",
            text=u"Beveiliging van apparatuur en bedrijfsmiddelen buiten het terrein: Bedrijfsmiddelen die zich buiten het terrein bevinden, behoren te worden beveiligd, waarbij rekening behoort te worden gehouden met de verschillende risico?s van werken buiten het terrein van de organisatie.",
            fragments=[
            ],
        ),

        Norm(
            identifier="11.02.07",
            title=u"",
            text=u"Veilig verwijderen of hergebruiken van apparatuur: Alle onderdelen van de apparatuur die opslagmedia bevatten, behoren te worden geverifieerd om te waarborgen dat gevoelige gegevens en in licentie gegeven software voorafgaand aan verwijdering of hergebruik zijn verwijderd of betrouwbaar veilig zijn overschreven.",
            fragments=[
            ],
        ),

        Norm(
            identifier="11.02.08",
            title=u"",
            text=u"Onbeheerde gebruikersapparatuur: Gebruikers moeten ervoor zorgen dat onbeheerde apparatuur voldoende beschermd is.",
            fragments=[
            ],
        ),

        Norm(
            identifier="11.02.09",
            title=u"",
            text=u"?Clear desk?- en ?clear screen?-beleid: Er behoort een ?clear desk?-beleid voor papieren documenten en verwijderbare opslagmedia en een ?clear screen?-beleid voor informatieverwerkende faciliteiten te worden ingesteld.",
            fragments=[
                Verifier(
                    identifier="11.02.09/01",
                    title=u"",
                    text=u"Een onbeheerde werkplek in een ongecontroleerde omgeving is altijd vergrendeld.",
                ),
                Verifier(
                    identifier="11.02.09/02",
                    title=u"",
                    text=u"Informatie wordt automatisch ontoegankelijk gemaakt met bijvoorbeeld een screensaver na een inactiviteit van maximaal 15 minuten.",
                ),
                Verifier(
                    identifier="11.02.09/03",
                    title=u"",
                    text=u"Sessies op remote desktops worden op het remote platform vergrendeld na 15 minuten. Het overnemen van sessies op remote desktops op een ander client apparaat is alleen mogelijk via dezelfde beveiligde loginprocedure als waarmee de sessie is gecreëerd.",
                ),
                Verifier(
                    identifier="11.02.09/04",
                    title=u"",
                    text=u"Bij het gebruik van een chipcardtoken voor toegang tot systemen wordt bij het verwijderen van de token de toegangsbeveiligingslock automatisch geactiveerd.",
                ),
            ],
        ),

    ],
)


CH11 = Chapter(
    identifier="11",
    title=u"",
    fragments=[
        S1101,
        S1102,
    ]
)
