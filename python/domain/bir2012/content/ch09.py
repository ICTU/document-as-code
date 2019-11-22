# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S0901 = Section(
    identifier="09.01",
    title="Beveiligde ruimten",
    fragments=[
        Norm(
            identifier="09.01.01",
            title="Fysieke beveiliging van de omgeving",
            text="Er behoren toegangsbeveiligingen (barrières zoals muren, toegangspoorten met kaartsloten of een "
                 "bemande receptie) te worden aangebracht om ruimten te beschermen waar zich informatie en "
                 "ICT-voorzieningen bevinden.",
            fragments=[
                Verifier(
                    identifier="09.01.01/01",
                    title="",
                    text="Voor iedere locatie is een beveiligingsplan opgesteld op basis van een risicoafweging.",
                ),
                Verifier(
                    identifier="09.01.01/02",
                    title="",
                    text="Voor voorzieningen (binnen of buiten het gebouw) zijn duidelijke beveiligingsgrenzen "
                         "bepaald.",
                ),
                Verifier(
                    identifier="09.01.01/03",
                    title="",
                    text="Gebouwen bieden voldoende weerstand (bepaald op basis van een risicoafweging) bij "
                         "gewelddadige aanvallen zoals inbraak en IT-gericht vandalisme.",
                ),
                Verifier(
                    identifier="09.01.01/04",
                    title="",
                    text="Er is 24-uur, 7 dagen per week bewaking; een inbraakalarm gekoppeld aan alarmcentrale is "
                         "het minimum.",
                ),
                Verifier(
                    identifier="09.01.01/05",
                    title="",
                    text="Van ingehuurde bewakingsdiensten is vooraf geverifieerd dat zij voldoen aan de wettelijke "
                         "eisen gesteld in de Wet Particuliere Beveiligingsorganisaties en Recherchebureaus. Deze "
                         "verificatie wordt minimaal jaarlijks herhaald.",
                ),
                Verifier(
                    identifier="09.01.01/06",
                    title="",
                    text="In gebouwen met serverruimtes houdt beveiligingspersoneel toezicht op de toegang. Hiervan "
                         "wordt een registratie bijhouden.",
                ),
            ],
        ),
        Norm(
            identifier="09.01.02",
            title="Fysieke toegangsbeveiliging",
            text="Beveiligde zones behoren te worden beschermd door geschikte toegangsbeveiliging, om te "
                 "bewerkstelligen dat alleen bevoegd personeel wordt toegelaten.",
            fragments=[
                Verifier(
                    identifier="09.01.02/01",
                    title="",
                    text="Toegang tot gebouwen of beveiligingszones is alleen mogelijk na autorisatie daartoe.",
                ),
                Verifier(
                    identifier="09.01.02/02",
                    title="",
                    text="De beveiligingszones en toegangsbeveiliging daarvan zijn ingericht conform het Kader "
                         "Rijkstoegangsbeleid.",
                ),
                Verifier(
                    identifier="09.01.02/03",
                    title="",
                    text="In gebouwen met serverruimtes houdt beveiligingspersoneel toezicht op de toegang. Hiervan "
                         "wordt een registratie bijhouden.",
                ),
                Verifier(
                    identifier="09.01.02/04",
                    title="",
                    text="De kwaliteit van toegangsmiddelen (deuren, sleutels, sloten, toegangspassen) is afgestemd "
                         "op de zonering.",
                ),
                Verifier(
                    identifier="09.01.02/05",
                    title="",
                    text="De uitgifte van toegangsmiddelen wordt geregistreerd.",
                ),
                Verifier(
                    identifier="09.01.02/06",
                    title="",
                    text="Niet uitgegeven toegangsmiddelen worden opgeborgen in een beveiligd opbergmiddel.",
                ),
                Verifier(
                    identifier="09.01.02/07",
                    title="",
                    text="Apparatuur en bekabeling in kabelverdeelruimtes en patchruimtes voldoen aan dezelfde eisen "
                         "t.a.v. toegangbeveiliging zoals die worden gesteld aan computerruimtes.",
                ),
                Verifier(
                    identifier="09.01.02/08",
                    title="",
                    text="Er vindt minimaal één keer per half jaar een periodieke controle/evaluatie plaats op de "
                         "autorisaties voor fysieke toegang.",
                ),
            ],
        ),
        Norm(
            identifier="09.01.03",
            title="Beveiliging van kantoren, ruimten en faciliteiten",
            text="Er behoort fysieke beveiliging van kantoren, ruimten en faciliteiten te worden ontworpen en "
                 "toegepast.",
            fragments=[
                Verifier(
                    identifier="09.01.03/01",
                    title="",
                    text="Papieren documenten en mobiele gegevensdragers die vertrouwelijke informatie bevatten "
                         "worden beveiligd opgeslagen.",
                ),
                Verifier(
                    identifier="09.01.03/02",
                    title="",
                    text="Er is actief beheer van sloten en kluizen met procedures voor wijziging van combinaties "
                         "door middel van een sleutelplan. Ten behoeve van opslag van gerubriceerde informatie.",
                ),
                Verifier(
                    identifier="09.01.03/03",
                    title="",
                    text="Serverruimtes, datacenters en daar aan gekoppelde bekabelingsystemen zijn ingericht in "
                         "lijn met geldende best practices.",
                ),
            ],
        ),
        Norm(
            identifier="09.01.04",
            title="Bescherming tegen bedreigingen van buitenaf",
            text="Er behoort fysieke bescherming tegen schade door brand, overstroming, aardschokken, explosies, "
                 "oproer en andere vormen van natuurlijke of menselijke calamiteiten te worden ontworpen en "
                 "toegepast.",
            fragments=[
                Verifier(
                    identifier="09.01.04/01",
                    title="",
                    text="Bij maatregelen is rekening gehouden met specifieke bedreigingen van aangrenzende panden "
                         "of terreinen.",
                ),
                Verifier(
                    identifier="09.01.04/02",
                    title="",
                    text="Reserve apparatuur en back-ups zijn op een zodanige afstand ondergebracht dat één en "
                         "dezelfde calamiteit er niet voor kan zorgen dat zowel de hoofdlocatie als de "
                         "back-up/reserve locatie niet meer toegankelijk zijn.",
                ),
                Verifier(
                    identifier="09.01.04/03",
                    title="",
                    text="Beveiligde ruimten waarin zich bedrijfskritische apparatuur bevindt zijn voldoende "
                         "beveiligd tegen wateroverlast.",
                ),
                Verifier(
                    identifier="09.01.04/04",
                    title="",
                    text="Bij het betrekken van nieuwe gebouwen wordt een locatie gekozen waarbij rekening wordt "
                         "gehouden met de kans op en de gevolgen van natuurrampen en door mensen veroorzaakte rampen.",
                ),
                Verifier(
                    identifier="09.01.04/05",
                    title="",
                    text="Gevaarlijke of brandbare materialen zijn op een zodanige afstand van een beveiligde ruimte "
                         "opgeslagen dat een calamiteit met deze materialen geen invloed heeft op de beveiligde "
                         "ruimte.",
                ),
                Verifier(
                    identifier="09.01.04/06",
                    title="",
                    text="Er is door de brandweer goedgekeurde en voor de situatie geschikte brandblusapparatuur "
                         "geplaatst en aangesloten. Dit wordt jaarlijks gecontroleerd.",
                ),
            ],
        ),
        Norm(
            identifier="09.01.05",
            title="Werken in beveiligde ruimten",
            text="Er behoren een fysieke bescherming en richtlijnen voor werken in beveiligde ruimten te worden "
                 "ontworpen en toegepast.",
            fragments=[
                Verifier(
                    identifier="09.01.05/01",
                    title="",
                    text="Medewerkers die zelf niet geautoriseerd zijn mogen alleen onder begeleiding van bevoegd "
                         "personeel en als er een duidelijke noodzaak voor is toegang krijgen tot fysiek beveiligde "
                         "ruimten waarin IT voorzieningen zijn geplaatst of waarin met vertrouwelijke informatie "
                         "wordt gewerkt.",
                ),
                Verifier(
                    identifier="09.01.05/02",
                    title="",
                    text="Beveiligde ruimten (zoals een serverruimte of kluis) waarin zich geen personen bevinden "
                         "zijn afgesloten en worden regelmatig gecontroleerd.",
                ),
                Verifier(
                    identifier="09.01.05/03",
                    title="",
                    text="Zonder expliciete toestemming mogen binnen beveiligde ruimten geen opnames (foto, video of "
                         "geluid) worden gemaakt.",
                ),
            ],
        ),
        Norm(
            identifier="09.01.06",
            title="Openbare toegang en gebieden voor laden en lossen",
            text="Toegangspunten zoals gebieden voor laden en lossen en andere punten waar onbevoegden het terrein "
                 "kunnen betreden, behoren te worden beheerst en indien mogelijk worden afgeschermd van "
                 "IT-voorzieningen, om onbevoegde toegang te voorkomen.",
            fragments=[
                Verifier(
                    identifier="09.01.06/01",
                    title="",
                    text="Er bestaat een procedure voor het omgaan met verdachte pakketten en brieven in postkamers "
                         "en laad- en losruimten.",
                ),
            ],
        ),
    ],
)


