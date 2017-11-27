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

S1801 = Section(
    identifier="18.01",
    title=u"",
    fragments=[

        Norm(
            identifier="18.01.01",
            title=u"",
            text=u"Vaststellen van toepasselijke wetgeving en contractuele eisen: Alle relevante wettelijke "
                 u"statutaire, regelgevende, contractuele eisen en de aanpak van de organisatie om aan deze eisen "
                 u"te voldoen behoren voor elk informatiesysteem en de organisatie expliciet te worden vastgesteld, "
                 u"gedocumenteerd en actueel gehouden.",
            fragments=[
            ],
        ),

        Norm(
            identifier="18.01.02",
            title=u"",
            text=u"Intellectuele-eigendomsrechten: Om de naleving van wettelijke, regelgevende en contractuele eisen "
                 u"in verband met intellectueleeigendomsrechten en het gebruik van eigendomssoftwareproducten te "
                 u"waarborgen behoren passende procedures te worden geïmplementeerd.",
            fragments=[
            ],
        ),

        Norm(
            identifier="18.01.03",
            title=u"",
            text=u"Beschermen van registraties: Registraties behoren in overeenstemming met wettelijke, regelgevende, "
                 u"contractuele en bedrijfseisen te worden beschermd tegen verlies, vernietiging, vervalsing, "
                 u"onbevoegde toegang en onbevoegde vrijgave.",
            fragments=[
                Verifier(
                    identifier="18.01.03/01",
                    title=u"",
                    text=u"De proceseigenaar heeft per soort informatie inzichtelijk gemaakt wat de bewaartermijn is.",
                ),
            ],
        ),

        Norm(
            identifier="18.01.04",
            title=u"",
            text=u"Privacy en bescherming van persoonsgegevens: Privacy en bescherming van persoonsgegevens "
                 u"behoren, voor zover van toepassing, te worden gewaarborgd in overeenstemming met "
                 u"relevante wet- en regelgeving.",
            fragments=[
                Verifier(
                    identifier="18.01.04/01",
                    title=u"",
                    text=u"In overeenstemming met de AVG heeft iedere organisatie een Functionaris Gegevensbescherming "
                         u"(FG) met voldoende mandaat om zijn/haar functie uit te voeren.",
                ),
                Verifier(
                    identifier="18.01.04/02",
                    title=u"",
                    text=u"Organisaties controleren regelmatig de naleving van de privacy regels en "
                         u"informatieverwerking en ?procedures binnen haar verantwoordelijkheidsgebied aan de hand van "
                         u"de desbetreffende beleidsregels, normen en andere eisen betreffende beveiliging.",
                ),
            ],
        ),

        Norm(
            identifier="18.01.05",
            title=u"",
            text=u"Voorschriften voor het gebruik van cryptografische beheersmaatregelen: Cryptografische "
                 u"beheersmaatregelen behoren te worden toegepast in overeenstemming met alle relevante "
                 u"overeenkomsten, wet- en regelgeving.",
            fragments=[
                Verifier(
                    identifier="18.01.05/01",
                    title=u"",
                    text=u"Cryptografische beheersmaatregelen moeten expliciet aansluiten bij de standaarden op de "
                         u"pas-toe-of-leg-uit lijst van het forum standaardisatie.",
                ),
            ],
        ),

    ],
)


S1802 = Section(
    identifier="18.02",
    title=u"",
    fragments=[

        Norm(
            identifier="18.02.01",
            title=u"",
            text=u"Onafhankelijke beoordeling van informatiebeveiliging: De aanpak van de organisatie ten aanzien van "
                 u"het beheer van informatiebeveiliging en de implementatie ervan (bijv. beheerdoelstellingen, "
                 u"beheersmaatregelen, beleidsregels, processen en procedures voor informatiebeveiliging), "
                 u"behoren onafhankelijk en met geplande tussenpozen of zodra zich belangrijke veranderingen voordoen "
                 u"te worden beoordeeld.",
            fragments=[
                Verifier(
                    identifier="18.02.01/01",
                    title=u"",
                    text=u"Er is een information security information system (ISMS) waarmee aantoonbaar de gehele "
                         u"plan-do-check-act cyclus op gestructureerde wijze wordt afgedekt.",
                ),
                Verifier(
                    identifier="18.02.01/02",
                    title=u"",
                    text=u"Er is een vastgesteld auditplan waarin jaarlijks keuzes worden gemaakt voor welke systemen "
                         u"welk soort beveiligingsaudits worden uitgevoerd.",
                ),
            ],
        ),

        Norm(
            identifier="18.02.02",
            title=u"",
            text=u"Naleving van beveiligingsbeleid en -normen: De directie behoort regelmatig de naleving van de "
                 u"informatieverwerking en - procedures binnen haar verantwoordelijkheidsgebied te beoordelen aan "
                 u"de hand van de desbetreffende beleidsregels, normen en andere eisen betreffende beveiliging.",
            fragments=[
                Verifier(
                    identifier="18.02.02/01",
                    title=u"",
                    text=u"In de P&C cyclus wordt gerapporteerd over informatiebeveiliging, resulterend in een "
                         u"jaarlijks af te geven In Control Verklaring (ICV) over de informatiebeveiliging. Indien "
                         u"voldoende herkenbaar kan de ICV voor informatiebeveiliging onderdeel zijn van de reguliere, "
                         u"generieke verantwoording.",
                ),
            ],
        ),

        Norm(
            identifier="18.02.03",
            title=u"",
            text=u"Beoordeling van technische naleving: Informatiesystemen behoren regelmatig te worden beoordeeld op "
                 u"naleving van de beleidsregels en normen van de organisatie voor informatiebeveiliging.",
            fragments=[
                Verifier(
                    identifier="18.02.03/01",
                    title=u"",
                    text=u"Informatiesystemen worden jaarlijks gecontroleerd op technische naleving van "
                         u"beveiligingsnormen en risico?s ten aanzien van de feitelijke veiligheid. Dit kan bijv door "
                         u"(geautomatiseerde) kwetsbaarheidsanalyses of pentesten.",
                ),
            ],
        ),

    ],
)


CH18 = Chapter(
    identifier="18",
    title=u"Compliance; with internal requirements, such as policies, and with external requirements, such as laws",
    fragments=[
        S1801,
        S1802,
    ]
)

