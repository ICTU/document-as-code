# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S1101 = Section(
    identifier="11.01",
    title="Toegangsbeleid",
    fragments=[
        Norm(
            identifier="11.01.01",
            title="Toegangsbeleid",
            text="Er behoort toegangsbeleid te worden vastgesteld, gedocumenteerd en beoordeeld op basis van "
                 "bedrijfseisen en beveiligingseisen voor toegang.",
            fragments=[
                Verifier(
                    identifier="11.01.01/01",
                    title="",
                    text="- conform norm -",
                ),
            ],
        ),
    ],
)


S1102 = Section(
    identifier="11.02",
    title="Beheer van toegangsrechten van gebruikers",
    fragments=[
        Norm(
            identifier="11.02.01",
            title="Registratie van gebruikers",
            text="Er behoren formele procedures voor het registreren en afmelden van gebruikers te zijn vastgesteld, "
                 "voor het verlenen en intrekken van toegangsrechten tot alle informatiesystemen en -diensten.",
            fragments=[
                Verifier(
                    identifier="11.02.01/01",
                    title="",
                    text="Gebruikers worden vooraf geïdentificeerd en geautoriseerd. Van de registratie wordt een "
                         "administratie bijgehouden.",
                ),
                Verifier(
                    identifier="11.02.01/02",
                    title="",
                    text="Authenticatiegegevens worden bijgehouden in één bronbestand) zodat consistentie is "
                         "gegarandeerd.",
                ),
                Verifier(
                    identifier="11.02.01/03",
                    title="",
                    text="Op basis van een risicoafweging wordt bepaald waar en op welke wijze functiescheiding "
                         "wordt toegepast en welke toegangsrechten worden gegeven.",
                ),
            ],
        ),
        Norm(
            identifier="11.02.02",
            title="Beheer van (speciale) bevoegdheden",
            text="De toewijzing en het gebruik van speciale bevoegdheden behoren te worden beperkt en beheerst.",
            fragments=[
                Verifier(
                    identifier="11.02.02/01",
                    title="",
                    text="Gebruikers hebben toegang tot speciale bevoegdheden voor zover dat voor de uitoefening "
                         "van hun taak noodzakelijk is (need to know, need to use).",
                ),
                Verifier(
                    identifier="11.02.02/02",
                    title="",
                    text="Systeemprocessen draaien onder een eigen gebruikersnaam (een functioneel account), "
                         "voor zover deze processen handelingen verrichten voor andere systemen of gebruikers.",
                ),
                Verifier(
                    identifier="11.02.02/03",
                    title="",
                    text="Gebruikers krijgen slechts toegang tot een noodzakelijk geachte set van applicaties en "
                         "commando's.",
                ),
            ],
        ),
        Norm(
            identifier="11.02.03",
            title="Beheer van gebruikerswachtwoorden",
            text="De toewijzing van wachtwoorden behoort met een formeel beheerproces te worden beheerst.",
            fragments=[
                Verifier(
                    identifier="11.02.03/01",
                    title="",
                    text="Wachtwoorden worden nooit in originele vorm (plaintext) opgeslagen of verstuurd, maar "
                         "in plaats daarvan wordt bijvoorbeeld de hashwaarde van het wachtwoord opgeslagen.",
                ),
                Verifier(
                    identifier="11.02.03/02",
                    title="",
                    text="""Ten aanzien van wachtwoorden geldt:
<ul>
<li>Wachtwoorden worden op een veilige manier uitgegeven (controle identiteit van de gebruiker).</li>
<li>Tijdelijke wachtwoorden of wachtwoorden die standaard in software worden meegegeven worden bij 
    eerste gebruik vervangen door een persoonlijk wachtwoord.</li>
<li>Gebruikers bevestigen de ontvangst van een wachtwoord.</li>
</ul>""",
                ),
            ],
        ),
        Norm(
            identifier="11.02.04",
            title="Beoordeling van toegangsrechten van gebruikers",
            text="De directie behoort de toegangsrechten van gebruikers regelmatig te beoordelen in een "
                 "formeel proces.",
            fragments=[
                Verifier(
                    identifier="11.02.04/01",
                    title="",
                    text="Toegangsrechten van gebruikers worden periodiek, minimaal jaarlijks, geëvalueerd. Het "
                         "interval is beschreven in het toegangsbeleid en is bepaald op basis van het risiconiveau.",
                ),
            ],
        ),
    ],
)


