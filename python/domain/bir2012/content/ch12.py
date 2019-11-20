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


S1201 = Section(
    identifier="12.01",
    title=u"Beveiligingseisen voor informatiesystemen",
    fragments=[
        Norm(
            identifier="12.01.01",
            title=u"Analyse en specificatie van beveiligingseisen",
            text=u"In bedrijfseisen voor nieuwe informatiesystemen of uitbreidingen van bestaande informatiesystemen "
                 u"behoren ook eisen voor beveiligingsmaatregelen te worden opgenomen.",
            fragments=[
                Verifier(
                    identifier="12.01.01/01",
                    title=u"",
                    text=u"In projecten worden een beveiligingsrisicoanalyse en maatregelbepaling opgenomen "
                         u"als onderdeel van het ontwerp. Ook bij wijzigingen worden de veiligheidsconsequenties "
                         u"meegenomen.",
                ),
                Verifier(
                    identifier="12.01.01/02",
                    title=u"",
                    text=u"In standaarden voor analyse, ontwikkeling en testen van informatiesystemen wordt "
                         u"structureel aandacht besteed aan beveiligingsaspecten. Waar mogelijk wordt gebruikt "
                         u"gemaakt van bestaande richtlijnen (bijv. secure coding guidelines).",
                ),
                Verifier(
                    identifier="12.01.01/03",
                    title=u"",
                    text=u"Bij aanschaf van producten wordt een proces gevolgd waarbij beveiliging een onderdeel is "
                         u"van de specificatie.",
                ),
                Verifier(
                    identifier="12.01.01/04",
                    title=u"",
                    text=u"Waar het gaat om beveiligingsrelevante producten wordt de keuze voor een bepaald product "
                         u"verantwoord onderbouwd.",
                ),
                Verifier(
                    identifier="12.01.01/05",
                    title=u"",
                    text=u"Voor beveiliging worden componenten gebruikt die aantoonbaar voldoen aan "
                         u"geaccepteerde beveiligingscriteria zoals NBV-goedkeuring of certificering volgens "
                         u"ISO/IEC 15408 (common criteria).",
                ),
            ],
        ),
    ],
)


S1202 = Section(
    identifier="12.02",
    title=u"Correcte verwerking in toepassingen",
    fragments=[
        Norm(
            identifier="12.02.01",
            title=u"Validatie van invoergegevens",
            text=u"In bedrijfseisen voor nieuwe informatiesystemen of uitbreidingen van bestaande informatiesystemen "
                 u"behoren ook eisen voor beveiligingsmaatregelen te worden opgenomen.",
            fragments=[
                Verifier(
                    identifier="12.02.01/01",
                    title=u"",
                    text=u"Gegevens die worden ingevoerd in toepassingen behoren te worden gevalideerd om te "
                         u"bewerkstelligen dat deze gegevens juist en geschikt zijn.",
                ),
            ],
        ),
        Norm(
            identifier="12.02.02",
            title=u"Beheersing van interne gegevensverwerking",
            text=u"Er behoren validatiecontroles te worden opgenomen in toepassingen om eventueel corrumperen van "
                 u"informatie door verwerkingsfouten of opzettelijke handelingen te ontdekken.",
            fragments=[
                Verifier(
                    identifier="12.02.02/01",
                    title=u"",
                    text=u"Er bestaan voldoende mogelijkheden om reeds ingevoerde gegevens te kunnen corrigeren door "
                         u"er gegevens aan te kunnen toevoegen.",
                ),
                Verifier(
                    identifier="12.02.02/02",
                    title=u"",
                    text=u"Het informatiesysteem moet functies bevatten waarmee vastgesteld kan worden of gegevens "
                         u"correct verwerkt zijn. Hiermee wordt een geautomatiseerde controle bedoeld waarmee "
                         u"(duidelijke) transactie- en verwerkingsfouten kunnen worden gedetecteerd.",
                ),
                Verifier(
                    identifier="12.02.02/03",
                    title=u"",
                    text=u"Stapelen van fouten wordt voorkomen door toepassing van 'noodstop' mechanismen.",
                ),
                Verifier(
                    identifier="12.02.02/04",
                    title=u"",
                    text=u"Verwerkingen zijn bij voorkeur herstelbaar zodat bij het optreden van fouten en/of wegraken "
                         u"van informatie dit hersteld kan worden door het opnieuw verwerken van de informatie.",
                ),
            ],
        ),
        Norm(
            identifier="12.02.03",
            title=u"Integriteit van berichten",
            text=u"Er behoren eisen te worden vastgesteld, en geschikte beheersmaatregelen te worden vastgesteld en "
                 u"geïmplementeerd, voor het bewerkstelligen van authenticiteit en het beschermen van integriteit van "
                 u"berichten in toepassingen.",
            fragments=[
                Verifier(
                    identifier="12.02.03/01",
                    title=u"",
                    text=u"- conform norm -",
                ),
            ],
        ),
        Norm(
            identifier="12.02.04",
            title=u"Validatie van uitvoergegevens",
            text=u"Gegevensuitvoer uit een toepassing behoort te worden gevalideerd, om te bewerkstelligen dat "
                 u"de verwerking van opgeslagen gegevens op de juiste manier plaatsvindt en geschikt is gezien "
                 u"de omstandigheden.",
            fragments=[
                Verifier(
                    identifier="12.02.04/01",
                    title=u"",
                    text=u"De uitvoerfuncties van programma's maken het mogelijk om de volledigheid en juistheid van "
                         u"de gegevens te kunnen vaststellen (bijv. door checksums).",
                ),
                Verifier(
                    identifier="12.02.04/02",
                    title=u"",
                    text=u"Bij uitvoer van gegevens wordt gegarandeerd dat deze met het juiste niveau van "
                         u"vertrouwelijkheid beschikbaar gesteld worden (bijv. beveiligd printen).",
                ),
                Verifier(
                    identifier="12.02.04/03",
                    title=u"",
                    text=u"Alleen gegevens die noodzakelijk zijn voor de doeleinden van de gebruiker worden uitgevoerd "
                         u"(need to know).",
                ),
            ],
        ),
    ],
)


