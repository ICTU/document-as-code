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


CH16S01 = Section(
    identifier="16.01",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="16.01.02",
            title=u"TITLE",
            text=u"""
Rapportage van informatiebeveiligingsgebeurtenissen;
Informatiebeveiligingsgebeurtenissen behoren zo snel mogelijk via de juiste leidinggevende niveaus te worden gerapporteerd.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="16.01.02/01",
                    title=u"",
                    text=u"""
Er is een meldloket waar beveiligingsincidenten kunnen worden gemeld.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/02",
                    title=u"",
                    text=u"""
Er is een meldprocedure waarin de taken en verantwoordelijkheden van het meldloket staan beschreven.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/03",
                    title=u"",
                    text=u"""
Alle medewerkers en contractanten hebben aantoonbaar kennis genomen van de meldingsprocedure van incidenten.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/04",
                    title=u"",
                    text=u"""
Incidenten worden zo snel als mogelijk, maar in ieder geval binnen 24 uur na bekendwording, gemeld bij het meldloket.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/05",
                    title=u"",
                    text=u"""
De proceseigenaar is verantwoordelijk voor het oplossen van beveiligingsincidenten.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/06",
                    title=u"",
                    text=u"""
De opvolging van incidenten wordt maandelijks gerapporteerd aan de verantwoordelijke.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="16.01.02/07",
                    title=u"",
                    text=u"""
Informatie afkomstig uit de responsible disclosure procedure zijn onderdeel van de incidentrapportage.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="16.01.03",
            title=u"TITLE",
            text=u"""
Rapportage van zwakke plekken in de informatiebeveiliging;
Van medewerkers en contractanten die gebruikmaken van de informatiesystemen en -diensten van de organisatie behoort te worden geëist dat zij de in systemen of diensten waargenomen of vermeende zwakke plekken in de informatiebeveiliging registreren en rapporteren.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="16.01.03/01",
                    title=u"",
                    text=u"""
Een responsible disclosure procedure is gepubliceerd en ingericht.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="16.01.04",
            title=u"TITLE",
            text=u"""
Beoordeling van en besluitvorming over informatiebeveiligingsgebeurtenissen; Informatiebeveiligingsgebeurtenissen behoren te worden beoordeeld en er behoort te worden geoordeeld of zij moeten worden geclassificeerd als informatiebeveiligingsincidenten.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="16.01.04/01",
                    title=u"",
                    text=u"""
Informatiebeveiligingsincidenten die hebben geleid tot een vermoedelijk of mogelijk opzettelijke inbreuk op de beschikbaarheid, vertrouwelijkheid of integriteit van informatie verwerkende systemen, behoren zo snel mogelijk (binnen 72 uur) al dan niet geautomatiseerd te worden gemeld aan het NCSC (alleen voor rijksoverheidsorganisaties) of de sectorale CERT.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="16.01.06",
            title=u"TITLE",
            text=u"""
Lering uit informatiebeveiligingsincidenten;
Kennis die is verkregen door informatiebeveiligingsincidenten te analyseren en op te lossen behoort te worden gebruikt om de waarschijnlijkheid of impact van toekomstige incidenten te verkleinen.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="16.01.06/01",
                    title=u"",
                    text=u"""
Beveiligingsincidenten worden geanalyseerd met als doel te leren en het voorkomen van toekomstige beveiligingsincidenten.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="16.01.06/02",
                    title=u"",
                    text=u"""
De analyses van de beveiligingsincidenten worden gedeeld met de relevante partners om herhaling en toekomstige incidenten te voorkomen.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="16.01.07",
            title=u"TITLE",
            text=u"""
Verzamelen van bewijsmateriaal;
De organisatie behoort procedures te definiëren en toe te passen voor het identificeren, verzamelen, verkrijgen en bewaren van informatie die als bewijs kan dienen.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="16.01.07/01",
                    title=u"",
                    text=u"""
Beveiligingsincidenten worden geanalyseerd met als doel te leren en het voorkomen van toekomstige beveiligingsincidenten.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH16 = Chapter(
    identifier="16",
    title=u"TITLE",
    fragments=[
        CH16S01
    ]
)
