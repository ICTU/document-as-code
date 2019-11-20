# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function

from domain.document.model.chapter import Chapter
from domain.document.model.section import Section
from domain.norm_document.model.norm import Norm
from domain.norm_document.model.verifier import Verifier


S1801 = Section(
    identifier="18.01",
    title=u"Naleving van wetelijke en contractuele eisen",
    text=u"Doelstelling: Voorkomen van schendingen van wetelijke, statutaire, regelgevende of contractuele "
         u"verplichtingen betrefende informatiebeveiliging en beveiligingseisen.",
    fragments=[

        Norm(
            identifier="18.01.01",
            title=u"Vaststellen van toepasselijke wetgeving en contractuele eisen",
            text=u"Alle relevante wettelijke statutaire, regelgevende, contractuele eisen en de aanpak van de "
                 u"organisatie om aan deze eisen te voldoen behoren voor elk informatiesysteem en de organisatie "
                 u"expliciet te worden vastgesteld, gedocumenteerd en actueel gehouden.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.01.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="18.01.02",
            title=u"Intellectuele-eigendomsrechten",
            text=u"Om de naleving van wettelijke, regelgevende en contractuele eisen in verband met "
                 u"intellectueleeigendomsrechten en het gebruik van eigendomssoftwareproducten te waarborgen behoren "
                 u"passende procedures te worden geïmplementeerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.01.02/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="18.01.03",
            title=u"Beschermen van registraties",
            text=u"Registraties behoren in overeenstemming met wettelijke, regelgevende, contractuele en bedrijfseisen "
                 u"te worden beschermd tegen verlies, vernietiging, vervalsing, onbevoegde toegang en onbevoegde "
                 u"vrijgave.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="18.01.03/01",
                    title=u"",
                    text=u"De proceseigenaar heeft per soort informatie inzichtelijk gemaakt wat de bewaartermijn is.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="18.01.04",
            title=u"Privacy en bescherming van persoonsgegevens",
            text=u"Privacy en bescherming van persoonsgegevens behoren, voor zover van toepassing, te worden "
                 u"gewaarborgd in overeenstemming met relevante wet- en regelgeving.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.01.04/01",
                    title=u"",
                    text=u"In overeenstemming met de AVG heeft iedere organisatie een Functionaris Gegevensbescherming "
                         u"(FG) met voldoende mandaat om zijn/haar functie uit te voeren.",
                    bbn=1,
                ),
                Verifier(
                    identifier="18.01.04/02",
                    title=u"",
                    text=u"Organisaties controleren regelmatig de naleving van de privacy regels en "
                         u"informatieverwerking en ?procedures binnen haar verantwoordelijkheidsgebied aan de hand van "
                         u"de desbetreffende beleidsregels, normen en andere eisen betreffende beveiliging.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="18.01.05",
            title=u"Voorschriften voor het gebruik van cryptografische beheersmaatregelen",
            text=u"Cryptografische beheersmaatregelen behoren te worden toegepast in overeenstemming met alle "
                 u"relevante overeenkomsten, wet- en regelgeving.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.01.05/01",
                    title=u"",
                    text=u"Cryptografische beheersmaatregelen moeten expliciet aansluiten bij de standaarden op de "
                         u"pas-toe-of-leg-uit lijst van het forum standaardisatie.",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S1802 = Section(
    identifier="18.02",
    title=u"Informatiebeveiligingsbeoordelingen",
    text=u"Doelstelling: Verzekeren dat informatiebeveiliging wordt  geïmplementeerd en uitgevoerd in overeenstemming "
         u"met de beleidsregels en procedures van de organisatie.",
    fragments=[

        Norm(
            identifier="18.02.01",
            title=u"Onafhankelijke beoordeling van informatiebeveiliging",
            text=u"De aanpak van de organisatie ten aanzien van het beheer van informatiebeveiliging en de "
                 u"implementatie ervan (bijv. beheerdoelstellingen, beheersmaatregelen, beleidsregels, processen en "
                 u"procedures voor informatiebeveiliging), behoren onafhankelijk en met geplande tussenpozen of zodra "
                 u"zich belangrijke veranderingen voordoen te worden beoordeeld.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.02.01/01",
                    title=u"",
                    text=u"Er is een information security information system (ISMS) waarmee aantoonbaar de gehele "
                         u"plan-do-check-act cyclus op gestructureerde wijze wordt afgedekt.",
                    bbn=2,
                ),
                Verifier(
                    identifier="18.02.01/02",
                    title=u"",
                    text=u"Er is een vastgesteld auditplan waarin jaarlijks keuzes worden gemaakt voor welke systemen "
                         u"welk soort beveiligingsaudits worden uitgevoerd.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="18.02.02",
            title=u"Naleving van beveiligingsbeleid en -normen",
            text=u"De directie behoort regelmatig de naleving van de informatieverwerking en - procedures binnen haar "
                 u"verantwoordelijkheidsgebied te beoordelen aan de hand van de desbetreffende beleidsregels, normen "
                 u"en andere eisen betreffende beveiliging.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.02.02/01",
                    title=u"",
                    text=u"In de P&C cyclus wordt gerapporteerd over informatiebeveiliging, resulterend in een "
                         u"jaarlijks af te geven In Control Verklaring (ICV) over de informatiebeveiliging. Indien "
                         u"voldoende herkenbaar kan de ICV voor informatiebeveiliging onderdeel zijn van de reguliere, "
                         u"generieke verantwoording.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="18.02.03",
            title=u"Beoordeling van technische naleving",
            text=u"Informatiesystemen behoren regelmatig te worden beoordeeld op naleving van de beleidsregels en "
                 u"normen van de organisatie voor informatiebeveiliging.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.02.03/01",
                    title=u"",
                    text=u"Informatiesystemen worden jaarlijks gecontroleerd op technische naleving van "
                         u"beveiligingsnormen en risico?s ten aanzien van de feitelijke veiligheid. Dit kan bijv door "
                         u"(geautomatiseerde) kwetsbaarheidsanalyses of pentesten.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH18 = Chapter(
    identifier="18",
    title=u"Naleving",
    fragments=[
        S1801,
        S1802,
    ]
)

