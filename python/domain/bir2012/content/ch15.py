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

S1501 = Section(
    identifier="15.01",
    title=u"Naleving van wettelijke voorschriften",
    fragments=[
        Norm(
            identifier="15.01.01",
            title=u"Identificatie van toepasselijke wetgeving",
            text=u"Alle relevante wettelijke en regelgevende eisen en contractuele verplichtingen en de benadering "
                 u"van de organisatie in de naleving van deze eisen, behoren expliciet te worden vastgesteld, "
                 u"gedocumenteerd en actueel te worden gehouden voor elk informatiesysteem en voor de organisatie.",
            fragments=[
                Verifier(
                    identifier="15.01.01/01",
                    title=u"",
                    text=u"Er is vastgesteld welke wetten en wettelijke maatregelen van toepassing zijn op de "
                         u"organisatie of organisatieonderdelen.",
                ),
            ],
        ),
        Norm(
            identifier="15.01.02",
            title=u"Intellectuele eigendomsrechten (Intellectual Property Rights)",
            text=u"Er behoren geschikte procedures te worden geïmplementeerd om te bewerkstelligen dat wordt voldaan "
                 u"aan de wettelijke en regelgevende eisen en contractuele verplichtingen voor het gebruik van "
                 u"materiaal waarop intellectuele eigendomsrechten kunnen berusten en het gebruik van programmatuur "
                 u"waarop intellectuele eigendomsrechten berusten.",
            fragments=[
                Verifier(
                    identifier="15.01.02/01",
                    title=u"",
                    text=u"Er is toezicht op het naleven van wettelijke verplichtingen m.b.t. intellectueel eigendom, "
                         u"auteursrechten en gebruiksrechten.",
                ),
            ],
        ),
        Norm(
            identifier="15.01.03",
            title=u"Bescherming van bedrijfsdocumenten",
            text=u"Belangrijke registraties behoren te worden beschermd tegen verlies, vernietiging en vervalsing, "
                 u"overeenkomstig wettelijke en regelgevende eisen, contractuele verplichtingen en "
                 u"bedrijfsmatige eisen.",
            fragments=[
                Verifier(
                    identifier="15.01.03/01",
                    title=u"",
                    text=u"- conform norm -",
                ),
            ],
        ),
        Norm(
            identifier="15.01.04",
            title=u"Bescherming van gegevens en geheimhouding van persoonsgegevens",
            text=u"De bescherming van gegevens en privacy behoort te worden bewerkstelligd overeenkomstig "
                 u"relevante wetgeving, voorschriften en indien van toepassing contractuele bepalingen.",
            fragments=[
                Verifier(
                    identifier="15.01.04/01",
                    title=u"",
                    text=u"- conform norm -",
                ),
            ],
        ),
        Norm(
            identifier="15.01.05",
            title=u"Voorkomen van misbruik van IT voorzieningen",
            text=u"Gebruikers behoren ervan te worden weerhouden IT voorzieningen te gebruiken voor "
                 u"onbevoegde doeleinden.",
            fragments=[
                Verifier(
                    identifier="15.01.05/01",
                    title=u"",
                    text=u"Er is een beleid met betrekking tot het gebruik van IT voorzieningen door gebruikers. "
                         u"Dit beleid is bekendgemaakt en op de goede werking ervan wordt toegezien.",
                ),
            ],
        ),
        Norm(
            identifier="15.01.06",
            title=u"Voorschriften voor het gebruik van cryptografische beheersmaatregelen",
            text=u"Cryptografische beheersmaatregelen behoren overeenkomstig alle relevante overeenkomsten, wetten en "
                 u"voorschriften te worden gebruikt.",
            fragments=[
                Verifier(
                    identifier="15.01.06/01",
                    title=u"",
                    text=u"Er is vastgesteld aan welke overeenkomsten, wetten en voorschriften de toepassing van "
                         u"cryptografische technieken moet voldoen.",
                ),
            ],
        ),
    ],
)


