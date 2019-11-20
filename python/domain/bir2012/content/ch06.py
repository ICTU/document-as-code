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


S0601 = Section(
    identifier="06.01",
    title=u"Interne organisatie",
    fragments=[
        Norm(
            identifier="06.01.01",
            title=u"Betrokkenheid van de directie bij beveiliging",
            text=u"De directie behoort actief beveiliging binnen de organisatie te ondersteunen door duidelijk "
                 u"richting te geven, betrokkenheid te tonen en expliciet verantwoordelijkheden voor "
                 u"informatiebeveiliging toe te kennen en te erkennen.",
            fragments=[
                Verifier(
                    identifier="06.01.01/01",
                    title=u"",
                    text=u"Het lijnmanagement waarborgt dat de informatiebeveiligingsdoelstellingen worden "
                         u"vastgesteld, voldoen aan de kaders zoals gesteld in dit document en zijn geïntegreerd in "
                         u"de relevante processen. Dit gebeurt door één keer per jaar opzet, bestaan en werking van "
                         u"de IB-maatregelen te bespreken in het overleg van de departementsleiding en hiervan "
                         u"verslag te doen."
                ),
            ],
        ),
        Norm(
            identifier="06.01.02",
            title=u"Coördineren van beveiliging",
            text=u"Activiteiten voor informatiebeveiliging behoren te worden gecoördineerd door vertegenwoordigers "
                 u"uit verschillende delen van de organisatie met relevante rollen en functies.",
            fragments=[
                Verifier(
                    identifier="06.01.02/01",
                    title=u"",
                    text=u"De rollen van BVA, BVC en het lijnmanagement zijn beschreven in het "
                         u"Beveiligingsvoorschrift Rijksdienst 2005."
                ),
            ],
        ),
        Norm(
            identifier="06.01.03",
            title=u"Verantwoordelijkheden",
            text=u"Alle verantwoordelijkheden voor informatiebeveiliging behoren duidelijk te zijn gedefinieerd.",
            fragments=[
                Verifier(
                    identifier="06.01.03/01",
                    title=u"",
                    text=u"Elke lijnmanager is verantwoordelijk voor de integrale beveiliging van zijn of haar "
                         u"dienstonderdeel."
                ),
            ],
        ),
        Norm(
            identifier="06.01.04",
            title=u"Goedkeuringsproces voor ICT-voorzieningen",
            text=u"Er behoort een goedkeuringsproces voor nieuwe ICT-voorzieningen te worden vastgesteld en "
                 u"geïmplementeerd.",
            fragments=[
                Verifier(
                    identifier="06.01.04/01",
                    title=u"",
                    text=u"Er is een goedkeuringsproces voor nieuwe IT-voorzieningen en wijzigingen in "
                         u"IT-voorzieningen."
                ),
            ],
        ),
        Norm(
            identifier="06.01.05",
            title=u"Geheimhoudingsovereenkomst",
            text=u"Eisen voor vertrouwelijkheid of geheimhoudingsovereenkomst die een weerslag vormen van de behoefte "
                 u"van de organisatie aan bescherming van informatie behoren te worden vastgesteld en regelmatig te "
                 u"worden beoordeeld.",
            fragments=[
                Verifier(
                    identifier="06.01.05/01",
                    title=u"",
                    text=u"De algemene geheimhoudingsplicht voor ambtenaren is geregeld in de Ambtenarenwet art. 125a, "
                         u"lid 3. Daarnaast dienen personen die te maken hebben met Bijzondere Informatie een "
                         u"geheimhoudingsverklaring te ondertekenen (zie VIRBI); daaronder valt ook de departementaal "
                         u"vertrouwelijke informatie. Hierbij wordt tevens vastgelegd dat na beëindiging van de "
                         u"functie, de betreffende persoon gehouden blijft aan die geheimhouding."
                ),
            ],
        ),
        Norm(
            identifier="06.01.06",
            title=u"Contact met overheidsinstanties",
            text=u"Er behoren geschikte contacten met relevante overheidsinstanties te worden onderhouden.",
            fragments=[
                Verifier(
                    identifier="06.01.06/01",
                    title=u"",
                    text=u"Het lijnmanagement stelt vast in welke gevallen en door wie er contacten met autoriteiten "
                         u"(brandweer, toezichthouders, enz.) wordt onderhouden."
                ),
            ],
        ),
        Norm(
            identifier="06.01.07",
            title=u"Contact met speciale belangengroepen",
            text=u"Er behoren geschikte contacten met speciale belangengroepen of andere specialistische platforms "
                 u"voor beveiliging en professionele organisaties te worden onderhouden.",
            fragments=[
                Verifier(
                    identifier="06.01.07/01",
                    title=u"",
                    text=u"IB-specifieke informatie van relevante expertisegroepen, leveranciers van hardware, "
                         u"software en diensten wordt gebruikt om de informatiebeveiliging te verbeteren."
                ),
            ],
        ),
        Norm(
            identifier="06.01.08",
            title=u"Beoordeling van het informatiebeveiligingsbeleid",
            text=u"De benadering van de organisatie voor het beheer van informatiebeveiliging en de implementatie "
                 u"daarvan (d.w.z. beheersdoelstellingen, beheersmaatregelen, beleid, processen en procedures voor "
                 u"informatiebeveiliging) behoren onafhankelijk en met geplande tussenpozen te worden beoordeeld, of "
                 u"zodra zich significante wijzigingen voordoen in de implementatie van de beveiliging.",
            fragments=[
                Verifier(
                    identifier="06.01.08/01",
                    title=u"",
                    text=u"Het informatiebeveiligingsbeleid wordt minimaal één keer in de drie jaar geëvalueerd "
                         u"(door een onafhankelijke deskundige) en desgewenst bijgesteld."
                ),
                Verifier(
                    identifier="06.01.08/02",
                    title=u"",
                    text=u"Periodieke beveiligingsaudits worden uitgevoerd in opdracht van het lijnmanagement."
                ),
                Verifier(
                    identifier="06.01.08/03",
                    title=u"",
                    text=u"Over het functioneren van de informatiebeveiliging wordt, conform de P&amp;C cyclus, "
                         u"jaarlijks gerapporteerd aan het lijnmanagement."
                ),
            ],
        ),
    ],
)