S1103 = Section(
    identifier="11.03",
    title="Verantwoordelijkheden van gebruikers",
    fragments=[
        Norm(
            identifier="11.03.01",
            title="Gebruik van wachtwoorden",
            text="Gebruikers behoren goede beveiligingsgewoontes in acht te nemen bij het kiezen en gebruiken van "
                 "wachtwoorden.",
            fragments=[
                Verifier(
                    identifier="11.03.01/01",
                    title="",
                    text="""Aan de gebruikers is een set gedragsregels aangereikt met daarin minimaal het volgende:
<ul>
<li>Wachtwoorden worden niet opgeschreven.</li>
<li>Gebruikers delen hun wachtwoord nooit met anderen.</li>
<li>Een wachtwoord wordt onmiddellijk gewijzigd indien het vermoeden bestaat dat het bekend is geworden aan
    een derde.</li>
<li>Wachtwoorden worden niet gebruikt in automatische inlogprocedures
    (bijv. opgeslagen onder een functietoets of in een macro).</li>
</ul>""",
                ),
            ],
        ),
        Norm(
            identifier="11.03.02",
            title="Onbeheerde gebruikersapparatuur",
            text="Gebruikers behoren te bewerkstelligen dat onbeheerde apparatuur passend is beschermd.",
            fragments=[
                Verifier(
                    identifier="11.03.02/01",
                    title="",
                    text="De gebruiker vergrendelt de werkplek tijdens afwezigheid.",
                ),
            ],
        ),
        Norm(
            identifier="11.03.03",
            title="Clear desk en clear screen",
            text="Er behoort een 'clear desk'-beleid voor papier en verwijderbare opslagmedia en een "
                 "'clear screen'-beleid voor ICT-voorzieningen te worden ingesteld.",
            fragments=[
                Verifier(
                    identifier="11.03.03/01",
                    title="",
                    text="In het clear desk beleid staat minimaal dat de gebruiker geen vertrouwelijke informatie op "
                         "het bureau mag laten liggen. Deze informatie moet altijd worden opgeborgen in een "
                         "afsluitbare opbergmogelijkheid (kast, locker, bureau of kamer).",
                ),
                Verifier(
                    identifier="11.03.03/02",
                    title="",
                    text="Bij afdrukken van gevoelige informatie wordt, wanneer mogelijk, gebruik gemaakt van de "
                         "functie 'beveiligd afdrukken' (pincode verificatie).",
                ),
                Verifier(
                    identifier="11.03.03/03",
                    title="",
                    text="Schermbeveiligingsprogrammatuur (een screensaver) maakt na een periode van inactiviteit "
                         "van maximaal 15 minuten alle informatie op het beeldscherm onleesbaar en ontoegankelijk.",
                ),
                Verifier(
                    identifier="11.03.03/04",
                    title="",
                    text="Toegangsbeveiliging lock wordt automatisch geactiveerd bij het verwijderen van een token "
                         "(indien aanwezig).",
                ),
            ],
        ),
    ],
)


