# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S1101 = Section(
    identifier="11.01",
    title="Beveiligde gebieden",
    text="Doelstelling: Onbevoegde fysieke toegang tot, schade aan en interferentie met informatie en "
         "informatieverwerkende faciliteiten van de organisatie voorkomen.",
    fragments=[

        Norm(
            identifier="11.01.01",
            title="Fysieke beveiligingszone",
            text="Beveiligingszones behoren te worden gedefinieerd en gebruikt om gebieden te beschermen die "
                 "gevoelige of essentiële informatie en informatieverwerkende faciliteiten bevatten.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.01/01",
                    title="",
                    text="Er wordt voor het inrichten van beveiligde zones gebruik gemaakt van de volgende "
                         "voorschriften: "
                         "(a) het Kader Rijkstoegangsbeleid (2010); "
                         "(b) het Normenkader Beveiliging Rijkskantoren (NkBR 2015); "
                         "(c) het Beveiligingsvoorschrift Rijk (BVR 2013).",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.01.02",
            title="Fysieke toegangsbeveiliging",
            text="Beveiligde gebieden behoren te worden beschermd door passende toegangsbeveiliging om ervoor "
                 "te zorgen dat alleen bevoegd personeel toegang krijgt.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.02/01",
                    title="",
                    text="In geval van concrete beveiligingsrisico?s worden waarschuwingen, conform onderlinge "
                         "afspraken, verzonden aan de relevante collega?s binnen het beveiligingsdomein van het Rijk.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="11.01.03",
            title="Kantoren, ruimten en faciliteiten beveiligen",
            text="Voor kantoren, ruimten en faciliteiten behoort fysieke beveiliging te worden "
                 "ontworpen en toegepast.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.03/01",
                    title="",
                    text="Sleutelbeheer is ingericht op basis van een sleutelplan (NkBR 5.4).",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.01.04",
            title="Beschermen tegen bedreigingen van buitenaf",
            text="Tegen natuurrampen, kwaadwillige aanvallen of ongelukken behoort fysieke bescherming te worden "
                 "ontworpen en toegepast.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.04/01",
                    title="",
                    text="De organisatie heeft geïnventariseerd welke papieren archieven en apparatuur "
                         "bedrijfskritisch zijn. Tegen bedreigingen van buitenaf zijn beveiligingsmaatregelen "
                         "genomen op basis van een expliciete risicoafweging.",
                    bbn=1,
                ),
                Verifier(
                    identifier="11.01.04/02",
                    title="",
                    text="Bij huisvesting van IT-apparatuur wordt rekening gehouden met de kans op gevolgen van "
                         "rampen veroorzaakt door de natuur en menselijk handelen.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.01.05",
            title="Werken in beveiligde gebieden",
            text="Voor het werken in beveiligde gebieden behoren procedures te worden ontwikkeld en toegepast.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="11.01.05/01",
                    title="",
                    text="- conform norm -",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="11.01.06",
            title="Laad- en loslocatie",
            text="Toegangspunten zoals laad- en loslocaties en andere punten waar onbevoegde personen het terrein "
                 "kunnen betreden, behoren te worden beheerst, en zo mogelijk te worden afgeschermd van "
                 "informatieverwerkende faciliteiten om onbevoegde toegang te vermijden.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.01.06/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1102 = Section(
    identifier="11.02",
    title="Apparatuur",
    text="Doelstelling: Verlies, schade, diefstal of compromittering van bedrijfsmiddelen en onderbreking van de "
         "bedrijfsvoering van de organisatie voorkomen.",
    fragments=[

        Norm(
            identifier="11.02.01",
            title="Plaatsing en bescherming van apparatuur",
            text="Apparatuur behoort zo te worden geplaatst en beschermd dat risico's van bedreigingen en gevaren "
                 "van buitenaf, alsook de kans op onbevoegde toegang worden verkleind.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.02",
            title="Nutsvoorzieningen",
            text="Apparatuur behoort te worden beschermd tegen stroomuitval en andere verstoringen die worden "
                 "veroorzaakt door ontregelingen in nutsvoorzieningen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.02/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.03",
            title="Beveiliging van bekabeling",
            text="Voedings- en telecommunicatiekabels voor het versturen van gegevens of die informatiediensten "
                 "ondersteunen, behoren te worden beschermd tegen interceptie, verstoring of schade.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.03/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.04",
            title="Onderhoud van apparatuur",
            text="Apparatuur behoort correct te worden onderhouden om de continue beschikbaarheid en integriteit "
                 "ervan te waarborgen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.04/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.05",
            title="Verwijdering van bedrijfsmiddelen",
            text="Apparatuur, informatie en software behoren niet van de locatie te worden meegenomen zonder "
                 "voorafgaande goedkeuring.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.05/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.06",
            title="Beveiliging van apparatuur en bedrijfsmiddelen buiten het terrein",
            text="Bedrijfsmiddelen die zich buiten het terrein bevinden, behoren te worden beveiligd, waarbij "
                 "rekening behoort te worden gehouden met de verschillende risico's van werken buiten het terrein "
                 "van de organisatie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.06/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.07",
            title="Veilig verwijderen of hergebruiken van apparatuur",
            text="Alle onderdelen van de apparatuur die opslagmedia bevatten, behoren te worden geverifieerd om te "
                 "waarborgen dat gevoelige gegevens en in licentie gegeven software voorafgaand aan verwijdering of "
                 "hergebruik zijn verwijderd of betrouwbaar veilig zijn overschreven.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.07/01",
                    title="",
                    text="- conform norm - (zie 08.03.02)",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.08",
            title="Onbeheerde gebruikersapparatuur",
            text="Gebruikers moeten ervoor zorgen dat onbeheerde apparatuur voldoende beschermd is.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.08/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="11.02.09",
            title="'Clear desk'- en 'clear screen'-beleid",
            text="Er behoort een 'clear desk'-beleid voor papieren documenten en verwijderbare opslagmedia en een "
                 "'clear screen'-beleid voor informatieverwerkende faciliteiten te worden ingesteld.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="11.02.09/01",
                    title="",
                    text="Een onbeheerde werkplek in een ongecontroleerde omgeving is altijd vergrendeld.",
                    bbn=2,
                ),
                Verifier(
                    identifier="11.02.09/02",
                    title="",
                    text="Informatie wordt automatisch ontoegankelijk gemaakt met bijvoorbeeld een screensaver na een "
                         "inactiviteit van maximaal 15 minuten.",
                    bbn=2,
                ),
                Verifier(
                    identifier="11.02.09/03",
                    title="",
                    text="Sessies op remote desktops worden op het remote platform vergrendeld na 15 minuten. Het "
                         "overnemen van sessies op remote desktops op een ander client apparaat is alleen mogelijk "
                         "via dezelfde beveiligde loginprocedure als waarmee de sessie is gecreëerd.",
                    bbn=2,
                ),
                Verifier(
                    identifier="11.02.09/04",
                    title="",
                    text="Bij het gebruik van een chipcardtoken voor toegang tot systemen wordt bij het verwijderen "
                         "van de token de toegangsbeveiligingslock automatisch geactiveerd.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH11 = Chapter(
    identifier="11",
    title="Fysieke beveiliging en beveiliging van de omgeving",
    fragments=[
        S1101,
        S1102,
    ]
)
