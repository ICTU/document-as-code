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

S0701 = Section(
    identifier="07.01",
    title=u"",
    fragments=[

        Norm(
            identifier="07.01.01",
            title=u"",
            text=u"Screening: Verificatie van de achtergrond van alle kandidaten voor een dienstverband behoort te "
                 u"worden uitgevoerd in overeenstemming met relevante wet- en regelgeving en ethische overwegingen "
                 u"en behoort in verhouding te staan tot de bedrijfseisen, de classificatie van de informatie waartoe "
                 u"toegang wordt verleend en de vastgestelde risico?s te zijn.",
            fragments=[
                Verifier(
                    identifier="07.01.01/01",
                    title=u"",
                    text=u"Bij indiensttreding overleggen alle medewerkers (intern en extern) een specifiek voor de "
                         u"functie verstrekte Verklaring Omtrent het Gedrag (VOG).",
                ),
            ],
        ),

        Norm(
            identifier="07.01.02",
            title=u"",
            text=u"Arbeidsvoorwaarden: De contractuele overeenkomst met medewerkers en contractanten behoort hun "
                 u"verantwoordelijkheden voor informatiebeveiliging en die van de organisatie te vermelden.",
            fragments=[
                Verifier(
                    identifier="07.01.02/01",
                    title=u"",
                    text=u"Alle medewerkers (intern en extern) zijn bij hun aanstelling of functiewisseling gewezen "
                         u"op hun verantwoordelijkheden ten aanzien van informatiebeveiliging. De voor hen geldende "
                         u"regelingen en instructies ten aanzien van informatiebeveiliging zijn eenvoudig "
                         u"toegankelijk.",
                ),
            ],
        ),

    ],
)


S0702 = Section(
    identifier="07.02",
    title=u"",
    fragments=[

        Norm(
            identifier="07.02.01",
            title=u"",
            text=u"Directieverantwoordelijkheden: De directie behoort van alle medewerkers en contractanten te eisen "
                 u"dat ze informatiebeveiliging toepassen in overeenstemming met de vastgestelde beleidsregels en "
                 u"procedures van de organisatie.",
            fragments=[
                Verifier(
                    identifier="07.02.01/01",
                    title=u"",
                    text=u"Er is aansluiting bij de interne klokkenluidersregeling, zodat iedereen in staat is om "
                         u"anoniem  en veilig beveiligingsissues te kunnen melden.",
                ),
            ],
        ),

        Norm(
            identifier="07.02.02",
            title=u"",
            text=u"Bewustzijn, opleiding en training ten aanzien van informatiebeveiliging: Alle medewerkers van de "
                 u"organisatie en, voor zover relevant, contractanten behoren een passende bewustzijnsopleiding en "
                 u"-training te krijgen en regelmatige bijscholing van beleidsregels en procedures van de organisatie, "
                 u"voor zover relevant voor hun functie.",
            fragments=[
                Verifier(
                    identifier="07.02.02/01",
                    title=u"",
                    text=u"Alle medewerkers hebben de verantwoordelijkheid bedrijfsinformatie te beschermen. Iedereen "
                         u"kent de regels en verplichtingen met betrekking tot informatiebeveiliging en daar waar "
                         u"relevant de speciale eisen voor gerubriceerde omgevingen",
                ),
                Verifier(
                    identifier="07.02.02/02",
                    title=u"",
                    text=u"Alle medewerkers en contractanten die gebruikmaken van de informatiesystemen- en diensten "
                         u"hebben binnen drie maanden na indiensttreding een training I-bewustzijn succesvol gevolgd.",
                ),
                Verifier(
                    identifier="07.02.02/03",
                    title=u"",
                    text=u"Het management benadrukt bij aanstelling en interne overplaatsing en bijvoorbeeld in "
                         u"werkoverleggen of in personeelsgesprekken bij haar medewerkers en contractanten het belang "
                         u"van opleiding en training op het gebied van informatiebeveiliging en stimuleert hen actief "
                         u"deze periodiek te volgen.",
                ),
            ],
        ),

        Norm(
            identifier="07.02.03",
            title=u"",
            text=u"Disciplinaire procedure: Er behoort een formele en gecommuniceerde disciplinaire procedure te "
                 u"zijn om actie te ondernemen tegen medewerkers die een inbreuk hebben gepleegd op de "
                 u"informatiebeveiliging.",
            fragments=[
                Verifier(
                    identifier="07.02.03/01",
                    title=u"",
                    text=u"- conform norm -",
                ),
            ],
        ),

    ],
)


S0703 = Section(
    identifier="07.03",
    title=u"",
    fragments=[

        Norm(
            identifier="07.03.01",
            title=u"",
            text=u"Beëindiging of wijziging van verantwoordelijkheden van het dienstverband: Verantwoordelijkheden en "
                 u"taken met betrekking tot informatiebeveiliging die van kracht blijven na beëindiging of wijziging "
                 u"van het dienstverband behoren te worden gedefinieerd, gecommuniceerd aan de medewerker of "
                 u"contractant, en ten uitvoer gebracht.",
            fragments=[
                Verifier(
                    identifier="07.03.01/01",
                    title=u"",
                    text=u"- conform norm -",
                ),
            ],
        ),

    ],
)


CH07 = Chapter(
    identifier="07",
    title=u"Human resource security",
    fragments=[
        S0701,
        S0702,
        S0703,
    ]
)