S1104 = Section(
    identifier="11.04",
    title="Toegangsbeheersing voor netwerken",
    fragments=[
        Norm(
            identifier="11.04.01",
            title="Beleid ten aanzien van het gebruik van netwerkdiensten",
            text="Gebruikers behoort alleen toegang te worden verleend tot diensten waarvoor ze specifiek "
                 "bevoegd zijn.",
            fragments=[
                Verifier(
                    identifier="11.04.01/01",
                    title="",
                    text="""Er is een gedocumenteerd beleid met betrekking tot het gebruik van netwerken en 
                    netwerkdiensten. Gebruikers krijgen slechts
toegang tot de netwerkdiensten die voor het werk noodzakelijk zijn.""",
                ),
            ],
        ),
        Norm(
            identifier="11.04.02",
            title="Authenticatie van gebruikers bij externe verbindingen",
            text="Er behoren geschikte authenticatiemethoden te worden gebruikt om toegang van gebruikers op "
                 "afstand te beheersen.",
            fragments=[
                Verifier(
                    identifier="11.04.02/01",
                    title="",
                    text="- conform norm -",
                ),
            ],
        ),
        Norm(
            identifier="11.04.03",
            title="Identificatie van (netwerk)apparatuur",
            text="Automatische identificatie van apparatuur behoort te worden overwogen als methode om "
                 "verbindingen vanaf specifieke locaties en apparatuur te authenticeren.",
            fragments=[
                Verifier(
                    identifier="11.04.03/01",
                    title="",
                    text="Alleen geïdentificeerde en geauthenticeerde apparatuur kan worden aangesloten op "
                         "een vertrouwde zone. Eigen, ongeauthenticeerde, apparatuur (Bring Your Own Device) "
                         "wordt alleen aangesloten op een onvertrouwde zone.",
                ),
            ],
        ),
        Norm(
            identifier="11.04.04",
            title="Bescherming op afstand van poorten voor diagnose en configuraties",
            text="De fysieke en logische toegang tot poorten voor diagnose en configuratie behoort te worden "
                 "beheerst.",
            fragments=[
                Verifier(
                    identifier="11.04.04/01",
                    title="",
                    text="Poorten, diensten en soortgelijke voorzieningen op een netwerk of computer die niet "
                         "vereist zijn voor de dienst dienen te worden afgesloten.",
                ),
            ],
        ),
        Norm(
            identifier="11.04.05",
            title="Scheiding van netwerken",
            text="Groepen informatiediensten, gebruikers en informatiesystemen behoren op netwerken te worden "
                 "gescheiden.",
            fragments=[
                Verifier(
                    identifier="11.04.05/01",
                    title="",
                    text="Werkstations worden zo ingericht dat routeren van verkeer tussen verschillende zones of "
                         "netwerken niet mogelijk is.",
                ),
                Verifier(
                    identifier="11.04.05/02",
                    title="",
                    text="De indeling van zones binnen de technische infrastructuur vindt plaats volgens een "
                         "operationeel beleidsdocument waarin is vastgelegd welke uitgangspunten voor zonering "
                         "worden gehanteerd. Van systemen wordt bijgehouden in welke zone ze staan. Er wordt "
                         "periodiek, minimaal één keer per jaar, geëvalueerd of het systeem nog steeds in de "
                         "optimale zone zit of verplaatst moet worden.",
                ),
                Verifier(
                    identifier="11.04.05/03",
                    title="",
                    text="Elke zone heeft een gedefinieerd beveiligingsniveau Zodat de filtering tussen zones is "
                         "afgestemd op de doelstelling van de zones en het te overbruggen verschil in "
                         "beveiligingsniveau. Hierbij vindt controle plaats op protocol, inhoud en richting "
                         "van de communicatie.",
                ),
                Verifier(
                    identifier="11.04.05/04",
                    title="",
                    text="Beheer en audit van zones vindt plaats vanuit een minimaal logisch gescheiden, "
                         "separate zone.",
                ),
                Verifier(
                    identifier="11.04.05/05",
                    title="",
                    text="Zonering wordt ingericht met voorzieningen waarvan de functionaliteit is beperkt tot het "
                         "strikt noodzakelijke (hardening van voorzieningen).",
                ),
            ],
        ),
        Norm(
            identifier="11.04.06",
            title="Beheersmaatregelen voor netwerkverbindingen",
            text="Voor gemeenschappelijke netwerken, vooral waar deze de grenzen van de organisatie overschrijden, "
                 "behoren de toegangsmogelijkheden voor gebruikers te worden beperkt, overeenkomstig het "
                 "toegangsbeleid en de eisen van bedrijfstoepassingen.",
            fragments=[
                Verifier(
                    identifier="11.04.06/01",
                    title="",
                    text="- conform norm -",
                ),
            ],
        ),
        Norm(
            identifier="11.04.07",
            title="Beheersmaatregelen voor netwerkroutering",
            text="Netwerken behoren te zijn voorzien van beheersmaatregelen voor netwerkroutering, om te "
                 "bewerkstelligen dat computerverbindingen en informatiestromen niet in strijd zijn met het "
                 "toegangsbeleid voor de bedrijfstoepassingen.",
            fragments=[
                Verifier(
                    identifier="11.04.07/01",
                    title="",
                    text="Netwerken zijn voorzien van beheersmaatregelen voor routering gebaseerd op mechanismen "
                         "ter verificatie van bron en bestemmingsadressen.",
                ),
            ],
        ),
    ],
)


