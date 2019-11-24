# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S0801 = Section(
    identifier="08.01",
    title="Verantwoordelijkheid voor bedrijfsmiddelen",
    text="Doelstelling: Bedrijfsmiddelen van de organisatie identifceren en passende verantwoordelijkheden "
         "ter bescherming defini&euml;ren.",
    fragments=[

        Norm(
            identifier="08.01.01",
            title="Inventariseren van bedrijfsmiddelen",
            text="Informatie, andere bedrijfsmiddelen die samenhangen met "
                 "informatie en informatieverwerkende faciliteiten behoren te worden ge&iuml;dentificeerd, en van deze "
                 "bedrijfsmiddelen behoort een inventaris te worden opgesteld en onderhouden.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.01.01/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="08.01.02",
            title="Eigendom van bedrijfsmiddelen",
            text="Bedrijfsmiddelen die in het inventarisoverzicht worden bijgehouden, "
                 "behoren een eigenaar te hebben.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.01.02/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="08.01.03",
            title="Aanvaardbaar gebruik van bedrijfsmiddelen",
            text="Voor het aanvaardbaar gebruik van informatie en van "
                 "bedrijfsmiddelen die samenhangen met informatie en informatieverwerkende faciliteiten behoren "
                 "regels te worden ge&iuml;dentificeerd, gedocumenteerd en ge&iuml;mplementeerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.01.03/01",
                    title="",
                    text="Alle medewerkers zijn aantoonbaar gewezen op de gedragsregels voor het gebruik van "
                         "bedrijfsmiddelen "
                         "en de Gedragsregeling voor de digitale werkomgeving",
                    bbn=1,
                ),
                Verifier(
                    identifier="08.01.03/02",
                    title="",
                    text="De gedragsregels voor het gebruik van bedrijfsmiddelen zijn voor extern personeel in het "
                         "contract vastgelegd overeenkomstig de "
                         "Gedragsregeling voor de digitale werkomgeving.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="08.01.04",
            title="Teruggeven van bedrijfsmiddelen",
            text="Alle medewerkers en externe gebruikers moeten alle "
                 "bedrijfsmiddelen van de organisatie die ze in hun bezit hebben bij be&euml;indiging van hun "
                 "dienstverband, contract of overeenkomst terug te geven.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.01.04/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S0802 = Section(
    identifier="08.02",
    title="Informatieclassificatie",
    text="Doelstelling: Bewerkstelligen dat informatie een passend  beschermingsniveau krijgt dat in overeenstemming "
         "is met het belang ervan voor de organisatie.",
    fragments=[

        Norm(
            identifier="08.02.01",
            title="Classificatie van informatie",
            text="Informatie behoort te worden geclassificeerd met betrekking tot "
                 "wettelijke eisen, waarde, belang en gevoeligheid voor onbevoegde bekendmaking of wijziging.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.02.01/01",
                    title="",
                    text="De informatie in alle informatiesystemen is door middel van een expliciete risicoafweging "
                         "geclassificeerd, zodat duidelijk is welke bescherming nodig is.",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="08.02.02",
            title="Informatie labelen",
            text="Om informatie te labelen behoort een passende reeks procedures te worden "
                 "ontwikkeld en ge&iuml;mplementeerd in overeenstemming met het informatieclassificatieschema dat is "
                 "vastgesteld door de organisatie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.02.02/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

        Norm(
            identifier="08.02.03",
            title="Behandelen van bedrijfsmiddelen",
            text="Procedures voor het behandelen van bedrijfsmiddelen behoren te "
                 "worden ontwikkeld en ge&iuml;mplementeerd in overeenstemming met het informatieclassificatieschema "
                 "dat is vastgesteld door de organisatie.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.02.03/01",
                    title="",
                    text="- conform norm -",
                    bbn=1,
                ),
            ],
        ),

    ],
)


S0803 = Section(
    identifier="08.03",
    title="Behandelen van media",
    text="Doelstelling: Onbevoegde openbaarmaking, wijziging, verwijdering of vernietiging van informatie die op "
         "media is opgeslagen voorkomen.",
    fragments=[

        Norm(
            identifier="08.03.01",
            title="Beheer van verwijderbare media",
            text="Voor het beheren van verwijderbare media behoren procedures te "
                 "worden ge&iuml;mplementeerd in overeenstemming met het classificatieschema dat door de organisatie "
                 "is vastgesteld.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="08.03.01/01",
                    title="",
                    text="Er is een verwijderinstructie waarin is opgenomen dat van herbruikbare media die de "
                         "organisatie verlaten de onnodige inhoud onherstelbaar verwijderd "
                         "(ISO27002 - implementatierichtlijn 8.3.1.a).",
                    bbn=1,
                ),
                Verifier(
                    identifier="08.03.01/02",
                    title="",
                    text="De wijze waarop "
                         "DepV "
                         "informatie is opgeslagen, voldoet aan "
                         "het gestelde in het VIR-BI: goedgekeurde producten "
                         "NBV.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="08.03.02",
            title="Verwijderen van media",
            text="Media behoren op een veilige en beveiligde manier te worden verwijderd als "
                 "ze niet langer nodig zijn, overeenkomstig formele procedures.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="08.03.02/01",
                    title="",
                    text="Media die vertrouwelijke informatie bevatten zijn opgeslagen op een plek die niet "
                         "toegankelijk is voor onbevoegden. Verwijdering vindt plaats op een veilige manier, "
                         "bijv. door verbranding of versnippering. Verwijdering van alleen gegevens is ook mogelijk "
                         "door het wissen van de gegevens voordat de media worden gebruikt voor een andere toepassing "
                         "in de organisatie (ISO27002 - implementatierichtlijn 8.3.2.a).",
                    bbn=2,
                ),
                Verifier(
                    identifier="08.03.02/02",
                    title="",
                    text="Voor het wissen van alle data op het medium, wordt de data onherstelbaar verwijderd, "
                         "bijvoorbeeld door minimaal twee keer te overschrijven met vaste data en &eacute;&eacute;n "
                         "keer met random data. Er wordt gecontroleerd of alle data onherstelbaar verwijderd is.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="08.03.03",
            title="Media fysiek overdragen",
            text="Media die informatie bevatten, behoren te worden beschermd tegen "
                 "onbevoegde toegang, misbruik of corruptie tijdens transport.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="08.03.03/01",
                    title="",
                    text="Er is voor de gehele organisatie beleid voor het fysiek transport van media vastgesteld.",
                    bbn=2,
                ),
                Verifier(
                    identifier="08.03.03/02",
                    title="",
                    text="Het gebruik van koeriers of transporteurs voor "
                         "DepV "
                         "of hoger geclassificeerde informatie voldoet aan "
                         "het gestelde in het VIR-BI.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH08 = Chapter(
    identifier="08",
    title="Beheer van bedrijfsmiddelen",
    fragments=[
        S0801,
        S0802,
        S0803,
    ]
)
