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


S1601 = Section(
    identifier="16.01",
    title=u"Beheer van informatiebeveiligings-incidenten en -verbeteringen",
    text=u"Doelstelling: Een consistente en doeltrefende aanpak bewerkstel-ligen van het beheer van "
         u"informatiebeveiligingsincidenten, met inbegrip van communicatie over beveiligingsgebeurtenissen en zwakke "
         u"plekken in de beveiliging.",
    fragments=[

        Norm(
            identifier="16.01.01",
            title=u"Verantwoordelijkheden en procedures",
            text=u"Directieverantwoordelijkheden en -procedures behoren te worden vastgesteld om een snelle, "
                 u"doeltreffende en ordelijke respons op informatiebeveiligingsincidenten te bewerkstelligen.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="16.01.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="16.01.02",
            title=u"Rapportage van informatiebeveiligingsgebeurtenissen",
            text=u"Informatiebeveiligingsgebeurtenissen behoren zo snel mogelijk via de juiste leidinggevende niveaus "
                 u"te worden gerapporteerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="16.01.02/01",
                    title=u"",
                    text=u"Er is een meldloket waar beveiligingsincidenten kunnen worden gemeld.",
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/02",
                    title=u"",
                    text=u"Er is een meldprocedure waarin de taken en verantwoordelijkheden van het meldloket staan "
                         u"beschreven.",
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/03",
                    title=u"",
                    text=u"Alle medewerkers en contractanten hebben aantoonbaar kennis genomen van de "
                         u"meldingsprocedure van incidenten.",
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/04",
                    title=u"",
                    text=u"Incidenten worden zo snel als mogelijk, maar in ieder geval binnen 24 uur na bekendwording, "
                         u"gemeld bij het meldloket.",
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/05",
                    title=u"",
                    text=u"De proceseigenaar is verantwoordelijk voor het oplossen van beveiligingsincidenten.",
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/06",
                    title=u"",
                    text=u"De opvolging van incidenten wordt maandelijks gerapporteerd aan de verantwoordelijke.",
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/07",
                    title=u"",
                    text=u"Informatie afkomstig uit de responsible disclosure procedure zijn onderdeel van de "
                         u"incidentrapportage.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="16.01.03",
            title=u"Rapportage van zwakke plekken in de informatiebeveiliging",
            text=u"Van medewerkers en contractanten die gebruikmaken van de informatiesystemen en -diensten van de "
                 u"organisatie behoort te worden geëist dat zij de in systemen of diensten waargenomen of vermeende "
                 u"zwakke plekken in de informatiebeveiliging registreren en rapporteren.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="16.01.03/01",
                    title=u"",
                    text=u"Een responsible disclosure procedure is gepubliceerd en ingericht.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="16.01.04",
            title=u"Beoordeling van en besluitvorming over informatiebeveiligingsgebeurtenissen",
            text=u"Informatiebeveiligingsgebeurtenissen behoren te worden beoordeeld en er behoort te worden "
                 u"geoordeeld of zij moeten worden geclassificeerd als informatiebeveiligingsincidenten.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="16.01.04/01",
                    title=u"",
                    text=u"Informatiebeveiligingsincidenten die hebben geleid tot een vermoedelijk of mogelijk "
                         u"opzettelijke inbreuk op de beschikbaarheid, vertrouwelijkheid of integriteit van "
                         u"informatieverwerkende systemen, behoren zo snel mogelijk (binnen 72 uur) al dan niet "
                         u"geautomatiseerd te worden gemeld aan het NCSC door of namens het department security "
                         u"contact (DSC, operationele contactpersoon voor het NCSC) of de Chief Information "
                         u"Security Officer (CISO).",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="16.01.05",
            title=u"Respons op informatiebeveiligingsincidenten",
            text=u"Op informatiebeveiligingsincidenten behoort te worden gereageerd in overeenstemming met de "
                 u"gedocumenteerde procedures.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="16.01.05/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="16.01.06",
            title=u"Lering uit informatiebeveiligingsincidenten",
            text=u"Kennis die is verkregen door informatiebeveiligingsincidenten te analyseren en op te lossen behoort "
                 u"te worden gebruikt om de waarschijnlijkheid of impact van toekomstige incidenten te verkleinen.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="16.01.06/01",
                    title=u"",
                    text=u"Beveiligingsincidenten worden geanalyseerd met als doel te leren en het voorkomen van "
                         u"toekomstige beveiligingsincidenten.",
                    bbn=2,
                ),
                Verifier(
                    identifier="16.01.06/02",
                    title=u"",
                    text=u"De analyses van de beveiligingsincidenten worden gedeeld met de relevante partners om "
                         u"herhaling en toekomstige incidenten te voorkomen.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="16.01.07",
            title=u"Verzamelen van bewijsmateriaal",
            text=u"De organisatie behoort procedures te definiëren en toe te passen voor het identificeren, "
                 u"verzamelen, verkrijgen en bewaren van informatie die als bewijs kan dienen.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="16.01.07/01",
                    title=u"",
                    text=u"In geval van een (vermoed) informatiebeveiligingsincident is de bewaartermijn van de "
                         u"gelogde incidentinformatie minimaal drie jaar.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH16 = Chapter(
    identifier="16",
    title=u"Beheer van informatiebeveiligingsincidenten",
    fragments=[
        S1601,
    ]
)