S1105 = Section(
    identifier="11.05",
    title="Toegangsbeveiliging voor besturingssystemen",
    fragments=[
        Norm(
            identifier="11.05.01",
            title="Beveiligde inlogprocedures",
            text="Toegang tot besturingssystemen behoort te worden beheerst met een beveiligde inlogprocedure.",
            fragments=[
                Verifier(
                    identifier="11.05.01/01",
                    title="",
                    text="Toegang tot kritische toepassingen of toepassingen met een hoog belang wordt verleend op "
                         "basis van twee-factor authenticatie.",
                ),
                Verifier(
                    identifier="11.05.01/02",
                    title="",
                    text="Het wachtwoord wordt niet getoond op het scherm tijdens het ingeven. Er wordt geen "
                         "informatie getoond die herleidbaar is tot de authenticatiegegevens.",
                ),
                Verifier(
                    identifier="11.05.01/03",
                    title="",
                    text="Voorafgaand aan het aanmelden wordt aan de gebruiker een melding getoond dat alleen "
                         "geautoriseerd gebruik is toegestaan voor expliciet door de organisatie vastgestelde "
                         "doeleinden.",
                ),
                Verifier(
                    identifier="11.05.01/04",
                    title="",
                    text="Bij een succesvol loginproces wordt de datum en tijd van de voorgaande login of "
                         "loginpoging getoond. Deze informatie kan de gebruiker enige informatie verschaffen over "
                         "de authenticiteit en/of misbruik van het systeem.",
                ),
                Verifier(
                    identifier="11.05.01/05",
                    title="",
                    text="Nadat voor een gebruikersnaam 5 keer een foutief wachtwoord gegeven is, wordt het account "
                         "minimaal 10 minuten geblokkeerd. Indien er geen lockout periode ingesteld kan worden, dan "
                         "wordt het account geblokkeerd totdat de gebruiker verzoekt deze lockout op te heffen of het "
                         "wachtwoord te resetten.",
                ),
            ],
        ),
        Norm(
            identifier="11.05.02",
            title="Gebruikersindentificatie en -authenticatie",
            text="Elke gebruiker behoort over een unieke identificatiecode te beschikken (gebruikers-ID) voor "
                 "uitsluitend persoonlijk gebruik, en er behoort een geschikte authenticatietechniek te worden "
                 "gekozen om de geclaimde identiteit van de gebruiker te bewijzen.",
            fragments=[
                Verifier(
                    identifier="11.05.02/01",
                    title="",
                    text="Bij uitgifte van authenticatiemiddelen wordt minimaal de identiteit vastgesteld evenals "
                         "het feit dat de gebruiker recht heeft op het authenticatiemiddel.",
                ),
                Verifier(
                    identifier="11.05.02/02",
                    title="",
                    text="Bij het intern gebruik van IT voorzieningen worden gebruikers minimaal geauthenticeerd op "
                         "basis van wachtwoorden.",
                ),
                Verifier(
                    identifier="11.05.02/03",
                    title="",
                    text="Applicaties mogen niet onnodig en niet langer dan noodzakelijk onder een systeemaccount "
                         "(een privileged user zoals adminstrator of root) draaien. Direct na het uitvoeren van "
                         "handelingen waar hogere rechten voor nodig zijn, wordt weer teruggeschakeld naar het "
                         "niveau van een gewone gebruiker (een unprivileged user).",
                ),
            ],
        ),
        Norm(
            identifier="11.05.03",
            title="Systemen voor wachtwoordenbeheer",
            text="Systemen voor wachtwoordbeheer behoren interactief te zijn en moeten bewerkstelligen dat "
                 "wachtwoorden van geschikte kwaliteit worden gekozen.",
            fragments=[
                Verifier(
                    identifier="11.05.03/01",
                    title="",
                    text="Er wordt automatisch gecontroleerd op goed gebruik van wachtwoorden (o.a. voldoende sterke "
                         "wachtwoorden, regelmatige wijziging, directe wijziging van initieel wachtwoord).",
                ),
                Verifier(
                    identifier="11.05.03/02",
                    title="",
                    text="Wachtwoorden hebben een geldigheidsduur van maximaal 3 maanden. Daarbinnen dient het "
                         "wachtwoord te worden gewijzigd. Wanneer het wachtwoord verlopen is, wordt het account "
                         "geblokkeerd.",
                ),
                Verifier(
                    identifier="11.05.03/03",
                    title="",
                    text="Wachtwoorden die gereset zijn en initiële wachtwoorden hebben een zeer beperkte "
                         "geldigheidsduur en moeten bij het eerste gebruik worden gewijzigd.",
                ),
                Verifier(
                    identifier="11.05.03/04",
                    title="",
                    text="""De gebruikers hebben de mogelijkheid hun eigen wachtwoord te kiezen en te wijzigen. 
Hierbij geldt het volgende:
<ul>
<li>Voordat een gebruiker zijn wachtwoord kan wijzigen, wordt de gebruiker opnieuw geauthenticeerd.</li>
<li>Ter voorkoming van typefouten in het nieuw gekozen wachtwoord is er een bevestigingsprocedure.</li>
</ul>""",
                ),
            ],
        ),
        Norm(
            identifier="11.05.04",
            title="Gebruik van systeemhulpmiddelen",
            text="Het gebruik van hulpprogrammatuur waarmee systeem- en toepassingsbeheersmaatregelen zouden kunnen "
                 "worden gepasseerd behoort te worden beperkt en behoort strikt te worden beheerst.",
            fragments=[
                Verifier(
                    identifier="11.05.04/01",
                    title="",
                    text="- conform norm -",
                ),
            ],
        ),
        Norm(
            identifier="11.05.05",
            title="Time-out van sessies",
            text="Inactieve sessies behoren na een vastgestelde periode van inactiviteit te worden uitgeschakeld.",
            fragments=[
                Verifier(
                    identifier="11.05.05/01",
                    title="",
                    text="De periode van inactiviteit van een werkstation is vastgesteld op maximaal 15 minuten. "
                         "Daarna wordt de PC vergrendeld. Bij remote desktop sessies geldt dat na maximaal 15 minuten "
                         "inactiviteit de sessie verbroken wordt.",
                ),
            ],
        ),
        Norm(
            identifier="11.05.06",
            title="Beperking van verbindingstijd",
            text="De verbindingstijd behoort te worden beperkt als aanvullende beveiliging voor toepassingen met een "
                 "verhoogd risico.",
            fragments=[
                Verifier(
                    identifier="11.05.06/01",
                    title="",
                    text="De toegang voor onderhoud op afstand door een leverancier wordt alleen opengesteld op basis "
                         "een wijzigingsverzoek of storingsmelding.",
                ),
            ],
        ),
    ],
)