S0602 = Section(
    identifier="06.02",
    title=u"Externe Partijen",
    fragments=[
        Norm(
            identifier="06.02.01",
            title=u"Identificatie van risico's die betrekking hebben op externe partijen",
            text=u"De risico's voor de informatie en ICT-voorzieningen van de organisatie vanuit bedrijfsprocessen "
                 u"waarbij externe partijen betrokken zijn, behoren te worden geïdentificeerd en er behoren geschikte "
                 u"beheersmaatregelen te worden geïmplementeerd voordat toegang wordt verleend.",
            fragments=[
                Verifier(
                    identifier="06.02.01/01",
                    title=u"",
                    text=u"Informatiebeveiliging is aantoonbaar (op basis van een risicoafweging) meegewogen bij het "
                         u"besluit een externe partij wel of niet in te schakelen."
                ),
                Verifier(
                    identifier="06.02.01/02",
                    title=u"",
                    text=u"Voorafgaand aan het afsluiten van een contract voor uitbesteding of externe inhuur is "
                         u"bepaald welke toegang (fysiek, netwerk of tot gegevens) de externe partij(en) moet(en) "
                         u"hebben om de in het contract overeen te komen opdracht uit te voeren en welke "
                         u"noodzakelijke beveiligingsmaatregelen hiervoor nodig zijn."
                ),
                Verifier(
                    identifier="06.02.01/03",
                    title=u"",
                    text=u"Voorafgaand aan het afsluiten van een contract voor uitbesteding of externe inhuur is "
                         u"bepaald welke waarde en gevoeligheid de informatie (bijv. risicoklasse van WBP of "
                         u"vertrouwelijkheidklasse volgens VIRBI) heeft waarmee de derde partij in aanraking kan "
                         u"komen en of hierbij eventueel aanvullende beveiligingsmaatregelen nodig zijn."
                ),
                Verifier(
                    identifier="06.02.01/04",
                    title=u"",
                    text=u"Voorafgaand aan het afsluiten van een contract voor uitbesteding en externe inhuur is "
                         u"bepaald hoe geauthenticeerde en geautoriseerde toegang vastgesteld wordt."
                ),
                Verifier(
                    identifier="06.02.01/05",
                    title=u"",
                    text=u"Indien externe partijen systemen beheren waarin persoonsgegevens verwerkt worden, wordt "
                         u"een bewerkerovereenkomst (conform WBP artikel 14) afgesloten."
                ),
                Verifier(
                    identifier="06.02.01/06",
                    title=u"",
                    text=u"Er is in contracten met externe partijen vastgelegd welke beveiligingsmaatregelen vereist "
                         u"zijn, dat deze door de externe partij zijn getroffen en worden nageleefd en dat "
                         u"beveiligingsincidenten onmiddellijk worden gerapporteerd. Ook wordt beschreven hoe die "
                         u"beveiligingsmaatregelen door de uitbestedende partij te controleren zijn (bijv. audits en "
                         u"penetratietests) en hoe het toezicht is geregeld."
                ),
            ],
        ),
        Norm(
            identifier="06.02.02",
            title=u"Beveiliging behandelen in de omgang met klanten",
            text=u"Alle geïdentificeerde beveiligingseisen behoren te worden behandeld voordat klanten toegang wordt "
                 u"verleend tot de informatie of bedrijfsmiddelen van de organisatie.",
            fragments=[
                Verifier(
                    identifier="06.02.02/01",
                    title=u"",
                    text=u"Alle noodzakelijke beveiligingseisen worden op basis van een risicoafweging vastgesteld en "
                         u"geïmplementeerd voordat aan gebruikers toegang tot informatie op bedrijfsmiddelen wordt "
                         u"verleend."
                ),
            ],
        ),
        Norm(
            identifier="06.02.03",
            title=u"Beveiliging behandelen in overeenkomsten met een derde partij",
            text=u"In overeenkomsten met derden waarbij toegang tot, het verwerken van, communicatie van of beheer "
                 u"van informatie of ICT-voorzieningen van de organisatie, of toevoeging van producten of diensten "
                 u"aan ICT-voorzieningen waarbij sprake is van toegang, behoren alle relevante beveiligingseisen te "
                 u"zijn opgenomen.",
            fragments=[
                Verifier(
                    identifier="06.02.03/01",
                    title=u"",
                    text=u"De maatregelen behorend bij 06.02.01 zijn voorafgaand aan het afsluiten van het contract "
                         u"gedefinieerd en geïmplementeerd."
                ),
                Verifier(
                    identifier="06.02.03/02",
                    title=u"",
                    text=u"Uitbesteding (ontwikkelen en aanpassen) van software is geregeld volgens formele "
                         u"contracten waarin o.a. intellectueel eigendom, kwaliteitsaspecten, beveiligingsaspecten, "
                         u"aansprakelijkheid, escrow en reviews geregeld worden."
                ),
                Verifier(
                    identifier="06.02.03/03",
                    title=u"",
                    text=u"In contracten met externe partijen is vastgelegd hoe men dient te gaan met wijzigingen en "
                         u"hoe ervoor gezorgd wordt dat de beveiliging niet wordt aangetast door de wijzigingen."
                ),
                Verifier(
                    identifier="06.02.03/04",
                    title=u"",
                    text=u"In contracten met externe partijen is vastgelegd hoe wordt omgegaan met geheimhouding."
                ),
                Verifier(
                    identifier="06.02.03/05",
                    title=u"",
                    text=u"Er is een plan voor beëindiging van de ingehuurde diensten waarin aandacht wordt besteed "
                         u"aan beschikbaarheid, vertrouwelijkheid en integriteit."
                ),
                Verifier(
                    identifier="06.02.03/06",
                    title=u"",
                    text=u"In contracten met externe partijen is vastgelegd hoe escalaties en aansprakelijkheid "
                         u"geregeld zijn."
                ),
                Verifier(
                    identifier="06.02.03/07",
                    title=u"",
                    text=u"Als er gebruikt gemaakt wordt van onderaannemers dan gelden daar dezelfde "
                         u"beveiligingseisen voor als voor de contractant. De hoofdaannemer is verantwoordelijk voor "
                         u"de borging bij de onderaannemer van de gemaakte afspraken."
                ),
                Verifier(
                    identifier="06.02.03/08",
                    title=u"",
                    text=u"De producten, diensten en daarbij geldende randvoorwaarden, rapporten en registraties die "
                         u"door een derde partij worden geleverd, worden beoordeeld op het nakomen van de afspraken "
                         u"in de overeenkomst. Verbeteracties worden geïnitieerd wanneer onder het afgesproken niveau "
                         u"wordt gepresteerd."
                ),
            ],
        ),
    ],
)

# ---


CH06 = Chapter(
    identifier="06",
    title=u"Organisatie van de Informatiebeveiliging",
    fragments=[
        S0601,
        S0602,
    ]
)
