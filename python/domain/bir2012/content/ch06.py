# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S0601 = Section(
    identifier="06.01",
    title="Interne organisatie",
    fragments=[
        Norm(
            identifier="06.01.01",
            title="Betrokkenheid van de directie bij beveiliging",
            text="De directie behoort actief beveiliging binnen de organisatie te ondersteunen door duidelijk "
                 "richting te geven, betrokkenheid te tonen en expliciet verantwoordelijkheden voor "
                 "informatiebeveiliging toe te kennen en te erkennen.",
            fragments=[
                Verifier(
                    identifier="06.01.01/01",
                    title="",
                    text="Het lijnmanagement waarborgt dat de informatiebeveiligingsdoelstellingen worden "
                         "vastgesteld, voldoen aan de kaders zoals gesteld in dit document en zijn geïntegreerd in "
                         "de relevante processen. Dit gebeurt door één keer per jaar opzet, bestaan en werking van "
                         "de IB-maatregelen te bespreken in het overleg van de departementsleiding en hiervan "
                         "verslag te doen."
                ),
            ],
        ),
        Norm(
            identifier="06.01.02",
            title="Coördineren van beveiliging",
            text="Activiteiten voor informatiebeveiliging behoren te worden gecoördineerd door vertegenwoordigers "
                 "uit verschillende delen van de organisatie met relevante rollen en functies.",
            fragments=[
                Verifier(
                    identifier="06.01.02/01",
                    title="",
                    text="De rollen van BVA, BVC en het lijnmanagement zijn beschreven in het "
                         "Beveiligingsvoorschrift Rijksdienst 2005."
                ),
            ],
        ),
        Norm(
            identifier="06.01.03",
            title="Verantwoordelijkheden",
            text="Alle verantwoordelijkheden voor informatiebeveiliging behoren duidelijk te zijn gedefinieerd.",
            fragments=[
                Verifier(
                    identifier="06.01.03/01",
                    title="",
                    text="Elke lijnmanager is verantwoordelijk voor de integrale beveiliging van zijn of haar "
                         "dienstonderdeel."
                ),
            ],
        ),
        Norm(
            identifier="06.01.04",
            title="Goedkeuringsproces voor ICT-voorzieningen",
            text="Er behoort een goedkeuringsproces voor nieuwe ICT-voorzieningen te worden vastgesteld en "
                 "geïmplementeerd.",
            fragments=[
                Verifier(
                    identifier="06.01.04/01",
                    title="",
                    text="Er is een goedkeuringsproces voor nieuwe IT-voorzieningen en wijzigingen in "
                         "IT-voorzieningen."
                ),
            ],
        ),
        Norm(
            identifier="06.01.05",
            title="Geheimhoudingsovereenkomst",
            text="Eisen voor vertrouwelijkheid of geheimhoudingsovereenkomst die een weerslag vormen van de behoefte "
                 "van de organisatie aan bescherming van informatie behoren te worden vastgesteld en regelmatig te "
                 "worden beoordeeld.",
            fragments=[
                Verifier(
                    identifier="06.01.05/01",
                    title="",
                    text="De algemene geheimhoudingsplicht voor ambtenaren is geregeld in de Ambtenarenwet art. 125a, "
                         "lid 3. Daarnaast dienen personen die te maken hebben met Bijzondere Informatie een "
                         "geheimhoudingsverklaring te ondertekenen (zie VIRBI); daaronder valt ook de departementaal "
                         "vertrouwelijke informatie. Hierbij wordt tevens vastgelegd dat na beëindiging van de "
                         "functie, de betreffende persoon gehouden blijft aan die geheimhouding."
                ),
            ],
        ),
        Norm(
            identifier="06.01.06",
            title="Contact met overheidsinstanties",
            text="Er behoren geschikte contacten met relevante overheidsinstanties te worden onderhouden.",
            fragments=[
                Verifier(
                    identifier="06.01.06/01",
                    title="",
                    text="Het lijnmanagement stelt vast in welke gevallen en door wie er contacten met autoriteiten "
                         "(brandweer, toezichthouders, enz.) wordt onderhouden."
                ),
            ],
        ),
        Norm(
            identifier="06.01.07",
            title="Contact met speciale belangengroepen",
            text="Er behoren geschikte contacten met speciale belangengroepen of andere specialistische platforms "
                 "voor beveiliging en professionele organisaties te worden onderhouden.",
            fragments=[
                Verifier(
                    identifier="06.01.07/01",
                    title="",
                    text="IB-specifieke informatie van relevante expertisegroepen, leveranciers van hardware, "
                         "software en diensten wordt gebruikt om de informatiebeveiliging te verbeteren."
                ),
            ],
        ),
        Norm(
            identifier="06.01.08",
            title="Beoordeling van het informatiebeveiligingsbeleid",
            text="De benadering van de organisatie voor het beheer van informatiebeveiliging en de implementatie "
                 "daarvan (d.w.z. beheersdoelstellingen, beheersmaatregelen, beleid, processen en procedures voor "
                 "informatiebeveiliging) behoren onafhankelijk en met geplande tussenpozen te worden beoordeeld, of "
                 "zodra zich significante wijzigingen voordoen in de implementatie van de beveiliging.",
            fragments=[
                Verifier(
                    identifier="06.01.08/01",
                    title="",
                    text="Het informatiebeveiligingsbeleid wordt minimaal één keer in de drie jaar geëvalueerd "
                         "(door een onafhankelijke deskundige) en desgewenst bijgesteld."
                ),
                Verifier(
                    identifier="06.01.08/02",
                    title="",
                    text="Periodieke beveiligingsaudits worden uitgevoerd in opdracht van het lijnmanagement."
                ),
                Verifier(
                    identifier="06.01.08/03",
                    title="",
                    text="Over het functioneren van de informatiebeveiliging wordt, conform de P&amp;C cyclus, "
                         "jaarlijks gerapporteerd aan het lijnmanagement."
                ),
            ],
        ),
    ],
)