S1106 = Section(
    identifier="11.06",
    title="Toegangsbeheersing voor toepassingen en informatie",
    fragments=[
        Norm(
            identifier="11.06.01",
            title="Beperken van toegang tot informatie",
            text="Toegang tot informatie en functies van toepassingssystemen door gebruikers en ondersteunend "
                 "personeel behoort te worden beperkt overeenkomstig het vastgestelde toegangsbeleid.",
            fragments=[
                Verifier(
                    identifier="11.06.01/01",
                    title="",
                    text="In de soort toegangsregels wordt tenminste onderscheid gemaakt tussen lees- en "
                         "schrijfbevoegdheden.",
                ),
                Verifier(
                    identifier="11.06.01/02",
                    title="",
                    text="Managementsoftware heeft de mogelijkheid gebruikerssessies af te sluiten.",
                ),
                Verifier(
                    identifier="11.06.01/03",
                    title="",
                    text="Bij extern gebruik vanuit een onvertrouwde omgeving vindt sterke authenticatie (two-factor)"
                         "van gebruikers plaats.",
                ),
                Verifier(
                    identifier="11.06.01/04",
                    title="",
                    text="Een beheerder gebruikt two-factor authenticatie voor het beheer van kritische apparaten. "
                         "B.v. een sleutel tot beveiligde ruimte en een password of een token en een password.",
                ),
            ],
        ),
        Norm(
            identifier="11.06.02",
            title="Isoleren van gevoelige systemen",
            text="Gevoelige systemen behoren een eigen, vast toegewezen (geïsoleerde) computeromgeving te hebben.",
            fragments=[
                Verifier(
                    identifier="11.06.02/01",
                    title="",
                    text="Gevoelige systemen (met hoge beschikbaarheid of grote vertrouwelijkheid) behoren een eigen "
                         "vast toegewezen (geïsoleerde) computeromgeving te hebben. Isoleren kan worden bereikt door "
                         "fysieke of logische methoden.",
                ),
            ],
        ),
    ],
)


