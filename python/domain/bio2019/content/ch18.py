# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.bio.model.norm import Norm
from domain.bio.model.verifier import Verifier
from domain.document.model.chapter import Chapter
from domain.document.model.section import Section


CH18S01 = Section(
    identifier="18.01",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="18.01.03",
            title=u"TITLE",
            text=u"""
Beschermen van registraties;
Registraties behoren in overeenstemming met wettelijke, regelgevende, contractuele en bedrijfseisen te worden beschermd tegen verlies, vernietiging, vervalsing, onbevoegde toegang en onbevoegde vrijgave.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="18.01.03/01",
                    title=u"",
                    text=u"""
De proceseigenaar heeft per soort informatie inzichtelijk gemaakt wat de bewaartermijn is.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="18.01.04",
            title=u"TITLE",
            text=u"""
Privacy en bescherming van persoonsgegevens;
Privacy en bescherming van persoonsgegevens behoren, voor zover van toepassing, te worden gewaarborgd in overeenstemming met relevante wet- en regelgeving.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.01.04/01",
                    title=u"",
                    text=u"""
In overeenstemming met de AVG heeft iedere organisatie een Functionaris Gegevensbescherming (FG) met voldoende mandaat om zijn/haar functie uit te voeren.
                    """,
                    bbn=1,
                ),
                Verifier(
                    identifier="18.01.04/02",
                    title=u"",
                    text=u"""
Organisaties controleren regelmatig de naleving van de privacy regels en informatieverwerking en –procedures binnen haar verantwoordelijkheidsgebied aan de hand van de desbetreffende beleidsregels, normen en andere eisen betreffende beveiliging.
                    """,
                    bbn=2,
                )
            ],
        )
    ],
)


CH18S02 = Section(
    identifier="18.02",
    title=u"TITLE",
    text=u"text",
    fragments=[
        Norm(
            identifier="18.02.01",
            title=u"TITLE",
            text=u"""
Onafhankelijke beoordeling van informatiebeveiliging;
De aanpak van de organisatie ten aanzien van het beheer van informatiebeveiliging en de implementatie ervan (bijv. beheerdoelstellingen, beheersmaatregelen, beleidsregels, processen en procedures voor informatiebeveiliging), behoren onafhankelijk en met geplande tussenpozen of zodra zich belangrijke veranderingen voordoen te worden beoordeeld.
            """,
            bbn=2,
            fragments=[
                Verifier(
                    identifier="18.02.01/01",
                    title=u"",
                    text=u"""
Er is een information security information system (ISMS) waarmee aantoonbaar de gehele plan-do-check-act cyclus op gestructureerde wijze wordt afgedekt.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="18.02.01/02",
                    title=u"",
                    text=u"""
Er is een vastgesteld auditplan waarin jaarlijks keuzes worden gemaakt voor welke systemen welk soort beveiligingsaudits worden uitgevoerd.
                    """,
                    bbn=2,
                )
            ],
        ),

        Norm(
            identifier="18.02.02",
            title=u"TITLE",
            text=u"""
Naleving van beveiligingsbeleid en -normen;
De directie behoort regelmatig de naleving van de informatieverwerking en - procedures binnen haar verantwoordelijkheidsgebied te beoordelen aan de hand van de desbetreffende beleidsregels, normen en andere eisen betreffende beveiliging.
            """,
            bbn=1,
            fragments=[
                Verifier(
                    identifier="18.02.02/01",
                    title=u"",
                    text=u"""
In de P&C cyclus wordt gerapporteerd over informatiebeveiliging, resulterend in een jaarlijks af te geven In Control Verklaring (ICV) over de informatiebeveiliging. Indien voldoende herkenbaar kan de ICV voor informatiebeveiliging onderdeel zijn van de reguliere, generieke verantwoording.
                    """,
                    bbn=1,
                )
            ],
        ),

        Norm(
            identifier="18.02.03",
            title=u"TITLE",
            text=u"""
Beoordeling van technische naleving;
Informatiesystemen behoren regelmatig te worden beoordeeld op naleving van de beleidsregels en normen van de organisatie voor informatiebeveiliging.
            """,
            bbn=666,
            fragments=[
                Verifier(
                    identifier="18.02.03/01",
                    title=u"",
                    text=u"""
Informatiesystemen worden jaarlijks gecontroleerd op technische naleving van beveiligingsnormen en risico’s ten aanzien van de feitelijke veiligheid. Dit kan bijvoorbeeld door (geautomatiseerde) kwetsbaarheidsanalyses of pentesten.
                    """,
                    bbn=2,
                ),
                Verifier(
                    identifier="18.02.03/01",
                    title=u"",
                    text=u"""
Informatiesystemen worden jaarlijks gecontroleerd op technische naleving van beveiligingsnormen en risico’s ten aanzien van de feitelijke veiligheid. Dit kan bijvoorbeeld door (geautomatiseerde) kwetsbaarheidsanalyses of pentesten.
                    """,
                    bbn=666,
                ),
                Verifier(
                    identifier="18.02.03/01",
                    title=u"",
                    text=u"""
Informatiesystemen worden jaarlijks gecontroleerd op technische naleving van beveiligingsnormen en risico’s ten aanzien van de feitelijke veiligheid. Dit kan bijvoorbeeld door (geautomatiseerde) kwetsbaarheidsanalyses of pentesten.
                    """,
                    bbn=666,
                ),
                Verifier(
                    identifier="18.02.03/01",
                    title=u"",
                    text=u"""
Informatiesystemen worden jaarlijks gecontroleerd op technische naleving van beveiligingsnormen en risico’s ten aanzien van de feitelijke veiligheid. Dit kan bijvoorbeeld door (geautomatiseerde) kwetsbaarheidsanalyses of pentesten.
                    """,
                    bbn=666,
                )
            ],
        )
    ],
)


CH18 = Chapter(
    identifier="18",
    title=u"TITLE",
    fragments=[
        CH18S01,
        CH18S02
    ]
)