S0902 = Section(
    identifier="09.02",
    title="Beveiliging van apparatuur",
    fragments=[
        Norm(
            identifier="09.02.01",
            title="Plaatsing en bescherming van apparatuur",
            text="Apparatuur behoort zo te worden geplaatst en beschermd dat risico's van schade en storing van "
                 "buitenaf en de gelegenheid voor onbevoegde toegang wordt verminderd.",
            fragments=[
                Verifier(
                    identifier="09.02.01/01",
                    title="",
                    text="Apparatuur wordt opgesteld en aangesloten conform de voorschriften van de leverancier. Dit "
                         "geldt minimaal voor temperatuur en luchtvochtigheid, aarding, spanningsstabiliteit en "
                         "overspanningbeveiliging.",
                ),
                Verifier(
                    identifier="09.02.01/02",
                    title="",
                    text="Gebouwen zijn beveiligd tegen blikseminslag.",
                ),
                Verifier(
                    identifier="09.02.01/03",
                    title="",
                    text="Eten en drinken is verboden in computerruimtes.",
                ),
                Verifier(
                    identifier="09.02.01/04",
                    title="",
                    text="Een informatiesysteem voldoet altijd aan de hoogste beveiligingseisen die voor kunnen "
                         "komen bij het verwerken van informatie. Indien dit niet mogelijk is wordt een gescheiden "
                         "systeem gebruikt voor de informatieverwerking waaraan hogere eisen gesteld worden.",
                ),
            ],
        ),
        Norm(
            identifier="09.02.02",
            title="Nutsvoorzieningen",
            text="Apparatuur behoort zo te worden geplaatst en beschermd dat risico's van schade en storing van "
                 "buitenaf en de gelegenheid voor onbevoegde toegang wordt verminderd.",
            fragments=[
                Verifier(
                    identifier="09.02.02/01",
                    title="",
                    text="Apparatuur behoort te worden beschermd tegen stroomuitval en andere storingen door "
                         "onderbreking van nutsvoorzieningen.",
                ),
            ],
        ),
        Norm(
            identifier="09.02.03",
            title="Beveiliging van kabels",
            text="Voedingskabels en telecommunicatiekabels die voor dataverkeer of ondersteunende informatiediensten "
                 "worden gebruikt, behoren tegen interceptie of beschadiging te worden beschermd.",
            fragments=[
                Verifier(
                    identifier="09.02.03/01",
                    title="",
                    text="- conform norm -""",
                ),
            ],
        ),
        Norm(
            identifier="09.02.04",
            title="Onderhoud van apparatuur",
            text="Apparatuur behoort op correcte wijze te worden onderhouden, om te waarborgen dat deze voortdurend "
                 "beschikbaar is en in goede staat verkeert.",
            fragments=[
                Verifier(
                    identifier="09.02.04/01",
                    title="",
                    text="Reparatie en onderhoud van apparatuur (hardware) vindt op locatie plaats door bevoegd "
                         "personeel, tenzij er geen data op het apparaat aanwezig of toegankelijk is.",
                ),
            ],
        ),
        Norm(
            identifier="09.02.05",
            title="Beveiliging van apparatuur buiten het terrein",
            text="Apparatuur buiten de terreinen behoort te worden beveiligd waarbij rekening wordt gehouden met de "
                 "diverse risico's van werken buiten het terrein van de organisatie.",
            fragments=[
                Verifier(
                    identifier="09.02.05/01",
                    title="",
                    text="Alle apparatuur buiten de terreinen wordt beveiligd met maatregelen die zijn vastgesteld op "
                         "basis van een risicoafweging.",
                ),
            ],
        ),
        Norm(
            identifier="09.02.06",
            title="Veilig verwijderen of hergebruiken van apparatuur",
            text="Alle apparatuur die opslagmedia bevat, behoort te worden gecontroleerd om te bewerkstelligen dat "
                 "alle gevoelige gegevens en in licentie gebruikte programmatuur zijn verwijderd of veilig zijn "
                 "overschreven voordat de apparatuur wordt verwijderd.",
            fragments=[
                Verifier(
                    identifier="09.02.06/01",
                    title="",
                    text="Bij beëindiging van het gebruik of bij een defect worden apparaten en informatiedragers bij "
                         "de beheersorganisatie ingeleverd. De beheerorganisatie zorgt voor een verantwoorde afvoer "
                         "zodat er geen data op het apparaat aanwezig of toegankelijk is. Als dit niet kan wordt het "
                         "apparaat of de informatiedrager fysiek vernietigd. Het afvoeren of vernietigen wordt per "
                         "bedrijfseenheid geregistreerd.",
                ),
                Verifier(
                    identifier="09.02.06/02",
                    title="",
                    text="Hergebruik van apparatuur buiten de organisatie is slechts toegestaan indien de informatie "
                         "is verwijderd met een voldoende veilige methode. Een veilige methode is Secure Erase voor "
                         "apparaten die dit ondersteunen. In overige gevallen wordt de data twee keer overschreven "
                         "met vaste data, één keer met random data en vervolgens wordt geverifieerd of het "
                         "overschrijven is gelukt.",
                ),
            ],
        ),
        Norm(
            identifier="09.02.07",
            title="Verwijdering van bedrijfseigendommen",
            text="Apparatuur, informatie en programmatuur van de organisatie mogen niet zonder toestemming vooraf "
                 "van de locatie worden meegenomen.",
            fragments=[
                Verifier(
                    identifier="09.02.07/01",
                    title="",
                    text="- conform norm -""",
                ),
            ],
        ),
    ],
)


CH09 = Chapter(
    identifier="09",
    title="Fysieke beveiliging en beveiliging van de omgeving",
    fragments=[
        S0901,
        S0902,
    ]
)
