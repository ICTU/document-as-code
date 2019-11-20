# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function

from domain.document.model.chapter import Chapter
from domain.document.model.section import Section
from domain.norm_document.model.norm import Norm
from domain.norm_document.model.verifier import Verifier


S0801 = Section(
    identifier="08.01",
    title=u"Verantwoordelijkheid voor bedrijfsmiddelen",
    text=u"Doelstelling: Bedrijfsmiddelen van de organisatie identifceren en passende verantwoordelijkheden "
         u"ter bescherming defniëren.",
    fragments=[

        Norm(
            identifier="08.01.01",
            title=u"Inventariseren van bedrijfsmiddelen",
            text=u"Informatie, andere bedrijfsmiddelen die samenhangen met "
                 u"informatie en informatieverwerkende faciliteiten behoren te worden geïdentificeerd, en van deze "
                 u"bedrijfsmiddelen behoort een inventaris te worden opgesteld en onderhouden.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.01.01/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="08.01.02",
            title=u"Eigendom van bedrijfsmiddelen",
            text=u"Bedrijfsmiddelen die in het inventarisoverzicht worden bijgehouden, "
                 u"behoren een eigenaar te hebben.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.01.02/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="08.01.03",
            title=u"Aanvaardbaar gebruik van bedrijfsmiddelen",
            text=u"Voor het aanvaardbaar gebruik van informatie en van "
                 u"bedrijfsmiddelen die samenhangen met informatie en informatieverwerkende faciliteiten behoren "
                 u"regels te worden geïdentificeerd, gedocumenteerd en geïmplementeerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.01.03/01",
                    title=u"",
                    text=u"Alle medewerkers zijn aantoonbaar gewezen op de gedragsregels voor het gebruik van "
                         u"bedrijfsmiddelen en de Gedragsregeling voor de digitale werkomgeving",
                    bbn=1,
                ),
                Verifier(
                    identifier="08.01.03/02",
                    title=u"",
                    text=u"De gedragsregels voor het gebruik van bedrijfsmiddelen zijn voor extern personeel in het "
                         u"contract vastgelegd overeenkomstig de Gedragsregeling voor de digitale werkomgeving.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="08.01.04",
            title=u"Teruggeven van bedrijfsmiddelen",
            text=u"Alle medewerkers en externe gebruikers moeten alle "
                 u"bedrijfsmiddelen van de organisatie die ze in hun bezit hebben bij beëindiging van hun "
                 u"dienstverband, contract of overeenkomst terug te geven.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.01.04/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S0802 = Section(
    identifier="08.02",
    title=u"Informatieclassificatie",
    text=u"Doelstelling: Bewerkstelligen dat informatie een passend  beschermingsniveau krijgt dat in overeenstemming "
         u"is met het belang ervan voor de organisatie.",
    fragments=[

        Norm(
            identifier="08.02.01",
            title=u"Classificatie van informatie",
            text=u"Informatie behoort te worden geclassificeerd met betrekking tot "
                 u"wettelijke eisen, waarde, belang en gevoeligheid voor onbevoegde bekendmaking of wijziging.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.02.01/01",
                    title=u"",
                    text=u"De informatie in alle informatiesystemen is door middel van een expliciete risicoafweging "
                         u"geclassificeerd, zodat duidelijk is welke bescherming nodig is.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="08.02.02",
            title=u"Informatie labelen",
            text=u"Om informatie te labelen behoort een passende reeks procedures te worden "
                 u"ontwikkeld en geïmplementeerd in overeenstemming met het informatieclassificatieschema dat is "
                 u"vastgesteld door de organisatie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.02.02/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="08.02.03",
            title=u"Behandelen van bedrijfsmiddelen",
            text=u"Procedures voor het behandelen van bedrijfsmiddelen behoren te "
                 u"worden ontwikkeld en geïmplementeerd in overeenstemming met het informatieclassificatieschema dat "
                 u"is vastgesteld door de organisatie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.02.03/01",
                    title=u"",
                    text=u"- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S0803 = Section(
    identifier="08.03",
    title=u"Behandelen van media",
    text=u"Doelstelling: Onbevoegde openbaarmaking, wijziging, verwijdering of vernietiging van informatie die op "
         u"media is opgeslagen voorkomen.",
    fragments=[

        Norm(
            identifier="08.03.01",
            title=u"Beheer van verwijderbare media",
            text=u"Voor het beheren van verwijderbare media behoren procedures te "
                 u"worden geïmplementeerd in overeenstemming met het classificatieschema dat door de organisatie "
                 u"is vastgesteld.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.03.01/01",
                    title=u"",
                    text=u"Er is een verwijderinstructie waarin is opgenomen dat van herbruikbare media die de "
                         u"organisatie verlaten de onnodige inhoud onherstelbaar verwijderd "
                         u"(ISO27002 ? implementatierichtlijn 8.3.1.a).",
                    bbn=1,
                ),
                Verifier(
                    identifier="08.03.01/02",
                    title=u"",
                    text=u"De wijze waarop DepV informatie is opgeslagen, voldoet aan het gestelde in het VIR-BI: "
                         u"goedgekeurde producten NBV.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="08.03.02",
            title=u"Verwijderen van media",
            text=u"Media behoren op een veilige en beveiligde manier te worden verwijderd als "
                 u"ze niet langer nodig zijn, overeenkomstig formele procedures.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="08.03.02/01",
                    title=u"",
                    text=u"Media die vertrouwelijke informatie bevatten zijn opgeslagen op een plek die niet "
                         u"toegankelijk is voor onbevoegden. Verwijdering vindt plaats op een veilige manier, "
                         u"bijv. door verbranding of versnippering. Verwijdering van alleen gegevens is ook mogelijk "
                         u"door het wissen van de gegevens voordat de media worden gebruikt voor een andere toepassing "
                         u"in de organisatie (ISO27002 ? implementatierichtlijn 8.3.2.a).",
                    bbn=2,
                ),
                Verifier(
                    identifier="08.03.02/02",
                    title=u"",
                    text=u"Voor het wissen van alle data op het medium, wordt de data onherstelbaar verwijderd, "
                         u"bijvoorbeeld door minimaal twee keer te overschrijven met vaste data en één keer met "
                         u"random data. Er wordt gecontroleerd of alle data onherstelbaar verwijderd is.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="08.03.03",
            title=u"Media fysiek overdragen",
            text=u"Media die informatie bevatten, behoren te worden beschermd tegen "
                 u"onbevoegde toegang, misbruik of corruptie tijdens transport.",
            bbn=2,
            fragments=[

                Verifier(
                    identifier="08.03.03/01",
                    title=u"",
                    text=u"Er is voor de gehele organisatie beleid voor het fysiek transport van media vastgesteld.",
                    bbn=2,
                ),

                Verifier(
                    identifier="08.03.03/02",
                    title=u"",
                    text=u"Het gebruik van koeriers of transporteurs voor DepV of hoger geclassificeerde informatie "
                         u"voldoet aan het gestelde in het VIR-BI.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH08 = Chapter(
    identifier="08",
    title=u"Beheer van bedrijfsmiddelen",
    fragments=[
        S0801,
        S0802,
        S0803,
    ]
)
