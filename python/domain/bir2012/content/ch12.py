# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S1201 = Section(
    identifier="12.01",
    title="Beveiligingseisen voor informatiesystemen",
    fragments=[
        Norm(
            identifier="12.01.01",
            title="Analyse en specificatie van beveiligingseisen",
            text="In bedrijfseisen voor nieuwe informatiesystemen of uitbreidingen van bestaande informatiesystemen "
                 "behoren ook eisen voor beveiligingsmaatregelen te worden opgenomen.",
            fragments=[
                Verifier(
                    identifier="12.01.01/01",
                    title="",
                    text="In projecten worden een beveiligingsrisicoanalyse en maatregelbepaling opgenomen "
                         "als onderdeel van het ontwerp. Ook bij wijzigingen worden de veiligheidsconsequenties "
                         "meegenomen.",
                ),
                Verifier(
                    identifier="12.01.01/02",
                    title="",
                    text="In standaarden voor analyse, ontwikkeling en testen van informatiesystemen wordt "
                         "structureel aandacht besteed aan beveiligingsaspecten. Waar mogelijk wordt gebruikt "
                         "gemaakt van bestaande richtlijnen (bijv. secure coding guidelines).",
                ),
                Verifier(
                    identifier="12.01.01/03",
                    title="",
                    text="Bij aanschaf van producten wordt een proces gevolgd waarbij beveiliging een onderdeel is "
                         "van de specificatie.",
                ),
                Verifier(
                    identifier="12.01.01/04",
                    title="",
                    text="Waar het gaat om beveiligingsrelevante producten wordt de keuze voor een bepaald product "
                         "verantwoord onderbouwd.",
                ),
                Verifier(
                    identifier="12.01.01/05",
                    title="",
                    text="Voor beveiliging worden componenten gebruikt die aantoonbaar voldoen aan "
                         "geaccepteerde beveiligingscriteria zoals NBV-goedkeuring of certificering volgens "
                         "ISO/IEC 15408 (common criteria).",
                ),
            ],
        ),
    ],
)


S1202 = Section(
    identifier="12.02",
    title="Correcte verwerking in toepassingen",
    fragments=[
        Norm(
            identifier="12.02.01",
            title="Validatie van invoergegevens",
            text="In bedrijfseisen voor nieuwe informatiesystemen of uitbreidingen van bestaande informatiesystemen "
                 "behoren ook eisen voor beveiligingsmaatregelen te worden opgenomen.",
            fragments=[
                Verifier(
                    identifier="12.02.01/01",
                    title="",
                    text="Gegevens die worden ingevoerd in toepassingen behoren te worden gevalideerd om te "
                         "bewerkstelligen dat deze gegevens juist en geschikt zijn.",
                ),
            ],
        ),
        Norm(
            identifier="12.02.02",
            title="Beheersing van interne gegevensverwerking",
            text="Er behoren validatiecontroles te worden opgenomen in toepassingen om eventueel corrumperen van "
                 "informatie door verwerkingsfouten of opzettelijke handelingen te ontdekken.",
            fragments=[
                Verifier(
                    identifier="12.02.02/01",
                    title="",
                    text="Er bestaan voldoende mogelijkheden om reeds ingevoerde gegevens te kunnen corrigeren door "
                         "er gegevens aan te kunnen toevoegen.",
                ),
                Verifier(
                    identifier="12.02.02/02",
                    title="",
                    text="Het informatiesysteem moet functies bevatten waarmee vastgesteld kan worden of gegevens "
                         "correct verwerkt zijn. Hiermee wordt een geautomatiseerde controle bedoeld waarmee "
                         "(duidelijke) transactie- en verwerkingsfouten kunnen worden gedetecteerd.",
                ),
                Verifier(
                    identifier="12.02.02/03",
                    title="",
                    text="Stapelen van fouten wordt voorkomen door toepassing van 'noodstop' mechanismen.",
                ),
                Verifier(
                    identifier="12.02.02/04",
                    title="",
                    text="Verwerkingen zijn bij voorkeur herstelbaar zodat bij het optreden van fouten en/of wegraken "
                         "van informatie dit hersteld kan worden door het opnieuw verwerken van de informatie.",
                ),
            ],
        ),
        Norm(
            identifier="12.02.03",
            title="Integriteit van berichten",
            text="Er behoren eisen te worden vastgesteld, en geschikte beheersmaatregelen te worden vastgesteld en "
                 "geïmplementeerd, voor het bewerkstelligen van authenticiteit en het beschermen van integriteit van "
                 "berichten in toepassingen.",
            fragments=[
                Verifier(
                    identifier="12.02.03/01",
                    title="",
                    text="- conform norm -",
                ),
            ],
        ),
        Norm(
            identifier="12.02.04",
            title="Validatie van uitvoergegevens",
            text="Gegevensuitvoer uit een toepassing behoort te worden gevalideerd, om te bewerkstelligen dat "
                 "de verwerking van opgeslagen gegevens op de juiste manier plaatsvindt en geschikt is gezien "
                 "de omstandigheden.",
            fragments=[
                Verifier(
                    identifier="12.02.04/01",
                    title="",
                    text="De uitvoerfuncties van programma's maken het mogelijk om de volledigheid en juistheid van "
                         "de gegevens te kunnen vaststellen (bijv. door checksums).",
                ),
                Verifier(
                    identifier="12.02.04/02",
                    title="",
                    text="Bij uitvoer van gegevens wordt gegarandeerd dat deze met het juiste niveau van "
                         "vertrouwelijkheid beschikbaar gesteld worden (bijv. beveiligd printen).",
                ),
                Verifier(
                    identifier="12.02.04/03",
                    title="",
                    text="Alleen gegevens die noodzakelijk zijn voor de doeleinden van de gebruiker worden uitgevoerd "
                         "(need to know).",
                ),
            ],
        ),
    ],
)