S1107 = Section(
    identifier="11.07",
    title="Draagbare computers en telewerken",
    fragments=[
        Norm(
            identifier="11.07.01",
            title="Draagbare computers en communicatievoorzieningen",
            text="Er behoort formeel beleid te zijn vastgesteld en er behoren geschikte beveiligingsmaatregelen te "
                 "zijn getroffen ter bescherming tegen risico's van het gebruik van draagbare computers en "
                 "communicatiefaciliteiten.",
            fragments=[
                Verifier(
                    identifier="11.07.01/01",
                    title="",
                    text="Het mobiele apparaat is waar mogelijk zo ingericht dat geen bedrijfsinformatie wordt "
                         "opgeslagen ('zero footprint'). Voor het geval dat zero footprint (nog) niet realiseerbaar "
                         "is, of functioneel onwenselijk is, geldt: een mobiel apparaat (zoals een handheld computer, "
                         "tablet, smartphone, PDA) biedt de mogelijkheid om de toegang te beschermen d.m.v. een "
                         "wachtwoord en versleuteling van die gegevens. Voor printen in onvertrouwde omgevingen vindt "
                         "een risicoafweging plaats.",
                ),
                Verifier(
                    identifier="11.07.01/02",
                    title="",
                    text="Er zijn, waar mogelijk, voorzieningen om de actualiteit van anti-malware programmatuur op "
                         "mobiele apparaten te garanderen.",
                ),
                Verifier(
                    identifier="11.07.01/03",
                    title="",
                    text="Bij melding van verlies of diefstal wordt de communicatiemogelijkheid met de centrale "
                         "applicaties afgesloten.",
                ),
            ],
        ),
        Norm(
            identifier="11.07.02",
            title="Telewerken",
            text="Er behoren beleid, operationele plannen en procedures voor telewerken te worden ontwikkeld en "
                 "geïmplementeerd.",
            fragments=[
                Verifier(
                    identifier="11.07.02/01",
                    title="",
                    text="Er wordt een beleid met gedragsregels en een geschikte implementatie van de techniek "
                         "opgesteld t.a.v. telewerken.",
                ),
                Verifier(
                    identifier="11.07.02/02",
                    title="",
                    text="De telewerkvoorzieningen zijn waar mogelijk zo ingericht dat op de werkplek (thuis of op "
                         "een andere locatie) geen bedrijfsinformatie wordt opgeslagen ('zero footprint') en "
                         "mogelijke malware vanaf de werkplek niet in het vertrouwde deel terecht kan komen. Voor "
                         "printen in onvertrouwde omgevingen vindt een risicoafweging plaats.",
                ),
            ],
        ),
    ],
)


CH11 = Chapter(
    identifier="11",
    title="Toegangsbeveiliging",
    fragments=[
        S1101,
        S1102,
        S1103,
        S1104,
        S1105,
        S1106,
        S1107,
    ]
)