S1203 = Section(
    identifier="12.03",
    title=u"Cryptografische beheersmaatregelen",
    fragments=[
        Norm(
            identifier="12.03.01",
            title=u"Beleid voor het gebruik van cryptografische beheersmaatregelen",
            text=u"Er behoort beleid te worden ontwikkeld en geïmplementeerd voor het gebruik van cryptografische "
                 u"beheersmaatregelen voor de bescherming van informatie.",
            fragments=[
                Verifier(
                    identifier="12.03.01/01",
                    title=u"",
                    text=u"De gebruikte cryptografische algoritmen voor versleuteling zijn als open standaard "
                         u"gedocumenteerd en zijn door onafhankelijke betrouwbare deskundigen getoetst.",
                ),
                Verifier(
                    identifier="12.03.01/02",
                    title=u"",
                    text=u"Bij de inzet van cryptografische producten volgt een afweging van de risico's aangaande "
                         u"locaties, processen en behandelende partijen.",
                ),
                Verifier(
                    identifier="12.03.01/03",
                    title=u"",
                    text=u"De cryptografische beveiligingsvoorzieningen en componenten voldoen aan algemeen gangbare "
                         u"beveiligingscriteria (zoals FIPS 140-2 en waar mogelijk NBV).",
                ),
            ],
        ),
        Norm(
            identifier="12.03.02",
            title=u"Sleutelbeheer",
            text=u"Er behoort sleutelbeheer te zijn vastgesteld ter ondersteuning van het gebruik van cryptografische "
                 u"technieken binnen de organisatie.",
            fragments=[
                Verifier(
                    identifier="12.03.02/01",
                    title=u"",
                    text=u"In het sleutelbeheer is minimaal aandacht besteed aan het proces, de actoren en hun "
                         u"verantwoordelijkheden.",
                ),
                Verifier(
                    identifier="12.03.02/02",
                    title=u"",
                    text=u"De geldigheidsduur van cryptografische sleutels wordt bepaald aan de hand van de beoogde "
                         u"toepassing en is vastgelegd in het cryptografisch beleid.",
                ),
                Verifier(
                    identifier="12.03.02/03",
                    title=u"",
                    text=u"De vertrouwelijkheid van cryptografische sleutels moet worden gewaarborgd tijdens "
                         u"generatie, gebruik, transport en opslag van de sleutels.",
                ),
                Verifier(
                    identifier="12.03.02/04",
                    title=u"",
                    text=u"Er is een procedure vastgesteld waarin is bepaald hoe wordt omgegaan met "
                         u"gecompromitteerde sleutels.",
                ),
                Verifier(
                    identifier="12.03.02/05",
                    title=u"",
                    text=u"Bij voorkeur is sleutelmanagement ingericht volgens PKI Overheid.",
                ),
            ],
        ),
    ],
)


