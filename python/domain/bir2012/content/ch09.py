# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function

from domain.bir2012.model.norm import Norm
from domain.bir2012.model.verifier import Verifier
from domain.document.model.chapter import Chapter
from domain.document.model.section import Section

S0901 = Section(
    identifier="09.01",
    title=u"Beveiligde ruimten",
    fragments=[
        Norm(
            identifier="09.01.01",
            title=u"Fysieke beveiliging van de omgeving",
            text=u"""Er behoren toegangsbeveiligingen (barrières zoals muren, toegangspoorten met kaartsloten of een bemande receptie) te worden aangebracht om ruimten te beschermen waar zich informatie en ICT-voorzieningen bevinden.""",
            fragments=[
                Verifier(
                    identifier="09.01.01/01",
                    title=u"",
                    text=u"""Voor iedere locatie is een beveiligingsplan opgesteld op basis van een risicoafweging.""",
                ),
                Verifier(
                    identifier="09.01.01/02",
                    title=u"",
                    text=u"""Voor voorzieningen (binnen of buiten het gebouw) zijn duidelijke beveiligingsgrenzen bepaald.""",
                ),
                Verifier(
                    identifier="09.01.01/03",
                    title=u"",
                    text=u"""Gebouwen bieden voldoende weerstand (bepaald op basis van een risicoafweging) bij gewelddadige aanvallen zoals inbraak en IT gericht vandalisme.""",
                ),
                Verifier(
                    identifier="09.01.01/04",
                    title=u"",
                    text=u"""Er is 24-uur, 7 dagen per week bewaking; een inbraakalarm gekoppeld aan alarmcentrale is het minimum.""",
                ),
                Verifier(
                    identifier="09.01.01/05",
                    title=u"",
                    text=u"""Van ingehuurde bewakingsdiensten is vooraf geverifieerd dat zij voldoen aan de wettelijke eisen gesteld in de Wet Particuliere Beveiligingsorganisaties en Recherchebureaus. Deze verificatie wordt minimaal jaarlijks herhaald.""",
                ),
                Verifier(
                    identifier="09.01.01/06",
                    title=u"",
                    text=u"""In gebouwen met serverruimtes houdt beveiligingspersoneel toezicht op de toegang. Hiervan wordt een registratie bijhouden.""",
                ),
            ],
        ),
        Norm(
            identifier="09.01.02",
            title=u"Fysieke toegangsbeveiliging",
            text=u"""Beveiligde zones behoren te worden beschermd door geschikte toegangsbeveiliging, om te bewerkstelligen dat alleen bevoegd personeel wordt toegelaten.""",
            fragments=[
                Verifier(
                    identifier="09.01.02/01",
                    title=u"",
                    text=u"""Toegang tot gebouwen of beveiligingszones is alleen mogelijk na autorisatie daartoe.""",
                ),
                Verifier(
                    identifier="09.01.02/02",
                    title=u"",
                    text=u"""De beveiligingszones en toegangsbeveiliging daarvan zijn ingericht conform het Kader Rijkstoegangsbeleid.""",
                ),
                Verifier(
                    identifier="09.01.02/03",
                    title=u"",
                    text=u"""In gebouwen met serverruimtes houdt beveiligingspersoneel toezicht op de toegang. Hiervan wordt een registratie bijhouden.""",
                ),
                Verifier(
                    identifier="09.01.02/04",
                    title=u"",
                    text=u"""De kwaliteit van toegangsmiddelen (deuren, sleutels, sloten, toegangspassen) is afgestemd op de zonering.""",
                ),
                Verifier(
                    identifier="09.01.02/05",
                    title=u"",
                    text=u"""De uitgifte van toegangsmiddelen wordt geregistreerd.""",
                ),
                Verifier(
                    identifier="09.01.02/06",
                    title=u"",
                    text=u"""Niet uitgegeven toegangsmiddelen worden opgeborgen in een beveiligd opbergmiddel.""",
                ),
                Verifier(
                    identifier="09.01.02/07",
                    title=u"",
                    text=u"""Apparatuur en bekabeling in kabelverdeelruimtes en patchruimtes voldoen aan dezelfde eisen t.a.v. toegangbeveiliging zoals die worden gesteld aan computerruimtes.""",
                ),
                Verifier(
                    identifier="09.01.02/08",
                    title=u"",
                    text=u"""Er vindt minimaal één keer per half jaar een periodieke controle/evaluatie plaats op de autorisaties voor fysieke toegang.""",
                ),
            ],
        ),
        Norm(
            identifier="09.01.03",
            title=u"Beveiliging van kantoren, ruimten en faciliteiten",
            text=u"""Er behoort fysieke beveiliging van kantoren, ruimten en faciliteiten te worden ontworpen en toegepast.""",
            fragments=[
                Verifier(
                    identifier="09.01.03/01",
                    title=u"",
                    text=u"""Papieren documenten en mobiele gegevensdragers die vertrouwelijke informatie bevatten worden beveiligd opgeslagen.""",
                ),
                Verifier(
                    identifier="09.01.03/02",
                    title=u"",
                    text=u"""Er is actief beheer van sloten en kluizen met procedures voor wijziging van combinaties door middel van een sleutelplan. Ten behoeve van opslag van gerubriceerde informatie.""",
                ),
                Verifier(
                    identifier="09.01.03/03",
                    title=u"",
                    text=u"""Serverruimtes, datacenters en daar aan gekoppelde bekabelingsystemen zijn ingericht in lijn met geldende best practices.""",
                ),
            ],
        ),
        Norm(
            identifier="09.01.04",
            title=u"Bescherming tegen bedreigingen van buitenaf",
            text=u"""Er behoort fysieke bescherming tegen schade door brand, overstroming, aardschokken, explosies, oproer en andere vormen van natuurlijke of menselijke calamiteiten te worden ontworpen en toegepast.""",
            fragments=[
                Verifier(
                    identifier="09.01.04/01",
                    title=u"",
                    text=u"""Bij maatregelen is rekening gehouden met specifieke bedreigingen van aangrenzende panden of terreinen.""",
                ),
                Verifier(
                    identifier="09.01.04/02",
                    title=u"",
                    text=u"""Reserve apparatuur en back-ups zijn op een zodanige afstand ondergebracht dat één en dezelfde calamiteit er niet voor kan zorgen dat zowel de hoofdlocatie als de back-up/reserve locatie niet meer toegankelijk zijn.""",
                ),
                Verifier(
                    identifier="09.01.04/03",
                    title=u"",
                    text=u"""Beveiligde ruimten waarin zich bedrijfskritische apparatuur bevindt zijn voldoende beveiligd tegen wateroverlast.""",
                ),
                Verifier(
                    identifier="09.01.04/04",
                    title=u"",
                    text=u"""Bij het betrekken van nieuwe gebouwen wordt een locatie gekozen waarbij rekening wordt gehouden met de kans op en de gevolgen van natuurrampen en door mensen veroorzaakte rampen.""",
                ),
                Verifier(
                    identifier="09.01.04/05",
                    title=u"",
                    text=u"""Gevaarlijke of brandbare materialen zijn op een zodanige afstand van een beveiligde ruimte opgeslagen dat een calamiteit met deze materialen geen invloed heeft op de beveiligde ruimte.""",
                ),
                Verifier(
                    identifier="09.01.04/06",
                    title=u"",
                    text=u"""Er is door de brandweer goedgekeurde en voor de situatie geschikte brandblusapparatuur geplaatst en aangesloten. Dit wordt jaarlijks gecontroleerd.""",
                ),
            ],
        ),
        Norm(
            identifier="09.01.05",
            title=u"Werken in beveiligde ruimten",
            text=u"""Er behoren een fysieke bescherming en richtlijnen voor werken in beveiligde ruimten te worden ontworpen en toegepast.""",
            fragments=[
                Verifier(
                    identifier="09.01.05/01",
                    title=u"",
                    text=u"""Medewerkers die zelf niet geautoriseerd zijn mogen alleen onder begeleiding van bevoegd personeel en als er een duidelijke noodzaak voor is toegang krijgen tot fysiek beveiligde ruimten waarin IT voorzieningen zijn geplaatst of waarin met vertrouwelijke informatie wordt gewerkt.""",
                ),
                Verifier(
                    identifier="09.01.05/02",
                    title=u"",
                    text=u"""Beveiligde ruimten (zoals een serverruimte of kluis) waarin zich geen personen bevinden zijn afgesloten en worden regelmatig gecontroleerd.""",
                ),
                Verifier(
                    identifier="09.01.05/03",
                    title=u"",
                    text=u"""Zonder expliciete toestemming mogen binnen beveiligde ruimten geen opnames (foto, video of geluid) worden gemaakt.""",
                ),
            ],
        ),
        Norm(
            identifier="09.01.06",
            title=u"Openbare toegang en gebieden voor laden en lossen",
            text=u"""Toegangspunten zoals gebieden voor laden en lossen en andere punten waar onbevoegden het terrein kunnen betreden, behoren te worden beheerst en indien mogelijk worden afgeschermd van IT voorzieningen, om onbevoegde toegang te voorkomen.""",
            fragments=[
                Verifier(
                    identifier="09.01.06/01",
                    title=u"",
                    text=u"""Er bestaat een procedure voor het omgaan met verdachte pakketten en brieven in postkamers en laad- en losruimten.""",
                ),
            ],
        ),
    ],
)


