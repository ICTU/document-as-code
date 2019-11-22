# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S1601 = Section(
    identifier="16.01",
    title="Beheer van informatiebeveiligings-incidenten en -verbeteringen",
    text="Doelstelling: Een consistente en doeltrefende aanpak bewerkstel-ligen van het beheer van "
         "informatiebeveiligingsincidenten, met inbegrip van communicatie over beveiligingsgebeurtenissen en zwakke "
         "plekken in de beveiliging.",
    fragments=[

        Norm(
            identifier="16.01.01",
            title="Verantwoordelijkheden en procedures",
            text="Directieverantwoordelijkheden en -procedures behoren te worden vastgesteld om een snelle, "
                 "doeltreffende en ordelijke respons op informatiebeveiligingsincidenten te bewerkstelligen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="16.01.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="16.01.02",
            title="Rapportage van informatiebeveiligingsgebeurtenissen",
            text="Informatiebeveiligingsgebeurtenissen behoren zo snel mogelijk via de juiste leidinggevende niveaus "
                 "te worden gerapporteerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="16.01.02/01",
                    title="",
                    text="Er is een meldloket waar beveiligingsincidenten kunnen worden gemeld.",
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/02",
                    title="",
                    text="Er is een meldprocedure waarin de taken en verantwoordelijkheden van het meldloket staan "
                         "beschreven.",
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/03",
                    title="",
                    text="Alle medewerkers en contractanten hebben aantoonbaar kennis genomen van de "
                         "meldingsprocedure van incidenten.",
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/04",
                    title="",
                    text="Incidenten worden zo snel als mogelijk, maar in ieder geval binnen 24 uur na bekendwording, "
                         "gemeld bij het meldloket.",
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/05",
                    title="",
                    text="De proceseigenaar is verantwoordelijk voor het oplossen van beveiligingsincidenten.",
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/06",
                    title="",
                    text="De opvolging van incidenten wordt maandelijks gerapporteerd aan de verantwoordelijke.",
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/07",
                    title="",
                    text="Informatie afkomstig uit de responsible disclosure procedure zijn onderdeel van de "
                         "incidentrapportage.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="16.01.03",
            title="Rapportage van zwakke plekken in de informatiebeveiliging",
            text="Van medewerkers en contractanten die gebruikmaken van de informatiesystemen en -diensten van de "
                 "organisatie behoort te worden geëist dat zij de in systemen of diensten waargenomen of vermeende "
                 "zwakke plekken in de informatiebeveiliging registreren en rapporteren.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="16.01.03/01",
                    title="",
                    text="Een responsible disclosure procedure is gepubliceerd en ingericht.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="16.01.04",
            title="Beoordeling van en besluitvorming over informatiebeveiligingsgebeurtenissen",
            text="Informatiebeveiligingsgebeurtenissen behoren te worden beoordeeld en er behoort te worden "
                 "geoordeeld of zij moeten worden geclassificeerd als informatiebeveiligingsincidenten.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="16.01.04/01",
                    title="",
                    text="Informatiebeveiligingsincidenten die hebben geleid tot een vermoedelijk of mogelijk "
                         "opzettelijke inbreuk op de beschikbaarheid, vertrouwelijkheid of integriteit van "
                         "informatieverwerkende systemen, behoren zo snel mogelijk (binnen 72 uur) al dan niet "
                         "geautomatiseerd te worden gemeld aan het NCSC door of namens het department security "
                         "contact (DSC, operationele contactpersoon voor het NCSC) of de Chief Information "
                         "Security Officer (CISO).",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="16.01.05",
            title="Respons op informatiebeveiligingsincidenten",
            text="Op informatiebeveiligingsincidenten behoort te worden gereageerd in overeenstemming met de "
                 "gedocumenteerde procedures.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="16.01.05/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="16.01.06",
            title="Lering uit informatiebeveiligingsincidenten",
            text="Kennis die is verkregen door informatiebeveiligingsincidenten te analyseren en op te lossen behoort "
                 "te worden gebruikt om de waarschijnlijkheid of impact van toekomstige incidenten te verkleinen.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="16.01.06/01",
                    title="",
                    text="Beveiligingsincidenten worden geanalyseerd met als doel te leren en het voorkomen van "
                         "toekomstige beveiligingsincidenten.",
                    bbn=2,
                ),
                Verifier(
                    identifier="16.01.06/02",
                    title="",
                    text="De analyses van de beveiligingsincidenten worden gedeeld met de relevante partners om "
                         "herhaling en toekomstige incidenten te voorkomen.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="16.01.07",
            title="Verzamelen van bewijsmateriaal",
            text="De organisatie behoort procedures te definiëren en toe te passen voor het identificeren, "
                 "verzamelen, verkrijgen en bewaren van informatie die als bewijs kan dienen.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="16.01.07/01",
                    title="",
                    text="In geval van een (vermoed) informatiebeveiligingsincident is de bewaartermijn van de "
                         "gelogde incidentinformatie minimaal drie jaar.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH16 = Chapter(
    identifier="16",
    title="Beheer van informatiebeveiligingsincidenten",
    fragments=[
        S1601,
    ]
)

