# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S1801 = Section(
    identifier="18.01",
    title="Naleving van wetelijke en contractuele eisen",
    text="Doelstelling: Voorkomen van schendingen van wetelijke, statutaire, regelgevende of contractuele "
         "verplichtingen betrefende informatiebeveiliging en beveiligingseisen.",
    fragments=[

        Norm(
            identifier="18.01.01",
            title="Vaststellen van toepasselijke wetgeving en contractuele eisen",
            text="Alle relevante wettelijke statutaire, regelgevende, contractuele eisen en de aanpak van de "
                 "organisatie om aan deze eisen te voldoen behoren voor elk informatiesysteem en de organisatie "
                 "expliciet te worden vastgesteld, gedocumenteerd en actueel gehouden.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.01.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="18.01.02",
            title="Intellectuele-eigendomsrechten",
            text="Om de naleving van wettelijke, regelgevende en contractuele eisen in verband met "
                 "intellectueleeigendomsrechten en het gebruik van eigendomssoftwareproducten te waarborgen behoren "
                 "passende procedures te worden geïmplementeerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.01.02/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="18.01.03",
            title="Beschermen van registraties",
            text="Registraties behoren in overeenstemming met wettelijke, regelgevende, contractuele en bedrijfseisen "
                 "te worden beschermd tegen verlies, vernietiging, vervalsing, onbevoegde toegang en onbevoegde "
                 "vrijgave.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="18.01.03/01",
                    title="",
                    text="De proceseigenaar heeft per soort informatie inzichtelijk gemaakt wat de bewaartermijn is.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="18.01.04",
            title="Privacy en bescherming van persoonsgegevens",
            text="Privacy en bescherming van persoonsgegevens behoren, voor zover van toepassing, te worden "
                 "gewaarborgd in overeenstemming met relevante wet- en regelgeving.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.01.04/01",
                    title="",
                    text="In overeenstemming met de AVG heeft iedere organisatie een Functionaris Gegevensbescherming "
                         "(FG) met voldoende mandaat om zijn/haar functie uit te voeren.",
                    bbn=1,
                ),
                Verifier(
                    identifier="18.01.04/02",
                    title="",
                    text="Organisaties controleren regelmatig de naleving van de privacy regels en "
                         "informatieverwerking en ?procedures binnen haar verantwoordelijkheidsgebied aan de hand van "
                         "de desbetreffende beleidsregels, normen en andere eisen betreffende beveiliging.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="18.01.05",
            title="Voorschriften voor het gebruik van cryptografische beheersmaatregelen",
            text="Cryptografische beheersmaatregelen behoren te worden toegepast in overeenstemming met alle "
                 "relevante overeenkomsten, wet- en regelgeving.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.01.05/01",
                    title="",
                    text="Cryptografische beheersmaatregelen moeten expliciet aansluiten bij de standaarden op de "
                         "pas-toe-of-leg-uit lijst van het forum standaardisatie.",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1802 = Section(
    identifier="18.02",
    title="Informatiebeveiligingsbeoordelingen",
    text="Doelstelling: Verzekeren dat informatiebeveiliging wordt  geïmplementeerd en uitgevoerd in overeenstemming "
         "met de beleidsregels en procedures van de organisatie.",
    fragments=[

        Norm(
            identifier="18.02.01",
            title="Onafhankelijke beoordeling van informatiebeveiliging",
            text="De aanpak van de organisatie ten aanzien van het beheer van informatiebeveiliging en de "
                 "implementatie ervan (bijv. beheerdoelstellingen, beheersmaatregelen, beleidsregels, processen en "
                 "procedures voor informatiebeveiliging), behoren onafhankelijk en met geplande tussenpozen of zodra "
                 "zich belangrijke veranderingen voordoen te worden beoordeeld.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.02.01/01",
                    title="",
                    text="Er is een information security information system (ISMS) waarmee aantoonbaar de gehele "
                         "plan-do-check-act cyclus op gestructureerde wijze wordt afgedekt.",
                    bbn=2,
                ),
                Verifier(
                    identifier="18.02.01/02",
                    title="",
                    text="Er is een vastgesteld auditplan waarin jaarlijks keuzes worden gemaakt voor welke systemen "
                         "welk soort beveiligingsaudits worden uitgevoerd.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="18.02.02",
            title="Naleving van beveiligingsbeleid en -normen",
            text="De directie behoort regelmatig de naleving van de informatieverwerking en - procedures binnen haar "
                 "verantwoordelijkheidsgebied te beoordelen aan de hand van de desbetreffende beleidsregels, normen "
                 "en andere eisen betreffende beveiliging.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.02.02/01",
                    title="",
                    text="In de P&C cyclus wordt gerapporteerd over informatiebeveiliging, resulterend in een "
                         "jaarlijks af te geven In Control Verklaring (ICV) over de informatiebeveiliging. Indien "
                         "voldoende herkenbaar kan de ICV voor informatiebeveiliging onderdeel zijn van de reguliere, "
                         "generieke verantwoording.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="18.02.03",
            title="Beoordeling van technische naleving",
            text="Informatiesystemen behoren regelmatig te worden beoordeeld op naleving van de beleidsregels en "
                 "normen van de organisatie voor informatiebeveiliging.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.02.03/01",
                    title="",
                    text="Informatiesystemen worden jaarlijks gecontroleerd op technische naleving van "
                         "beveiligingsnormen en risico?s ten aanzien van de feitelijke veiligheid. Dit kan bijv door "
                         "(geautomatiseerde) kwetsbaarheidsanalyses of pentesten.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH18 = Chapter(
    identifier="18",
    title="Naleving",
    fragments=[
        S1801,
        S1802,
    ]
)

