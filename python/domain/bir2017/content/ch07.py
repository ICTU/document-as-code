# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S0701 = Section(
    identifier="07.01",
    title="Voorafgaand aan het dienstverband",
    text="Doelstelling: waarborgen dat medewerkers en contractanten hun verantwoordelijkheden begrijpen en geschikt "
         "zijn voor de rollen waarvoor zij in aanmerking komen.",
    fragments=[

        Norm(
            identifier="07.01.01",
            title="Screening",
            text="Verificatie van de achtergrond van alle kandidaten voor een dienstverband behoort te "
                 "worden uitgevoerd in overeenstemming met relevante wet- en regelgeving en ethische overwegingen "
                 "en behoort in verhouding te staan tot de bedrijfseisen, de classificatie van de informatie waartoe "
                 "toegang wordt verleend en de vastgestelde risico's te zijn.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="07.01.01/01",
                    title="",
                    text="Bij indiensttreding overleggen alle medewerkers (intern en extern) een specifiek voor de "
                         "functie verstrekte Verklaring Omtrent het Gedrag (VOG).",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="07.01.02",
            title="Arbeidsvoorwaarden",
            text="De contractuele overeenkomst met medewerkers en contractanten behoort hun "
                 "verantwoordelijkheden voor informatiebeveiliging en die van de organisatie te vermelden.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="07.01.02/01",
                    title="",
                    text="Alle medewerkers (intern en extern) zijn bij hun aanstelling of functiewisseling gewezen "
                         "op hun verantwoordelijkheden ten aanzien van informatiebeveiliging. De voor hen geldende "
                         "regelingen en instructies ten aanzien van informatiebeveiliging zijn eenvoudig "
                         "toegankelijk.",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S0702 = Section(
    identifier="07.02",
    title="Tijdens het dienstverband",
    text="Doelstelling: Ervoor zorgen dat medewerkers en contractanten zich bewust zijn van hun verantwoordelijkheden "
         "op het gebied van informatiebeveiliging en deze nakomen.",
    fragments=[

        Norm(
            identifier="07.02.01",
            title="Directieverantwoordelijkheden",
            text="De directie behoort van alle medewerkers en contractanten te eisen "
                 "dat ze informatiebeveiliging toepassen in overeenstemming met de vastgestelde beleidsregels en "
                 "procedures van de organisatie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="07.02.01/01",
                    title="",
                    text="Er is aansluiting bij de interne klokkenluidersregeling, zodat iedereen in staat is om "
                         "anoniem  en veilig beveiligingsissues te kunnen melden.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="07.02.02",
            title="Bewustzijn, opleiding en training ten aanzien van informatiebeveiliging",
            text="Alle medewerkers van de "
                 "organisatie en, voor zover relevant, contractanten behoren een passende bewustzijnsopleiding en "
                 "-training te krijgen en regelmatige bijscholing van beleidsregels en procedures van de organisatie, "
                 "voor zover relevant voor hun functie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="07.02.02/01",
                    title="",
                    text="Alle medewerkers hebben de verantwoordelijkheid bedrijfsinformatie te beschermen. Iedereen "
                         "kent de regels en verplichtingen met betrekking tot informatiebeveiliging en daar waar "
                         "relevant de speciale eisen voor gerubriceerde omgevingen",
                    bbn=1,
                ),
                Verifier(
                    identifier="07.02.02/02",
                    title="",
                    text="Alle medewerkers en contractanten die gebruikmaken van de informatiesystemen- en diensten "
                         "hebben binnen drie maanden na indiensttreding een training I-bewustzijn succesvol gevolgd.",
                    bbn=1,
                ),
                Verifier(
                    identifier="07.02.02/03",
                    title="",
                    text="Het management benadrukt bij aanstelling en interne overplaatsing en bijvoorbeeld in "
                         "werkoverleggen of in personeelsgesprekken bij haar medewerkers en contractanten het belang "
                         "van opleiding en training op het gebied van informatiebeveiliging en stimuleert hen actief "
                         "deze periodiek te volgen.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="07.02.03",
            title="Disciplinaire procedure",
            text="Er behoort een formele en gecommuniceerde disciplinaire procedure te "
                 "zijn om actie te ondernemen tegen medewerkers die een inbreuk hebben gepleegd op de "
                 "informatiebeveiliging.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="07.02.03/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S0703 = Section(
    identifier="07.03",
    title="Be&euml;indiging of wijziging van dienstverband",
    text="Doelstelling: Het beschermen van de belangen van de organisatie als onderdeel van de wijzigings- of "
         "be&euml;indigingsprocedure van het dienstverband.",
    fragments=[

        Norm(
            identifier="07.03.01",
            title="Be&euml;indiging of wijziging van verantwoordelijkheden van het dienstverband",
            text="Verantwoordelijkheden en "
                 "taken met betrekking tot informatiebeveiliging die van kracht blijven na be&euml;indiging of "
                 "wijziging van het dienstverband behoren te worden gedefinieerd, gecommuniceerd aan de medewerker of "
                 "contractant, en ten uitvoer gebracht.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="07.03.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


CH07 = Chapter(
    identifier="07",
    title="Veilig personeel",
    fragments=[
        S0701,
        S0702,
        S0703,
    ]
)