S1203 = Section(
    identifier="12.03",
    title="Cryptografische beheersmaatregelen",
    fragments=[
        Norm(
            identifier="12.03.01",
            title="Beleid voor het gebruik van cryptografische beheersmaatregelen",
            text="Er behoort beleid te worden ontwikkeld en geïmplementeerd voor het gebruik van cryptografische "
                 "beheersmaatregelen voor de bescherming van informatie.",
            fragments=[
                Verifier(
                    identifier="12.03.01/01",
                    title="",
                    text="De gebruikte cryptografische algoritmen voor versleuteling zijn als open standaard "
                         "gedocumenteerd en zijn door onafhankelijke betrouwbare deskundigen getoetst.",
                ),
                Verifier(
                    identifier="12.03.01/02",
                    title="",
                    text="Bij de inzet van cryptografische producten volgt een afweging van de risico's aangaande "
                         "locaties, processen en behandelende partijen.",
                ),
                Verifier(
                    identifier="12.03.01/03",
                    title="",
                    text="De cryptografische beveiligingsvoorzieningen en componenten voldoen aan algemeen gangbare "
                         "beveiligingscriteria (zoals FIPS 140-2 en waar mogelijk NBV).",
                ),
            ],
        ),
        Norm(
            identifier="12.03.02",
            title="Sleutelbeheer",
            text="Er behoort sleutelbeheer te zijn vastgesteld ter ondersteuning van het gebruik van cryptografische "
                 "technieken binnen de organisatie.",
            fragments=[
                Verifier(
                    identifier="12.03.02/01",
                    title="",
                    text="In het sleutelbeheer is minimaal aandacht besteed aan het proces, de actoren en hun "
                         "verantwoordelijkheden.",
                ),
                Verifier(
                    identifier="12.03.02/02",
                    title="",
                    text="De geldigheidsduur van cryptografische sleutels wordt bepaald aan de hand van de beoogde "
                         "toepassing en is vastgelegd in het cryptografisch beleid.",
                ),
                Verifier(
                    identifier="12.03.02/03",
                    title="",
                    text="De vertrouwelijkheid van cryptografische sleutels moet worden gewaarborgd tijdens "
                         "generatie, gebruik, transport en opslag van de sleutels.",
                ),
                Verifier(
                    identifier="12.03.02/04",
                    title="",
                    text="Er is een procedure vastgesteld waarin is bepaald hoe wordt omgegaan met "
                         "gecompromitteerde sleutels.",
                ),
                Verifier(
                    identifier="12.03.02/05",
                    title="",
                    text="Bij voorkeur is sleutelmanagement ingericht volgens PKI Overheid.",
                ),
            ],
        ),
    ],
)


