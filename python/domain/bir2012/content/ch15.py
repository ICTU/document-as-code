# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S1501 = Section(
    identifier="15.01",
    title="Naleving van wettelijke voorschriften",
    fragments=[
        Norm(
            identifier="15.01.01",
            title="Identificatie van toepasselijke wetgeving",
            text="Alle relevante wettelijke en regelgevende eisen en contractuele verplichtingen en de benadering "
                 "van de organisatie in de naleving van deze eisen, behoren expliciet te worden vastgesteld, "
                 "gedocumenteerd en actueel te worden gehouden voor elk informatiesysteem en voor de organisatie.",
            fragments=[
                Verifier(
                    identifier="15.01.01/01",
                    title="",
                    text="Er is vastgesteld welke wetten en wettelijke maatregelen van toepassing zijn op de "
                         "organisatie of organisatieonderdelen.",
                ),
            ],
        ),
        Norm(
            identifier="15.01.02",
            title="Intellectuele eigendomsrechten (Intellectual Property Rights)",
            text="Er behoren geschikte procedures te worden ge�mplementeerd om te bewerkstelligen dat wordt voldaan "
                 "aan de wettelijke en regelgevende eisen en contractuele verplichtingen voor het gebruik van "
                 "materiaal waarop intellectuele eigendomsrechten kunnen berusten en het gebruik van programmatuur "
                 "waarop intellectuele eigendomsrechten berusten.",
            fragments=[
                Verifier(
                    identifier="15.01.02/01",
                    title="",
                    text="Er is toezicht op het naleven van wettelijke verplichtingen m.b.t. intellectueel eigendom, "
                         "auteursrechten en gebruiksrechten.",
                ),
            ],
        ),
        Norm(
            identifier="15.01.03",
            title="Bescherming van bedrijfsdocumenten",
            text="Belangrijke registraties behoren te worden beschermd tegen verlies, vernietiging en vervalsing, "
                 "overeenkomstig wettelijke en regelgevende eisen, contractuele verplichtingen en "
                 "bedrijfsmatige eisen.",
            fragments=[
                Verifier(
                    identifier="15.01.03/01",
                    title="",
                    text="- conform norm -",
                ),
            ],
        ),
        Norm(
            identifier="15.01.04",
            title="Bescherming van gegevens en geheimhouding van persoonsgegevens",
            text="De bescherming van gegevens en privacy behoort te worden bewerkstelligd overeenkomstig "
                 "relevante wetgeving, voorschriften en indien van toepassing contractuele bepalingen.",
            fragments=[
                Verifier(
                    identifier="15.01.04/01",
                    title="",
                    text="- conform norm -",
                ),
            ],
        ),
        Norm(
            identifier="15.01.05",
            title="Voorkomen van misbruik van IT voorzieningen",
            text="Gebruikers behoren ervan te worden weerhouden IT voorzieningen te gebruiken voor "
                 "onbevoegde doeleinden.",
            fragments=[
                Verifier(
                    identifier="15.01.05/01",
                    title="",
                    text="Er is een beleid met betrekking tot het gebruik van IT voorzieningen door gebruikers. "
                         "Dit beleid is bekendgemaakt en op de goede werking ervan wordt toegezien.",
                ),
            ],
        ),
        Norm(
            identifier="15.01.06",
            title="Voorschriften voor het gebruik van cryptografische beheersmaatregelen",
            text="Cryptografische beheersmaatregelen behoren overeenkomstig alle relevante overeenkomsten, wetten en "
                 "voorschriften te worden gebruikt.",
            fragments=[
                Verifier(
                    identifier="15.01.06/01",
                    title="",
                    text="Er is vastgesteld aan welke overeenkomsten, wetten en voorschriften de toepassing van "
                         "cryptografische technieken moet voldoen.",
                ),
            ],
        ),
    ],
)


S1502 = Section(
    identifier="15.02",
    title="Naleving van beveiligingsbeleid en -normen en technische naleving",
    fragments=[
        Norm(
            identifier="15.02.01",
            title="Naleving van beveiligingsbeleid en -normen",
            text="Managers behoren te bewerkstelligen dat alle beveiligingsprocedures die binnen hun "
                 "verantwoordelijkheid vallen correct worden uitgevoerd om naleving te bereiken van "
                 "beveiligingsbeleid en -normen.",
            fragments=[
                Verifier(
                    identifier="15.02.01/01",
                    title="",
                    text="Het lijnmanagement is verantwoordelijk voor uitvoering en beveiligingsprocedures en "
                         "toetsing daarop (o.a. jaarlijkse in control verklaring). Conform het BVR zorgt de "
                         "Beveiligingsambtenaar, namens de Secretaris Generaal, voor het toezicht op de uitvoering "
                         "van het beveiligingsbeleid. Daarbij behoren ook periodieke beveiligingsaudits. Deze kunnen "
                         "worden uitgevoerd door of vanwege de BVA dan wel door interne of externe auditteams.",
                ),
                Verifier(
                    identifier="15.02.01/02",
                    title="",
                    text="In de P&amp;C cyclus wordt gerapporteerd over informatiebeveiliging aan de hand van het in "
                         "control statement.",
                ),
            ],
        ),
        Norm(
            identifier="15.02.02",
            title="Controle op technische naleving",
            text="Informatiesystemen behoren regelmatig te worden gecontroleerd op naleving van implementatie van "
                 "beveiligingsnormen.",
            fragments=[
                Verifier(
                    identifier="15.02.02/01",
                    title="",
                    text="Informatiesystemen worden regelmatig gecontroleerd op naleving van beveiligingsnormen. "
                         "Dit kan door bijv. kwetsbaarheidsanalyses en penetratietesten.",
                ),
            ],
        ),
    ],
)


S1503 = Section(
    identifier="15.03",
    title="Overwegingen bij audits van informatiesystemen",
    fragments=[
        Norm(
            identifier="15.03.01",
            title="Beheersmaatregelen voor audits van informatiesystemen",
            text="Managers behoren te bewerkstelligen dat alle beveiligingsprocedures die binnen hun "
                 "verantwoordelijkheid vallen correct worden uitgevoerd om naleving te bereiken van "
                 "beveiligingsbeleid en -normen.",
            fragments=[
                Verifier(
                    identifier="15.03.01/01",
                    title="",
                    text="Eisen voor audits en andere activiteiten waarbij controles worden uitgevoerd op "
                         "productiesystemen, behoren zorgvuldig te worden gepland en goedgekeurd om het risico "
                         "van verstoring van bedrijfsprocessen tot een minimum te beperken.",
                ),
            ],
        ),
        Norm(
            identifier="15.03.02",
            title="Bescherming van hulpmiddelen voor audits van informatiesystemen",
            text="Managers behoren te bewerkstelligen dat alle beveiligingsprocedures die binnen hun "
                 "verantwoordelijkheid vallen correct worden uitgevoerd om naleving te bereiken van "
                 "beveiligingsbeleid en -normen.",
            fragments=[
                Verifier(
                    identifier="15.03.02/01",
                    title="",
                    text="Toegang tot hulpmiddelen voor audits van informatiesystemen behoort te worden beschermd "
                         "om mogelijk misbuik of compromittering te voorkomen.",
                ),
            ],
        ),
    ],
)


CH15 = Chapter(
    identifier="15",
    title="Naleving",
    fragments=[
        S1501,
        S1502,
        S1503,
    ]
)

