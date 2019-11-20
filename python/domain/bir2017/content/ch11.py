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


S1101 = Section(
    identifier="11.01",
    title=u"Beveiligde gebieden",
    text=u"Doelstelling: Onbevoegde fysieke toegang tot, schade aan en interferentie met informatie en "
         u"informatieverwerkende faciliteiten van de organisatie voorkomen.",
    fragments=[

        Norm(
            identifier="11.01.01",
            title=u"Fysieke beveiligingszone",
            text=u"Beveiligingszones behoren te worden gedefinieerd en gebruikt om gebieden te beschermen die "
                 u"gevoelige of essentiële informatie en informatieverwerkende faciliteiten bevatten.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.01/01",
                    title=u"",
                    text=u"Er wordt voor het inrichten van beveiligde zones gebruik gemaakt van de volgende "
                         u"voorschriften: "
                         u"(a) het Kader Rijkstoegangsbeleid (2010); "
                         u"(b) het Normenkader Beveiliging Rijkskantoren (NkBR 2015); "
                         u"(c) het Beveiligingsvoorschrift Rijk (BVR 2013).",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.01.02",
            title=u"Fysieke toegangsbeveiliging",
            text=u"Beveiligde gebieden behoren te worden beschermd door passende toegangsbeveiliging om ervoor "
                 u"te zorgen dat alleen bevoegd personeel toegang krijgt.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.02/01",
                    title=u"",
                    text=u"In geval van concrete beveiligingsrisico?s worden waarschuwingen, conform onderlinge "
                         u"afspraken, verzonden aan de relevante collega?s binnen het beveiligingsdomein van het Rijk.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="11.01.03",
            title=u"Kantoren, ruimten en faciliteiten beveiligen",
            text=u"Voor kantoren, ruimten en faciliteiten behoort fysieke beveiliging te worden "
                 u"ontworpen en toegepast.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.03/01",
                    title=u"",
                    text=u"Sleutelbeheer is ingericht op basis van een sleutelplan (NkBR 5.4).",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.01.04",
            title=u"Beschermen tegen bedreigingen van buitenaf",
            text=u"Tegen natuurrampen, kwaadwillige aanvallen of ongelukken behoort fysieke bescherming te worden "
                 u"ontworpen en toegepast.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.04/01",
                    title=u"",
                    text=u"De organisatie heeft geïnventariseerd welke papieren archieven en apparatuur "
                         u"bedrijfskritisch zijn. Tegen bedreigingen van buitenaf zijn beveiligingsmaatregelen "
                         u"genomen op basis van een expliciete risicoafweging.",
                    bbn=1,
                ),
                Verifier(
                    identifier="11.01.04/02",
                    title=u"",
                    text=u"Bij huisvesting van IT-apparatuur wordt rekening gehouden met de kans op gevolgen van "
                         u"rampen veroorzaakt door de natuur en menselijk handelen.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.01.05",
            title=u"Werken in beveiligde gebieden",
            text=u"Voor het werken in beveiligde gebieden behoren procedures te worden ontwikkeld en toegepast.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="11.01.05/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="11.01.06",
            title=u"Laad- en loslocatie",
            text=u"Toegangspunten zoals laad- en loslocaties en andere punten waar onbevoegde personen het terrein "
                 u"kunnen betreden, behoren te worden beheerst, en zo mogelijk te worden afgeschermd van "
                 u"informatieverwerkende faciliteiten om onbevoegde toegang te vermijden.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.06/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1102 = Section(
    identifier="11.02",
    title=u"Apparatuur",
    text=u"Doelstelling: Verlies, schade, diefstal of compromittering van bedrijfsmiddelen en onderbreking van de "
         u"bedrijfsvoering van de organisatie voorkomen.",
    fragments=[

        Norm(
            identifier="11.02.01",
            title=u"Plaatsing en bescherming van apparatuur",
            text=u"Apparatuur behoort zo te worden geplaatst en beschermd dat risico's van bedreigingen en gevaren "
                 u"van buitenaf, alsook de kans op onbevoegde toegang worden verkleind.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.02",
            title=u"Nutsvoorzieningen",
            text=u"Apparatuur behoort te worden beschermd tegen stroomuitval en andere verstoringen die worden "
                 u"veroorzaakt door ontregelingen in nutsvoorzieningen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.02/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.03",
            title=u"Beveiliging van bekabeling",
            text=u"Voedings- en telecommunicatiekabels voor het versturen van gegevens of die informatiediensten "
                 u"ondersteunen, behoren te worden beschermd tegen interceptie, verstoring of schade.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.03/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.04",
            title=u"Onderhoud van apparatuur",
            text=u"Apparatuur behoort correct te worden onderhouden om de continue beschikbaarheid en integriteit "
                 u"ervan te waarborgen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.04/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.05",
            title=u"Verwijdering van bedrijfsmiddelen",
            text=u"Apparatuur, informatie en software behoren niet van de locatie te worden meegenomen zonder "
                 u"voorafgaande goedkeuring.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.05/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.06",
            title=u"Beveiliging van apparatuur en bedrijfsmiddelen buiten het terrein",
            text=u"Bedrijfsmiddelen die zich buiten het terrein bevinden, behoren te worden beveiligd, waarbij "
                 u"rekening behoort te worden gehouden met de verschillende risico's van werken buiten het terrein "
                 u"van de organisatie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.06/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.07",
            title=u"Veilig verwijderen of hergebruiken van apparatuur",
            text=u"Alle onderdelen van de apparatuur die opslagmedia bevatten, behoren te worden geverifieerd om te "
                 u"waarborgen dat gevoelige gegevens en in licentie gegeven software voorafgaand aan verwijdering of "
                 u"hergebruik zijn verwijderd of betrouwbaar veilig zijn overschreven.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.07/01",
                    title=u"",
                    text=u"- conform norm - (zie 08.03.02)",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.08",
            title=u"Onbeheerde gebruikersapparatuur",
            text=u"Gebruikers moeten ervoor zorgen dat onbeheerde apparatuur voldoende beschermd is.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.08/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.09",
            title=u"'Clear desk'- en 'clear screen'-beleid",
            text=u"Er behoort een 'clear desk'-beleid voor papieren documenten en verwijderbare opslagmedia en een "
                 u"'clear screen'-beleid voor informatieverwerkende faciliteiten te worden ingesteld.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.09/01",
                    title=u"",
                    text=u"Een onbeheerde werkplek in een ongecontroleerde omgeving is altijd vergrendeld.",
                    bbn=2,
                ),
                Verifier(
                    identifier="11.02.09/02",
                    title=u"",
                    text=u"Informatie wordt automatisch ontoegankelijk gemaakt met bijvoorbeeld een screensaver na een "
                         u"inactiviteit van maximaal 15 minuten.",
                    bbn=2,
                ),
                Verifier(
                    identifier="11.02.09/03",
                    title=u"",
                    text=u"Sessies op remote desktops worden op het remote platform vergrendeld na 15 minuten. Het "
                         u"overnemen van sessies op remote desktops op een ander client apparaat is alleen mogelijk "
                         u"via dezelfde beveiligde loginprocedure als waarmee de sessie is gecreëerd.",
                    bbn=2,
                ),
                Verifier(
                    identifier="11.02.09/04",
                    title=u"",
                    text=u"Bij het gebruik van een chipcardtoken voor toegang tot systemen wordt bij het verwijderen "
                         u"van de token de toegangsbeveiligingslock automatisch geactiveerd.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH11 = Chapter(
    identifier="11",
    title=u"Fysieke beveiliging en beveiliging van de omgeving",
    fragments=[
        S1101,
        S1102,
    ]
)
