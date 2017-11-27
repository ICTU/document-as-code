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

S1601 = Section(
    identifier="16.01",
    title=u"",
    fragments=[

        Norm(
            identifier="16.01.01",
            title=u"",
            text=u"Verantwoordelijkheden en procedures: Directieverantwoordelijkheden en -procedures behoren te worden "
                 u"vastgesteld om een snelle, doeltreffende en ordelijke respons op informatiebeveiligingsincidenten "
                 u"te bewerkstelligen.",
            fragments=[
            ],
        ),

        Norm(
            identifier="16.01.02",
            title=u"",
            text=u"Rapportage van informatiebeveiligingsgebeurtenissen: Informatiebeveiligingsgebeurtenissen behoren "
                 u"zo snel mogelijk via de juiste leidinggevende niveaus te worden gerapporteerd.",
            fragments=[
                Verifier(
                    identifier="16.01.02/01",
                    title=u"",
                    text=u"Er is een meldloket waar beveiligingsincidenten kunnen worden gemeld.",
                ),
                Verifier(
                    identifier="16.01.02/02",
                    title=u"",
                    text=u"Er is een meldprocedure waarin de taken en verantwoordelijkheden van het meldloket staan "
                         u"beschreven.",
                ),
                Verifier(
                    identifier="16.01.02/03",
                    title=u"",
                    text=u"Alle medewerkers en contractanten hebben aantoonbaar kennis genomen van de "
                         u"meldingsprocedure van incidenten.",
                ),
                Verifier(
                    identifier="16.01.02/04",
                    title=u"",
                    text=u"Incidenten worden zo snel als mogelijk, maar in ieder geval binnen 24 uur na bekendwording, "
                         u"gemeld bij het meldloket.",
                ),
                Verifier(
                    identifier="16.01.02/05",
                    title=u"",
                    text=u"De proceseigenaar is verantwoordelijk voor het oplossen van beveiligingsincidenten.",
                ),
                Verifier(
                    identifier="16.01.02/06",
                    title=u"",
                    text=u"De opvolging van incidenten wordt maandelijks gerapporteerd aan de verantwoordelijke.",
                ),
                Verifier(
                    identifier="16.01.02/07",
                    title=u"",
                    text=u"Informatie afkomstig uit de responsible disclosure procedure zijn onderdeel van de "
                         u"incidentrapportage.",
                ),
            ],
        ),

        Norm(
            identifier="16.01.03",
            title=u"",
            text=u"Rapportage van zwakke plekken in de informatiebeveiliging: Van medewerkers en contractanten die "
                 u"gebruikmaken van de informatiesystemen en -diensten van de organisatie behoort te worden geëist dat "
                 u"zij de in systemen of diensten waargenomen of vermeende zwakke plekken in de informatiebeveiliging "
                 u"registreren en rapporteren.",
            fragments=[
                Verifier(
                    identifier="16.01.03/01",
                    title=u"",
                    text=u"Een responsible disclosure procedure is gepubliceerd en ingericht.",
                ),
            ],
        ),

        Norm(
            identifier="16.01.04",
            title=u"",
            text=u"Beoordeling van en besluitvorming over informatiebeveiligingsgebeurtenissen: "
                 u"Informatiebeveiligingsgebeurtenissen behoren te worden beoordeeld en er behoort te worden "
                 u"geoordeeld of zij moeten worden geclassificeerd als informatiebeveiligingsincidenten.",
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
                ),
            ],
        ),

        Norm(
            identifier="16.01.05",
            title=u"",
            text=u"Respons op informatiebeveiligingsincidenten: Op informatiebeveiligingsincidenten behoort te worden "
                 u"gereageerd in overeenstemming met de gedocumenteerde procedures.",
            fragments=[
            ],
        ),

        Norm(
            identifier="16.01.06",
            title=u"",
            text=u"Lering uit informatiebeveiligingsincidenten: Kennis die is verkregen door "
                 u"informatiebeveiligingsincidenten te analyseren en op te lossen behoort te worden gebruikt om de "
                 u"waarschijnlijkheid of impact van toekomstige incidenten te verkleinen.",
            fragments=[
                Verifier(
                    identifier="16.01.06/01",
                    title=u"",
                    text=u"Beveiligingsincidenten worden geanalyseerd met als doel te leren en het voorkomen van "
                         u"toekomstige beveiligingsincidenten.",
                ),
                Verifier(
                    identifier="16.01.06/02",
                    title=u"",
                    text=u"De analyses van de beveiligingsincidenten worden gedeeld met de relevante partners om "
                         u"herhaling en toekomstige incidenten te voorkomen.",
                ),
            ],
        ),

        Norm(
            identifier="16.01.07",
            title=u"",
            text=u"Verzamelen van bewijsmateriaal: De organisatie behoort procedures te definiëren en toe te passen "
                 u"voor het identificeren, verzamelen, verkrijgen en bewaren van informatie die als bewijs kan dienen.",
            fragments=[
                Verifier(
                    identifier="16.01.07/01",
                    title=u"",
                    text=u"In geval van een (vermoed) informatiebeveiligingsincident is de bewaartermijn van de "
                         u"gelogde incidentinformatie minimaal drie jaar.",
                ),
            ],
        ),

    ],
)


CH16 = Chapter(
    identifier="16",
    title=u"Information security incident management",
    fragments=[
        S1601,
    ]
)