S1502 = Section(
    identifier="15.02",
    title=u"Naleving van beveiligingsbeleid en -normen en technische naleving",
    fragments=[
        Norm(
            identifier="15.02.01",
            title=u"Naleving van beveiligingsbeleid en -normen",
            text=u"Managers behoren te bewerkstelligen dat alle beveiligingsprocedures die binnen hun "
                 u"verantwoordelijkheid vallen correct worden uitgevoerd om naleving te bereiken van "
                 u"beveiligingsbeleid en -normen.",
            fragments=[
                Verifier(
                    identifier="15.02.01/01",
                    title=u"",
                    text=u"Het lijnmanagement is verantwoordelijk voor uitvoering en beveiligingsprocedures en "
                         u"toetsing daarop (o.a. jaarlijkse in control verklaring). Conform het BVR zorgt de "
                         u"Beveiligingsambtenaar, namens de Secretaris Generaal, voor het toezicht op de uitvoering "
                         u"van het beveiligingsbeleid. Daarbij behoren ook periodieke beveiligingsaudits. Deze kunnen "
                         u"worden uitgevoerd door of vanwege de BVA dan wel door interne of externe auditteams.",
                ),
                Verifier(
                    identifier="15.02.01/02",
                    title=u"",
                    text=u"In de P&amp;C cyclus wordt gerapporteerd over informatiebeveiliging aan de hand van het in "
                         u"control statement.",
                ),
            ],
        ),
        Norm(
            identifier="15.02.02",
            title=u"Controle op technische naleving",
            text=u"Informatiesystemen behoren regelmatig te worden gecontroleerd op naleving van implementatie van "
                 u"beveiligingsnormen.",
            fragments=[
                Verifier(
                    identifier="15.02.02/01",
                    title=u"",
                    text=u"Informatiesystemen worden regelmatig gecontroleerd op naleving van beveiligingsnormen. "
                         u"Dit kan door bijv. kwetsbaarheidsanalyses en penetratietesten.",
                ),
            ],
        ),
    ],
)


S1503 = Section(
    identifier="15.03",
    title=u"Overwegingen bij audits van informatiesystemen",
    fragments=[
        Norm(
            identifier="15.03.01",
            title=u"Beheersmaatregelen voor audits van informatiesystemen",
            text=u"Managers behoren te bewerkstelligen dat alle beveiligingsprocedures die binnen hun "
                 u"verantwoordelijkheid vallen correct worden uitgevoerd om naleving te bereiken van "
                 u"beveiligingsbeleid en -normen.",
            fragments=[
                Verifier(
                    identifier="15.03.01/01",
                    title=u"",
                    text=u"Eisen voor audits en andere activiteiten waarbij controles worden uitgevoerd op "
                         u"productiesystemen, behoren zorgvuldig te worden gepland en goedgekeurd om het risico "
                         u"van verstoring van bedrijfsprocessen tot een minimum te beperken.",
                ),
            ],
        ),
        Norm(
            identifier="15.03.02",
            title=u"Bescherming van hulpmiddelen voor audits van informatiesystemen",
            text=u"Managers behoren te bewerkstelligen dat alle beveiligingsprocedures die binnen hun "
                 u"verantwoordelijkheid vallen correct worden uitgevoerd om naleving te bereiken van "
                 u"beveiligingsbeleid en -normen.",
            fragments=[
                Verifier(
                    identifier="15.03.02/01",
                    title=u"",
                    text=u"Toegang tot hulpmiddelen voor audits van informatiesystemen behoort te worden beschermd "
                         u"om mogelijk misbuik of compromittering te voorkomen.",
                ),
            ],
        ),
    ],
)


CH15 = Chapter(
    identifier="15",
    title=u"Naleving",
    fragments=[
        S1501,
        S1502,
        S1503,
    ]
)