S1204 = Section(
    identifier="12.04",
    title="Beveiliging van systeembestanden",
    fragments=[
        Norm(
            identifier="12.04.01",
            title="Beheersing van operationele programmatuur",
            text="Er behoren procedures te zijn vastgesteld om de installatie van programmatuur op productiesystemen "
                 "te beheersen.",
            fragments=[
                Verifier(
                    identifier="12.04.01/01",
                    title="",
                    text="Alleen geautoriseerd personeel kan functies en software installeren of activeren.",
                ),
                Verifier(
                    identifier="12.04.01/02",
                    title="",
                    text="Programmatuur behoort pas te worden geïnstalleerd op een productieomgeving na een "
                         "succesvolle test en acceptatie.",
                ),
                Verifier(
                    identifier="12.04.01/03",
                    title="",
                    text="Geïnstalleerde programmatuur, configuraties en documentatie worden bijgehouden in "
                         "een configuratiedatabase.",
                ),
                Verifier(
                    identifier="12.04.01/04",
                    title="",
                    text="Er worden alleen door de leverancier onderhouden (versies van) software gebruikt.",
                ),
                Verifier(
                    identifier="12.04.01/05",
                    title="",
                    text="Van updates wordt een log bijgehouden.",
                ),
                Verifier(
                    identifier="12.04.01/06",
                    title="",
                    text="Er is een rollbackstrategie.",
                ),
            ],
        ),
        Norm(
            identifier="12.04.02",
            title="Bescherming van testdata",
            text="Testgegevens behoren zorgvuldig te worden gekozen, beschermd en beheerst.",
            fragments=[
                Verifier(
                    identifier="12.04.02/01",
                    title="",
                    text="Het gebruik van kopieën van operationele databases voor testgegevens wordt vermeden. "
                         "Indien toch noodzakelijk, worden de gegevens zoveel mogelijk geanonimiseerd en na de test "
                         "zorgvuldig verwijderd.",
                ),
            ],
        ),
        Norm(
            identifier="12.04.03",
            title="Toegangsbeheersing voor broncode van programmatuur",
            text="De toegang tot broncode van programmatuur behoort te worden beperkt.",
            fragments=[
                Verifier(
                    identifier="12.04.03/01",
                    title="",
                    text="De toegang tot broncode wordt zoveel mogelijk beperkt om de code tegen onbedoelde "
                         "wijzigingen te beschermen. Alleen geautoriseerde personen hebben toegang.",
                ),
            ],
        ),
    ],
)