S0602 = Section(
    identifier="06.02",
    title="Externe Partijen",
    fragments=[
        Norm(
            identifier="06.02.01",
            title="Identificatie van risico's die betrekking hebben op externe partijen",
            text="De risico's voor de informatie en ICT-voorzieningen van de organisatie vanuit bedrijfsprocessen "
                 "waarbij externe partijen betrokken zijn, behoren te worden geïdentificeerd en er behoren geschikte "
                 "beheersmaatregelen te worden geïmplementeerd voordat toegang wordt verleend.",
            fragments=[
                Verifier(
                    identifier="06.02.01/01",
                    title="",
                    text="Informatiebeveiliging is aantoonbaar (op basis van een risicoafweging) meegewogen bij het "
                         "besluit een externe partij wel of niet in te schakelen."
                ),
                Verifier(
                    identifier="06.02.01/02",
                    title="",
                    text="Voorafgaand aan het afsluiten van een contract voor uitbesteding of externe inhuur is "
                         "bepaald welke toegang (fysiek, netwerk of tot gegevens) de externe partij(en) moet(en) "
                         "hebben om de in het contract overeen te komen opdracht uit te voeren en welke "
                         "noodzakelijke beveiligingsmaatregelen hiervoor nodig zijn."
                ),
                Verifier(
                    identifier="06.02.01/03",
                    title="",
                    text="Voorafgaand aan het afsluiten van een contract voor uitbesteding of externe inhuur is "
                         "bepaald welke waarde en gevoeligheid de informatie (bijv. risicoklasse van WBP of "
                         "vertrouwelijkheidklasse volgens VIRBI) heeft waarmee de derde partij in aanraking kan "
                         "komen en of hierbij eventueel aanvullende beveiligingsmaatregelen nodig zijn."
                ),
                Verifier(
                    identifier="06.02.01/04",
                    title="",
                    text="Voorafgaand aan het afsluiten van een contract voor uitbesteding en externe inhuur is "
                         "bepaald hoe geauthenticeerde en geautoriseerde toegang vastgesteld wordt."
                ),
                Verifier(
                    identifier="06.02.01/05",
                    title="",
                    text="Indien externe partijen systemen beheren waarin persoonsgegevens verwerkt worden, wordt "
                         "een bewerkerovereenkomst (conform WBP artikel 14) afgesloten."
                ),
                Verifier(
                    identifier="06.02.01/06",
                    title="",
                    text="Er is in contracten met externe partijen vastgelegd welke beveiligingsmaatregelen vereist "
                         "zijn, dat deze door de externe partij zijn getroffen en worden nageleefd en dat "
                         "beveiligingsincidenten onmiddellijk worden gerapporteerd. Ook wordt beschreven hoe die "
                         "beveiligingsmaatregelen door de uitbestedende partij te controleren zijn (bijv. audits en "
                         "penetratietests) en hoe het toezicht is geregeld."
                ),
            ],
        ),
        Norm(
            identifier="06.02.02",
            title="Beveiliging behandelen in de omgang met klanten",
            text="Alle geïdentificeerde beveiligingseisen behoren te worden behandeld voordat klanten toegang wordt "
                 "verleend tot de informatie of bedrijfsmiddelen van de organisatie.",
            fragments=[
                Verifier(
                    identifier="06.02.02/01",
                    title="",
                    text="Alle noodzakelijke beveiligingseisen worden op basis van een risicoafweging vastgesteld en "
                         "geïmplementeerd voordat aan gebruikers toegang tot informatie op bedrijfsmiddelen wordt "
                         "verleend."
                ),
            ],
        ),
        Norm(
            identifier="06.02.03",
            title="Beveiliging behandelen in overeenkomsten met een derde partij",
            text="In overeenkomsten met derden waarbij toegang tot, het verwerken van, communicatie van of beheer "
                 "van informatie of ICT-voorzieningen van de organisatie, of toevoeging van producten of diensten "
                 "aan ICT-voorzieningen waarbij sprake is van toegang, behoren alle relevante beveiligingseisen te "
                 "zijn opgenomen.",
            fragments=[
                Verifier(
                    identifier="06.02.03/01",
                    title="",
                    text="De maatregelen behorend bij 06.02.01 zijn voorafgaand aan het afsluiten van het contract "
                         "gedefinieerd en geïmplementeerd."
                ),
                Verifier(
                    identifier="06.02.03/02",
                    title="",
                    text="Uitbesteding (ontwikkelen en aanpassen) van software is geregeld volgens formele "
                         "contracten waarin o.a. intellectueel eigendom, kwaliteitsaspecten, beveiligingsaspecten, "
                         "aansprakelijkheid, escrow en reviews geregeld worden."
                ),
                Verifier(
                    identifier="06.02.03/03",
                    title="",
                    text="In contracten met externe partijen is vastgelegd hoe men dient te gaan met wijzigingen en "
                         "hoe ervoor gezorgd wordt dat de beveiliging niet wordt aangetast door de wijzigingen."
                ),
                Verifier(
                    identifier="06.02.03/04",
                    title="",
                    text="In contracten met externe partijen is vastgelegd hoe wordt omgegaan met geheimhouding."
                ),
                Verifier(
                    identifier="06.02.03/05",
                    title="",
                    text="Er is een plan voor beëindiging van de ingehuurde diensten waarin aandacht wordt besteed "
                         "aan beschikbaarheid, vertrouwelijkheid en integriteit."
                ),
                Verifier(
                    identifier="06.02.03/06",
                    title="",
                    text="In contracten met externe partijen is vastgelegd hoe escalaties en aansprakelijkheid "
                         "geregeld zijn."
                ),
                Verifier(
                    identifier="06.02.03/07",
                    title="",
                    text="Als er gebruikt gemaakt wordt van onderaannemers dan gelden daar dezelfde "
                         "beveiligingseisen voor als voor de contractant. De hoofdaannemer is verantwoordelijk voor "
                         "de borging bij de onderaannemer van de gemaakte afspraken."
                ),
                Verifier(
                    identifier="06.02.03/08",
                    title="",
                    text="De producten, diensten en daarbij geldende randvoorwaarden, rapporten en registraties die "
                         "door een derde partij worden geleverd, worden beoordeeld op het nakomen van de afspraken "
                         "in de overeenkomst. Verbeteracties worden geïnitieerd wanneer onder het afgesproken niveau "
                         "wordt gepresteerd."
                ),
            ],
        ),
    ],
)

# ---


CH06 = Chapter(
    identifier="06",
    title="Organisatie van de Informatiebeveiliging",
    fragments=[
        S0601,
        S0602,
    ]
)