S0902 = Section(
    identifier="09.02",
    title=u"Beveiliging van apparatuur",
    fragments=[
        Norm(
            identifier="09.02.01",
            title=u"Plaatsing en bescherming van apparatuur",
            text=u"""Apparatuur behoort zo te worden geplaatst en beschermd dat risico's van schade en storing van buitenaf en de gelegenheid voor onbevoegde toegang wordt verminderd.""",
            fragments=[
                Verifier(
                    identifier="09.02.01/01",
                    title=u"",
                    text=u"""Apparatuur wordt opgesteld en aangesloten conform de voorschriften van de leverancier. Dit geldt minimaal voor temperatuur en luchtvochtigheid, aarding, spanningsstabiliteit en overspanningbeveiliging.""",
                ),
                Verifier(
                    identifier="09.02.01/02",
                    title=u"",
                    text=u"""Gebouwen zijn beveiligd tegen blikseminslag.""",
                ),
                Verifier(
                    identifier="09.02.01/03",
                    title=u"",
                    text=u"""Eten en drinken is verboden in computerruimtes.""",
                ),
                Verifier(
                    identifier="09.02.01/04",
                    title=u"",
                    text=u"""Een informatiesysteem voldoet altijd aan de hoogste beveiligingseisen die voor kunnen komen bij het verwerken van informatie. Indien dit niet mogelijk is wordt een gescheiden systeem gebruikt voor de informatieverwerking waaraan hogere eisen gesteld worden.""",
                ),
            ],
        ),
        Norm(
            identifier="09.02.02",
            title=u"Nutsvoorzieningen",
            text=u"""Apparatuur behoort zo te worden geplaatst en beschermd dat risico's van schade en storing van buitenaf en de gelegenheid voor onbevoegde toegang wordt verminderd.""",
            fragments=[
                Verifier(
                    identifier="09.02.02/01",
                    title=u"",
                    text=u"""Apparatuur behoort te worden beschermd tegen stroomuitval en andere storingen door onderbreking van nutsvoorzieningen.""",
                ),
            ],
        ),
        Norm(
            identifier="09.02.03",
            title=u"Beveiliging van kabels",
            text=u"""Voedingskabels en telecommunicatiekabels die voor dataverkeer of ondersteunende informatiediensten worden gebruikt, behoren tegen interceptie of beschadiging te worden beschermd.""",
            fragments=[
                Verifier(
                    identifier="09.02.03/01",
                    title=u"",
                    text=u"""- conform norm -""",
                ),
            ],
        ),
        Norm(
            identifier="09.02.04",
            title=u"Onderhoud van apparatuur",
            text=u"""Apparatuur behoort op correcte wijze te worden onderhouden, om te waarborgen dat deze voortdurend beschikbaar is en in goede staat verkeert.""",
            fragments=[
                Verifier(
                    identifier="09.02.04/01",
                    title=u"",
                    text=u"""Reparatie en onderhoud van apparatuur (hardware) vindt op locatie plaats door bevoegd personeel, tenzij er geen data op het apparaat aanwezig of toegankelijk is.""",
                ),
            ],
        ),
        Norm(
            identifier="09.02.05",
            title=u"Beveiliging van apparatuur buiten het terrein",
            text=u"""Apparatuur buiten de terreinen behoort te worden beveiligd waarbij rekening wordt gehouden met de diverse risico's van werken buiten het terrein van de organisatie.""",
            fragments=[
                Verifier(
                    identifier="09.02.05/01",
                    title=u"",
                    text=u"""Alle apparatuur buiten de terreinen wordt beveiligd met maatregelen die zijn vastgesteld op basis van een risicoafweging.""",
                ),
            ],
        ),
        Norm(
            identifier="09.02.06",
            title=u"Veilig verwijderen of hergebruiken van apparatuur",
            text=u"""Alle apparatuur die opslagmedia bevat, behoort te worden gecontroleerd om te bewerkstelligen dat alle gevoelige gegevens en in licentie gebruikte programmatuur zijn verwijderd of veilig zijn overschreven voordat de apparatuur wordt verwijderd.""",
            fragments=[
                Verifier(
                    identifier="09.02.06/01",
                    title=u"",
                    text=u"""Bij beëindiging van het gebruik of bij een defect worden apparaten en informatiedragers bij de beheersorganisatie ingeleverd. De beheerorganisatie zorgt voor een verantwoorde afvoer zodat er geen data op het apparaat aanwezig of toegankelijk is. Als dit niet kan wordt het apparaat of de informatiedrager fysiek vernietigd. Het afvoeren of vernietigen wordt per bedrijfseenheid geregistreerd.""",
                ),
                Verifier(
                    identifier="09.02.06/02",
                    title=u"",
                    text=u"""Hergebruik van apparatuur buiten de organisatie is slechts toegestaan indien de informatie is verwijderd met een voldoende veilige methode. Een veilige methode is Secure Erase voor apparaten die dit ondersteunen. In overige gevallen wordt de data twee keer overschreven met vaste data, één keer met random data en vervolgens wordt geverifieerd of het overschrijven is gelukt.""",
                ),
            ],
        ),
        Norm(
            identifier="09.02.07",
            title=u"Verwijdering van bedrijfseigendommen",
            text=u"""Apparatuur, informatie en programmatuur van de organisatie mogen niet zonder toestemming vooraf van de locatie worden meegenomen.""",
            fragments=[
                Verifier(
                    identifier="09.02.07/01",
                    title=u"",
                    text=u"""- conform norm -""",
                ),
            ],
        ),
    ],
)


CH09 = Chapter(
    identifier="09",
    title=u"Fysieke beveiliging en beveiliging van de omgeving",
    fragments=[
        S0901,
        S0902,
    ]
)