S1204 = Section(
    identifier="12.04",
    title=u"Beveiliging van systeembestanden",
    fragments=[
        Norm(
            identifier="12.04.01",
            title=u"Beheersing van operationele programmatuur",
            text=u"Er behoren procedures te zijn vastgesteld om de installatie van programmatuur op productiesystemen "
                 u"te beheersen.",
            fragments=[
                Verifier(
                    identifier="12.04.01/01",
                    title=u"",
                    text=u"Alleen geautoriseerd personeel kan functies en software installeren of activeren.",
                ),
                Verifier(
                    identifier="12.04.01/02",
                    title=u"",
                    text=u"Programmatuur behoort pas te worden geïnstalleerd op een productieomgeving na een "
                         u"succesvolle test en acceptatie.",
                ),
                Verifier(
                    identifier="12.04.01/03",
                    title=u"",
                    text=u"Geïnstalleerde programmatuur, configuraties en documentatie worden bijgehouden in "
                         u"een configuratiedatabase.",
                ),
                Verifier(
                    identifier="12.04.01/04",
                    title=u"",
                    text=u"Er worden alleen door de leverancier onderhouden (versies van) software gebruikt.",
                ),
                Verifier(
                    identifier="12.04.01/05",
                    title=u"",
                    text=u"Van updates wordt een log bijgehouden.",
                ),
                Verifier(
                    identifier="12.04.01/06",
                    title=u"",
                    text=u"Er is een rollbackstrategie.",
                ),
            ],
        ),
        Norm(
            identifier="12.04.02",
            title=u"Bescherming van testdata",
            text=u"Testgegevens behoren zorgvuldig te worden gekozen, beschermd en beheerst.",
            fragments=[
                Verifier(
                    identifier="12.04.02/01",
                    title=u"",
                    text=u"Het gebruik van kopieën van operationele databases voor testgegevens wordt vermeden. "
                         u"Indien toch noodzakelijk, worden de gegevens zoveel mogelijk geanonimiseerd en na de test "
                         u"zorgvuldig verwijderd.",
                ),
            ],
        ),
        Norm(
            identifier="12.04.03",
            title=u"Toegangsbeheersing voor broncode van programmatuur",
            text=u"De toegang tot broncode van programmatuur behoort te worden beperkt.",
            fragments=[
                Verifier(
                    identifier="12.04.03/01",
                    title=u"",
                    text=u"De toegang tot broncode wordt zoveel mogelijk beperkt om de code tegen onbedoelde "
                         u"wijzigingen te beschermen. Alleen geautoriseerde personen hebben toegang.",
                ),
            ],
        ),
    ],
)