S1205 = Section(
    identifier="12.05",
    title="Beveiliging bij ontwikkelingsprocessen en ondersteuningsprocessen",
    fragments=[
        Norm(
            identifier="12.05.01",
            title="Procedures voor wijzigingsbeheer",
            text="De implementatie van wijzigingen behoort te worden beheerst door middel van formele procedures "
                 "voor wijzigingsbeheer.",
            fragments=[
                Verifier(
                    identifier="12.05.01/01",
                    title="",
                    text="Er is aantoonbaar wijzigingsmanagement ingericht volgens gangbare best practices "
                         "zoals ITIL.",
                ),
            ],
        ),
        Norm(
            identifier="12.05.02",
            title="Technische beoordeling van toepassingen na wijzigingen in het besturingssysteem",
            text="Bij wijzigingen in besturingssystemen behoren bedrijfskritische toepassingen te worden beoordeeld "
                 "en getest om te bewerkstelligen dat er geen nadelige gevolgen zijn voor de activiteiten of "
                 "beveiliging van de organisatie.",
            fragments=[
                Verifier(
                    identifier="12.05.02/01",
                    title="",
                    text="Van aanpassingen (zoals updates) aan softwarematige componenten van de technische "
                         "infrastructuur wordt vastgesteld dat deze de juiste werking van de technische componenten "
                         "niet in gevaar brengen.",
                ),
            ],
        ),
        Norm(
            identifier="12.05.03",
            title="Restricties op wijzigingen in programmatuurpakketten",
            text="Bij wijzigingen in besturingssystemen behoren bedrijfskritische toepassingen te worden "
                 "beoordeeld en getest om te bewerkstelligen dat er geen nadelige gevolgen zijn voor de "
                 "activiteiten of beveiliging van de organisatie.Wijzigingen in programmatuurpakketten behoren "
                 "te worden ontmoedigd, te worden beperkt tot noodzakelijke wijzigingen, en alle wijzigingen "
                 "behoren strikt te worden beheerst.",
            fragments=[
                Verifier(
                    identifier="12.05.03/01",
                    title="",
                    text="Bij het instellen van besturingsprogrammatuur en programmapakketten wordt uitgegaan van "
                         "de aanwijzingen van de leverancier.",
                ),
            ],
        ),
        Norm(
            identifier="12.05.04",
            title="Uitlekken van informatie",
            text="Er behoort te worden voorkomen dat zich gelegenheden voordoen om informatie te laten uitlekken.",
            fragments=[
                Verifier(
                    identifier="12.05.04/01",
                    title="",
                    text="Op het grensvlak van een vertrouwde en een onvertrouwde omgeving vindt "
                         "content-scanning plaats.",
                ),
            ],
        ),
        Norm(
            identifier="12.05.05",
            title="Uitbestede ontwikkeling van programmatuur",
            text="Uitbestede ontwikkeling van programmatuur behoort onder supervisie te staan van en te worden "
                 "gecontroleerd door de organisatie.",
            fragments=[
                Verifier(
                    identifier="12.05.05/01",
                    title="",
                    text="Uitbestede ontwikkeling van programmatuur komt tot stand onder supervisie en "
                         "verantwoordelijkheid van de uitbestedende organisatie. Er worden maatregelen "
                         "getroffen om de kwaliteit en vertrouwelijkheid te borgen (bijv. stellen van "
                         "veiligheidseisen, regelen van beschikbaarheid en eigendomsrecht van de code, "
                         "certificatie, kwaliteitsaudits, testen en aansprakelijkheidsregelingen).",
                ),
            ],
        ),
    ],
)


S1206 = Section(
    identifier="12.06",
    title="Beheer van technische kwetsbaarheden",
    fragments=[
        Norm(
            identifier="12.06.01",
            title="Beheersing van technische kwetsbaarheden",
            text="Er behoort tijdig informatie te worden verkregen over technische kwetsbaarheden van de "
                 "gebruikte informatiesystemen. De mate waarin de organisatie blootstaat aan dergelijke "
                 "kwetsbaarheden behoort te worden geëvalueerd en er behoren geschikte maatregelen te worden "
                 "genomen voor behandeling van daarmee samenhangende risico's.",
            fragments=[
                Verifier(
                    identifier="12.06.01/01",
                    title="",
                    text="Er is een proces ingericht voor het beheer van technische kwetsbaarheden; dit omvat "
                         "minimaal periodieke penetratietests, risicoanalyses van kwetsbaarheden en patching.",
                ),
                Verifier(
                    identifier="12.06.01/02",
                    title="",
                    text="Van softwarematige voorzieningen van de technische infrastructuur kan (bij voorkeur "
                         "geautomatiseerd) gecontroleerd worden of de laatste updates (patches) in zijn doorgevoerd. "
                         "Het doorvoeren van een update vindt niet geautomatiseerd plaats, tenzij hier speciale "
                         "afspraken over zijn met de leverancier.",
                ),
                Verifier(
                    identifier="12.06.01/03",
                    title="",
                    text="Indien een patch beschikbaar is, dienen de risico's verbonden met de installatie van de "
                         "patch te worden geëvalueerd (de risico's verbonden met de kwetsbaarheid dienen vergeleken "
                         "te worden met de risico's van het installeren van de patch).",
                ),
                Verifier(
                    identifier="12.06.01/04",
                    title="",
                    text="Updates/patches voor kwetsbaarheden waarvan de kans op misbruik hoog is en waarvan de "
                         "schade hoog is worden zo spoedig mogelijk doorgevoerd, echter minimaal binnen één week. "
                         "Minder kritische beveiligings-updates/patches moeten worden ingepland bij de eerst "
                         "volgende onderhoudsronde.",
                ),
            ],
        ),
    ],
)


CH12 = Chapter(
    identifier="12",
    title="Verwerving, ontwikkeling en onderhoud van Informatiesystemen",
    fragments=[
        S1201,
        S1202,
        S1203,
        S1204,
        S1205,
        S1206,
    ]
)