S1205 = Section(
    identifier="12.05",
    title=u"Beveiliging bij ontwikkelingsprocessen en ondersteuningsprocessen",
    fragments=[
        Norm(
            identifier="12.05.01",
            title=u"Procedures voor wijzigingsbeheer",
            text=u"De implementatie van wijzigingen behoort te worden beheerst door middel van formele procedures "
                 u"voor wijzigingsbeheer.",
            fragments=[
                Verifier(
                    identifier="12.05.01/01",
                    title=u"",
                    text=u"Er is aantoonbaar wijzigingsmanagement ingericht volgens gangbare best practices "
                         u"zoals ITIL.",
                ),
            ],
        ),
        Norm(
            identifier="12.05.02",
            title=u"Technische beoordeling van toepassingen na wijzigingen in het besturingssysteem",
            text=u"Bij wijzigingen in besturingssystemen behoren bedrijfskritische toepassingen te worden beoordeeld "
                 u"en getest om te bewerkstelligen dat er geen nadelige gevolgen zijn voor de activiteiten of "
                 u"beveiliging van de organisatie.",
            fragments=[
                Verifier(
                    identifier="12.05.02/01",
                    title=u"",
                    text=u"Van aanpassingen (zoals updates) aan softwarematige componenten van de technische "
                         u"infrastructuur wordt vastgesteld dat deze de juiste werking van de technische componenten "
                         u"niet in gevaar brengen.",
                ),
            ],
        ),
        Norm(
            identifier="12.05.03",
            title=u"Restricties op wijzigingen in programmatuurpakketten",
            text=u"Bij wijzigingen in besturingssystemen behoren bedrijfskritische toepassingen te worden "
                 u"beoordeeld en getest om te bewerkstelligen dat er geen nadelige gevolgen zijn voor de "
                 u"activiteiten of beveiliging van de organisatie.Wijzigingen in programmatuurpakketten behoren "
                 u"te worden ontmoedigd, te worden beperkt tot noodzakelijke wijzigingen, en alle wijzigingen "
                 u"behoren strikt te worden beheerst.",
            fragments=[
                Verifier(
                    identifier="12.05.03/01",
                    title=u"",
                    text=u"Bij het instellen van besturingsprogrammatuur en programmapakketten wordt uitgegaan van "
                         u"de aanwijzingen van de leverancier.",
                ),
            ],
        ),
        Norm(
            identifier="12.05.04",
            title=u"Uitlekken van informatie",
            text=u"Er behoort te worden voorkomen dat zich gelegenheden voordoen om informatie te laten uitlekken.",
            fragments=[
                Verifier(
                    identifier="12.05.04/01",
                    title=u"",
                    text=u"Op het grensvlak van een vertrouwde en een onvertrouwde omgeving vindt "
                         u"content-scanning plaats.",
                ),
            ],
        ),
        Norm(
            identifier="12.05.05",
            title=u"Uitbestede ontwikkeling van programmatuur",
            text=u"Uitbestede ontwikkeling van programmatuur behoort onder supervisie te staan van en te worden "
                 u"gecontroleerd door de organisatie.",
            fragments=[
                Verifier(
                    identifier="12.05.05/01",
                    title=u"",
                    text=u"Uitbestede ontwikkeling van programmatuur komt tot stand onder supervisie en "
                         u"verantwoordelijkheid van de uitbestedende organisatie. Er worden maatregelen "
                         u"getroffen om de kwaliteit en vertrouwelijkheid te borgen (bijv. stellen van "
                         u"veiligheidseisen, regelen van beschikbaarheid en eigendomsrecht van de code, "
                         u"certificatie, kwaliteitsaudits, testen en aansprakelijkheidsregelingen).",
                ),
            ],
        ),
    ],
)


S1206 = Section(
    identifier="12.06",
    title=u"Beheer van technische kwetsbaarheden",
    fragments=[
        Norm(
            identifier="12.06.01",
            title=u"Beheersing van technische kwetsbaarheden",
            text=u"Er behoort tijdig informatie te worden verkregen over technische kwetsbaarheden van de "
                 u"gebruikte informatiesystemen. De mate waarin de organisatie blootstaat aan dergelijke "
                 u"kwetsbaarheden behoort te worden geëvalueerd en er behoren geschikte maatregelen te worden "
                 u"genomen voor behandeling van daarmee samenhangende risico's.",
            fragments=[
                Verifier(
                    identifier="12.06.01/01",
                    title=u"",
                    text=u"Er is een proces ingericht voor het beheer van technische kwetsbaarheden; dit omvat "
                         u"minimaal periodieke penetratietests, risicoanalyses van kwetsbaarheden en patching.",
                ),
                Verifier(
                    identifier="12.06.01/02",
                    title=u"",
                    text=u"Van softwarematige voorzieningen van de technische infrastructuur kan (bij voorkeur "
                         u"geautomatiseerd) gecontroleerd worden of de laatste updates (patches) in zijn doorgevoerd. "
                         u"Het doorvoeren van een update vindt niet geautomatiseerd plaats, tenzij hier speciale "
                         u"afspraken over zijn met de leverancier.",
                ),
                Verifier(
                    identifier="12.06.01/03",
                    title=u"",
                    text=u"Indien een patch beschikbaar is, dienen de risico's verbonden met de installatie van de "
                         u"patch te worden geëvalueerd (de risico's verbonden met de kwetsbaarheid dienen vergeleken "
                         u"te worden met de risico's van het installeren van de patch).",
                ),
                Verifier(
                    identifier="12.06.01/04",
                    title=u"",
                    text=u"Updates/patches voor kwetsbaarheden waarvan de kans op misbruik hoog is en waarvan de "
                         u"schade hoog is worden zo spoedig mogelijk doorgevoerd, echter minimaal binnen één week. "
                         u"Minder kritische beveiligings-updates/patches moeten worden ingepland bij de eerst "
                         u"volgende onderhoudsronde.",
                ),
            ],
        ),
    ],
)


CH12 = Chapter(
    identifier="12",
    title=u"Verwerving, ontwikkeling en onderhoud van Informatiesystemen",
    fragments=[
        S1201,
        S1202,
        S1203,
        S1204,
        S1205,
        S1206,
    ]
)
