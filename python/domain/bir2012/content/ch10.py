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


S1001 = Section(
    identifier="10.01",
    title=u"Bedieningsprocedures en verantwoordelijkheden",
    fragments=[
        Norm(
            identifier="10.01.01",
            title=u"Gedocumenteerde bedieningsprocedures",
            text=u"Bedieningsprocedures behoren te worden gedocumenteerd, te worden bijgehouden en beschikbaar te "
                 u"worden gesteld aan alle gebruikers die deze nodig hebben.",
            fragments=[
                Verifier(
                    identifier="10.01.01/01",
                    title=u"",
                    text=u"Bedieningsprocedures bevatten informatie over opstarten, afsluiten, back-uppen en "
                         u"herstelacties, afhandelen van fouten, beheer van logs, contactpersonen, noodprocedures en "
                         u"speciale maatregelen voor beveiliging.",
                ),
                Verifier(
                    identifier="10.01.01/02",
                    title=u"",
                    text=u"Er zijn procedures voor de behandeling van digitale media die ingaan op ontvangst, opslag, "
                         u"rubricering, toegangsbeperkingen, verzending, hergebruik en vernietiging.",
                ),
            ],
        ),
        Norm(
            identifier="10.01.02",
            title=u"Wijzigingsbeheer",
            text=u"Wijzigingen in IT voorzieningen en informatiesystemen behoren te worden beheerst.",
            fragments=[
                Verifier(
                    identifier="10.01.02/01",
                    title=u"",
                    text=u"""In de procedure voor wijzigingenbeheer is minimaal aandacht besteed aan:
<ul>
<li>het administreren van significante wijzigingen</li>
<li>impactanalyse van mogelijke gevolgen van de wijzigingen</li>
<li>goedkeuringsprocedure voor wijzigingen</li>
</ul>""",
                ),
                Verifier(
                    identifier="10.01.02/02",
                    title=u"",
                    text=u"Instellingen van informatiebeveiligingsfuncties (b.v. security software) op het koppelvlak "
                         u"tussen vertrouwde en onvertrouwde netwerken, worden automatisch op wijzigingen "
                         u"gecontroleerd.",
                ),
            ],
        ),
        Norm(
            identifier="10.01.03",
            title=u"Functiescheiding",
            text=u"Taken en verantwoordelijkheidsgebieden behoren te worden gescheiden om gelegenheid voor onbevoegde "
                 u"of onbedoelde wijziging of misbruik van de bedrijfsmiddelen van de organisatie te verminderen.",
            fragments=[
                Verifier(
                    identifier="10.01.03/01",
                    title=u"",
                    text=u"Niemand in een organisatie of proces mag op uitvoerend niveau rechten hebben om een gehele "
                         u"cyclus van handelingen in een kritisch informatiesysteem te beheersen. Dit in verband met "
                         u"het risico dat hij of zij zichzelf of anderen onrechtmatig bevoordeelt of de organisatie "
                         u"schade toe brengt. Dit geldt voor zowel informatieverwerking als beheeracties.",
                ),
                Verifier(
                    identifier="10.01.03/02",
                    title=u"",
                    text=u"Er is een scheiding tussen beheertaken en overige gebruikstaken. Beheerswerkzaamheden "
                         u"worden alleen uitgevoerd wanneer ingelogd als beheerder, normale gebruikstaken alleen "
                         u"wanneer ingelogd als gebruiker.",
                ),
                Verifier(
                    identifier="10.01.03/03",
                    title=u"",
                    text=u"Vóór de verwerking van gegevens die de integriteit van kritieke informatie of kritieke "
                         u"informatie systemen kunnen aantasten worden deze gegevens door een tweede persoon "
                         u"geïnspecteerd en geaccepteerd. Van de acceptatie wordt een log bijgehouden.",
                ),
                Verifier(
                    identifier="10.01.03/04",
                    title=u"",
                    text=u"Verantwoordelijkheden voor beheer en wijziging van gegevens en bijbehorende "
                         u"informatiesysteemfuncties moeten eenduidig toegewezen zijn aan één specifieke "
                         u"(beheerders)rol.",
                ),
            ],
        ),
        Norm(
            identifier="10.01.04",
            title=u"Scheiding van faciliteiten voor ontwikkeling, testen en productie",
            text=u"Faciliteiten voor ontwikkeling, testen en productie behoren te zijn gescheiden om het risico van "
                 u"onbevoegde toegang tot of wijzigingen in het productiesysteem te verminderen.",
            fragments=[
                Verifier(
                    identifier="10.01.04/01",
                    title=u"",
                    text=u"Er zijn minimaal logisch gescheiden systemen voor Ontwikkeling, Test en/of Acceptatie en "
                         u"Productie (OTAP). De systemen en applicaties in deze zones beïnvloeden systemen en "
                         u"applicaties in andere zones niet.",
                ),
                Verifier(
                    identifier="10.01.04/02",
                    title=u"",
                    text=u"Gebruikers hebben gescheiden gebruiksprofielen voor Ontwikkeling, Test en/of Acceptatie en "
                         u"Productiesystemen om het risico van fouten te verminderen. Het moet duidelijk zichtbaar "
                         u"zijn in welk systeem gewerkt wordt.",
                ),
                Verifier(
                    identifier="10.01.04/03",
                    title=u"",
                    text=u"Indien er een experimenteer of laboratorium omgeving is, is deze fysiek gescheiden van de "
                         u"productieomgeving.",
                ),
            ],
        ),
    ],
)


S1002 = Section(
    identifier="10.02",
    title=u"Exploitatie door een derde partij",
    fragments=[
        Norm(
            identifier="10.02.01",
            title=u"Dienstverlening",
            text=u"Er behoort te worden bewerkstelligd dat de beveiligingsmaatregelen, definities van dienstverlening "
                 u"en niveaus van dienstverlening zoals vastgelegd in de overeenkomst voor dienstverlening door een "
                 u"derde partij worden geïmplementeerd en uitgevoerd en worden bijgehouden door die derde partij.",
            fragments=[
                Verifier(
                    identifier="10.02.01/01",
                    title=u"",
                    text=u"De uitbestedende partij blijft verantwoordelijk voor de betrouwbaarheid van uitbestede "
                         u"diensten.",
                ),
                Verifier(
                    identifier="10.02.01/02",
                    title=u"",
                    text=u"Uitbesteding is goedgekeurd door de voor het informatiesysteem verantwoordelijke "
                         u"lijnmanager.",
                ),
            ],
        ),
        Norm(
            identifier="10.02.02",
            title=u"Controle en beoordeling van dienstverlening door een derde partij",
            text=u"De diensten, rapporten en registraties die door de derde partij worden geleverd, behoren regelmatig "
                 u"te worden gecontroleerd en beoordeeld en er behoren regelmatig audits te worden uitgevoerd.",
            fragments=[
                Verifier(
                    identifier="10.02.02/01",
                    title=u"",
                    text=u"Er worden afspraken gemaakt over de inhoud van rapportages, zoals over het melden van "
                         u"incidenten en autorisatiebeheer.",
                ),
                Verifier(
                    identifier="10.02.02/02",
                    title=u"",
                    text=u"De in dienstverleningscontracten vastgelegde betrouwbaarheidseisen worden gemonitord. Dit "
                         u"kan bijvoorbeeld met audits of rapportages en gebeurt minimaal eens per drie maanden.",
                ),
                Verifier(
                    identifier="10.02.02/03",
                    title=u"",
                    text=u"Er zijn voor beide partijen eenduidige aanspreekpunten.",
                ),
            ],
        ),
        Norm(
            identifier="10.02.03",
            title=u"Beheer van wijzigingen in dienstverlening door een derde partij",
            text=u"Wijzigingen in de dienstverlening door derden, waaronder het bijhouden en verbeteren van bestaande "
                 u"beleidslijnen, procedures en maatregelen voor informatiebeveiliging, behoren te worden beheerd, "
                 u"waarbij rekening wordt gehouden met de onmisbaarheid van de betrokken bedrijfssystemen en "
                 u"-processen en met heroverweging van risico's.",
            fragments=[
                Verifier(
                    identifier="10.02.03/01",
                    title=u"",
                    text=u"""In de procedure voor wijzigingenbeheer is minimaal aandacht besteed aan:
<ul>
<li>het administreren van significante wijzigingen</li>
<li>impactanalyse van mogelijke gevolgen van de wijzigingen</li>
<li>goedkeuringsprocedure voor wijzigingen</li>
</ul>""",
                ),
                Verifier(
                    identifier="10.02.03/02",
                    title=u"",
                    text=u"Instellingen van informatiebeveiligingsfuncties (b.v. security software) op het koppelvlak "
                         u"tussen vertrouwde en onvertrouwde netwerken, worden automatisch op wijzigingen "
                         u"gecontroleerd.",
                ),
            ],
        ),
    ],
)


S1003 = Section(
    identifier="10.03",
    title=u"Systeemplanning en -acceptatie",
    fragments=[
        Norm(
            identifier="10.03.01",
            title=u"Capaciteitsbeheer",
            text=u"Het gebruik van middelen behoort te worden gecontroleerd en afgestemd en er behoren verwachtingen "
                 u"te worden opgesteld voor toekomstige capaciteitseisen, om de vereiste systeemprestaties te "
                 u"bewerkstelligen.",
            fragments=[
                Verifier(
                    identifier="10.03.01/01",
                    title=u"",
                    text=u"De ICT-voorzieningen voldoen aan het voor de diensten overeengekomen niveau van "
                         u"beschikbaarheid. Er worden voorzieningen geïmplementeerd om de beschikbaarheid van "
                         u"componenten te bewaken (bijvoorbeeld de controle op aanwezigheid van een component en "
                         u"metingen die het gebruik van een component vaststellen). Op basis van voorspellingen van "
                         u"het gebruik wordt actie genomen om tijdig de benodigde uitbreiding van capaciteit te "
                         u"bewerkstelligen. Op basis van een risicoanalyse wordt bepaald wat de beschikbaarheid is van "
                         u"een ICT-voorziening is en wat de impact bij uitval is. Afhankelijk daarvan worden "
                         u"maatregelen bepaald zoals automatisch werkende mechanismen om uitval van (fysieke) "
                         u"ICT-voorzieningen, waaronder verbindingen op te vangen.",
                ),
                Verifier(
                    identifier="10.03.01/02",
                    title=u"",
                    text=u"Er worden beperkingen opgelegd aan gebruikers en systemen ten aanzien van het gebruik van "
                         u"gemeenschappelijke middelen, zodat een enkele gebruiker (of systeem) niet meer van deze "
                         u"middelen kan opeisen dan nodig is voor de uitvoering van zijn of haar taak en daarmee de "
                         u"beschikbaarheid van systemen voor andere gebruikers (of systemen) in gevaar kan brengen.",
                ),
                Verifier(
                    identifier="10.03.01/03",
                    title=u"",
                    text=u"In koppelpunten met externe of onvertrouwde zones worden maatregelen getroffen om "
                         u"DDOS (Denial of Service attacks) aanvallen te signaleren en hierop te reageren. Het gaat "
                         u"hier om aanvallen die erop gericht zijn de verwerkingscapaciteit zodanig te laten vollopen, "
                         u"dat onbereikbaarheid of uitval van computers het gevolg is.",
                ),
            ],
        ),
        Norm(
            identifier="10.03.02",
            title=u"Systeem acceptatie",
            text=u"Er behoren aanvaardingscriteria te worden vastgesteld voor nieuwe informatiesystemen, upgrades en "
                 u"nieuwe versies en er behoort een geschikte test van het systeem of de systemen te worden uitgevoerd "
                 u"tijdens ontwikkeling en voorafgaand aan de acceptatie.",
            fragments=[
                Verifier(
                    identifier="10.03.02/01",
                    title=u"",
                    text=u"Van acceptatietesten wordt een log bijgehouden.",
                ),
                Verifier(
                    identifier="10.03.02/02",
                    title=u"",
                    text=u"Er zijn acceptatiecriteria vastgesteld voor het testen van de beveiliging. "
                         u"Dit betreft minimaal OWASP of gelijkwaardig.",
                ),
            ],
        ),
    ],
)


S1004 = Section(
    identifier="10.04",
    title=u"Bescherming tegen virussen en \"mobile code\"",
    fragments=[
        Norm(
            identifier="10.04.01",
            title=u"Maatregelen tegen virussen",
            text=u"Er behoren maatregelen te worden getroffen voor detectie, preventie en herstellen om te beschermen "
                 u"tegen virussen en er behoren geschikte procedures te worden ingevoerd om het bewustzijn van de "
                 u"gebruikers te vergroten.",
            fragments=[
                Verifier(
                    identifier="10.04.01/01",
                    title=u"",
                    text=u"Bij het openen van bestanden worden deze geautomatiseerd gecontroleerd op virussen, trojans "
                         u"en andere malware. De update voor de detectiedefinities vindt frequent, minimaal één keer "
                         u"per dag, automatisch plaats.",
                ),
                Verifier(
                    identifier="10.04.01/02",
                    title=u"",
                    text=u"Inkomende en uitgaande e-mails worden gecontroleerd op virussen, trojans en andere malware. "
                         u"De update voor de detectiedefinities vindt frequent, minimaal één keer per dag, "
                         u"(automatisch) plaats.",
                ),
                Verifier(
                    identifier="10.04.01/03",
                    title=u"",
                    text=u"In verschillende schakels van een keten binnen de infrastructuur van een organisatie wordt "
                         u"bij voorkeur antivirus programmatuur van verschillende leveranciers toegepast.",
                ),
                Verifier(
                    identifier="10.04.01/04",
                    title=u"",
                    text=u"Er zijn maatregelen om verspreiding van virussen tegen te gaan en daarmee schade te "
                         u"beperken (bijv. quarantaine en compartimentering).",
                ),
                Verifier(
                    identifier="10.04.01/05",
                    title=u"",
                    text=u"Er zijn continuïteitsplannen voor herstel na aanvallen met virussen waarin minimaal "
                         u"maatregelen voor back-ups en herstel van gegevens en programmatuur zijn beschreven.",
                ),
            ],
        ),
        Norm(
            identifier="10.04.02",
            title=u"Maatregelen tegen \"mobile code\"",
            text=u"Als gebruik van \"mobile code\" is toegelaten, behoort de configuratie te bewerkstelligen dat de "
                 u"geautoriseerde \"mobile code\" functioneert volgens een duidelijk vastgesteld beveiligingsbeleid, "
                 u"en behoort te worden voorkomen dat onbevoegde \"mobile code\" wordt uitgevoerd.",
            fragments=[
                Verifier(
                    identifier="10.04.02/01",
                    title=u"",
                    text=u"Mobile code wordt uitgevoerd in een logisch geïsoleerde omgeving (sandbox) om de kans op "
                         u"aantasting van de integriteit van het systeem te verkleinen. De mobile code wordt altijd "
                         u"uitgevoerd met minimale rechten zodat de integriteit van het host systeem niet aangetast "
                         u"wordt.",
                ),
                Verifier(
                    identifier="10.04.02/02",
                    title=u"",
                    text=u"Een gebruiker moet geen extra rechten kunnen toekennen aan programma's (bijv. internet "
                         u"browsers) die mobiele code uitvoeren.",
                ),
            ],
        ),
    ],
)


S1005 = Section(
    identifier="10.05",
    title=u"Back-up",
    fragments=[
        Norm(
            identifier="10.05.01",
            title=u"Reservekopieën maken (back-ups)",
            text=u"Er behoren back-upkopieën van informatie en programmatuur te worden gemaakt en regelmatig te worden "
                 u"getest overeenkomstig het vastgestelde back-upbeleid.",
            fragments=[
                Verifier(
                    identifier="10.05.01/01",
                    title=u"",
                    text=u"Er zijn (geteste) procedures voor back-up en recovery van informatie voor herinrichting en "
                         u"foutherstel van verwerkingen.",
                ),
                Verifier(
                    identifier="10.05.01/02",
                    title=u"",
                    text=u"Back-upstrategieën zijn vastgesteld op basis van het soort gegevens (bestanden, databases, "
                         u"enz.), de maximaal toegestane periode waarover gegevens verloren mogen raken, en de "
                         u"maximaal toelaatbare back-up- en hersteltijd.",
                ),
                Verifier(
                    identifier="10.05.01/03",
                    title=u"",
                    text=u"Van back-upactiviteiten en de verblijfplaats van de media wordt een registratie "
                         u"bijgehouden, met een kopie op een andere locatie. De andere locatie is zodanig gekozen "
                         u"dat een incident/calamiteit op de oorspronkelijke locatie niet leidt tot schade aan of "
                         u"toegang tot de kopie van die registratie.",
                ),
                Verifier(
                    identifier="10.05.01/04",
                    title=u"",
                    text=u"Back-ups worden bewaard op een locatie die zodanig is gekozen dat een incident op de "
                         u"oorspronkelijke locatie niet leidt tot schade aan de back-up.",
                ),
                Verifier(
                    identifier="10.05.01/05",
                    title=u"",
                    text=u"De fysieke en logische toegang tot de back-ups, zowel van systeemschijven als van data, is "
                         u"zodanig geregeld dat alleen geautoriseerde personen zich toegang kunnen verschaffen tot "
                         u"deze back-ups.",
                ),
            ],
        ),
    ],
)


S1006 = Section(
    identifier="10.06",
    title=u"Beheer van netwerkbeveiliging",
    fragments=[
        Norm(
            identifier="10.06.01",
            title=u"Maatregelen voor netwerken",
            text=u"Netwerken behoren adequaat te worden beheerd en beheerst om ze te beschermen tegen bedreigingen en "
                 u"om beveiliging te handhaven voor de systemen en toepassingen die gebruikmaken van het netwerk, "
                 u"waaronder informatie die wordt getransporteerd.",
            fragments=[
                Verifier(
                    identifier="10.06.01/01",
                    title=u"",
                    text=u"Het netwerk wordt gemonitord en beheerd zodat aanvallen, storingen of fouten ontdekt en "
                         u"hersteld kunnen worden en de betrouwbaarheid van het netwerk niet onder het afgesproken "
                         u"minimum niveau komt.",
                ),
                Verifier(
                    identifier="10.06.01/01",
                    title=u"",
                    text=u"Gegevensuitwisseling tussen vertrouwde en onvertrouwde zones dient inhoudelijk "
                         u"geautomatiseerd gecontroleerd te worden op aanwezigheid van malware.",
                ),
                Verifier(
                    identifier="10.06.01/02",
                    title=u"",
                    text=u"Bij transport van vertrouwelijke informatie over onvertrouwde netwerken, zoals het "
                         u"internet, dient altijd geschikte encryptie te worden toegepast. Zie hiertoe "
                         u"[[http:///index.php/BIR_12_-_Verwerving,_ontwikkeling_en_onderhoud_van_Informatiesystemen#"
                         u"12.03.01/3 12.03.01/3]]""",
                ),
                Verifier(
                    identifier="10.06.01/03",
                    title=u"",
                    text=u"Er zijn procedures voor beheer van apparatuur op afstand.",
                ),
            ],
        ),
        Norm(
            identifier="10.06.02",
            title=u"Beveiliging van netwerkdiensten",
            text=u"Netwerken behoren adequaat te worden beheerd en beheerst om ze te beschermen tegen bedreigingen en "
                 u"om beveiliging te handhaven voor de systemen en toepassingen die gebruikmaken van het netwerk, "
                 u"waaronder informatie die wordt getransporteerd.",
            fragments=[
                Verifier(
                    identifier="10.06.02/01",
                    title=u"",
                    text=u"Beveiligingskenmerken, niveaus van dienstverlening en beheerseisen voor alle n"
                         u"etwerkdiensten behoren te worden geïdentificeerd en opgenomen in elke overeenkomst voor "
                         u"netwerkdiensten, zowel voor diensten die intern worden geleverd als voor uitbestede "
                         u"diensten.",
                ),
            ],
        ),
    ],
)


S1007 = Section(
    identifier="10.07",
    title=u"Behandeling van media",
    fragments=[
        Norm(
            identifier="10.07.01",
            title=u"Beheer van verwijderbare media",
            text=u"Er behoren procedures te zijn vastgesteld voor het beheer van verwijderbare media.",
            fragments=[
                Verifier(
                    identifier="10.07.01/01",
                    title=u"",
                    text=u"Er zijn procedures opgesteld en geïmplementeerd voor opslag van vertrouwelijke informatie "
                         u"voor verwijderbare media.",
                ),
                Verifier(
                    identifier="10.07.01/02",
                    title=u"",
                    text=u"Verwijderbare media met vertrouwelijke informatie mogen niet onbeheerd worden achtergelaten "
                         u"op plaatsen die toegankelijk zijn zonder toegangscontrole.",
                ),
                Verifier(
                    identifier="10.07.01/03",
                    title=u"",
                    text=u"In het geval dat media een kortere verwachte levensduur hebben dan de gegevens die ze "
                         u"bevatten, worden de gegevens gekopieerd wanneer 75% van de levensduur van het medium is "
                         u"verstreken.",
                ),
                Verifier(
                    identifier="10.07.01/04",
                    title=u"",
                    text=u"Gegevensdragers worden behandeld volgens de voorschriften van de fabrikant.",
                ),
            ],
        ),
        Norm(
            identifier="10.07.02",
            title=u"Verwijdering van media",
            text=u"Media behoren op een veilige en beveiligde manier te worden verwijderd als ze niet langer nodig "
                 u"zijn.",
            fragments=[
                Verifier(
                    identifier="10.07.02/01",
                    title=u"",
                    text=u"Er zijn procedures vastgesteld en in werking voor verwijderen van vertrouwelijke data en "
                         u"de vernietiging van verwijderbare media. Verwijderen van data wordt gedaan met een "
                         u"Secure Erase voor apparaten waar dit mogelijk is. In overige gevallen wordt de data twee "
                         u"keer overschreven met vaste data, één keer met random data en vervolgens wordt geverifieerd "
                         u"of het overschrijven is gelukt.",
                ),
            ],
        ),
        Norm(
            identifier="10.07.03",
            title=u"Procedures voor de behandeling van informatie",
            text=u"Er behoren procedures te worden vastgesteld voor de behandeling en opslag van informatie om deze te "
                 u"beschermen tegen onbevoegde openbaarmaking of misbruik.",
            fragments=[
                Verifier(
                    identifier="10.07.03/01",
                    title=u"",
                    text=u"- conform norm -""",
                ),
            ],
        ),
        Norm(
            identifier="10.07.04",
            title=u"Beveiliging van systeemdocumentatie",
            text=u"Systeemdocumentatie behoort te worden beschermd tegen onbevoegde toegang.",
            fragments=[
                Verifier(
                    identifier="10.07.04/01",
                    title=u"",
                    text=u"Systeemdocumentatie die vertrouwelijke informatie bevat is niet vrij toegankelijk.",
                ),
                Verifier(
                    identifier="10.07.04/02",
                    title=u"",
                    text=u"Wanneer de eigenaar er expliciet voor kiest om gerubriceerde systeemdocumentatie buiten de "
                         u"rijksdienst te brengen, doet hij dat niet zonder risicoafweging.",
                ),
            ],
        ),
    ],
)


S1008 = Section(
    identifier="10.08",
    title=u"Uitwisseling van informatie",
    fragments=[
        Norm(
            identifier="10.08.01",
            title=u"Beleid en procedures voor informatie-uitwisseling",
            text=u"Er behoren formeel beleid, formele procedures en formele beheersmaatregelen te zijn vastgesteld "
                 u"om de uitwisseling van informatie via het gebruik van alle typen communicatiefaciliteiten te "
                 u"beschermen.",
            fragments=[
                Verifier(
                    identifier="10.08.01/01",
                    title=u"",
                    text=u"Het meenemen van Departementaal Vertrouwelijke informatie buiten gecontroleerd gebied "
                         u"vindt uitsluitend plaats indien dit voor de uitoefening van de functie noodzakelijk is.",
                ),
                Verifier(
                    identifier="10.08.01/02",
                    title=u"",
                    text=u"Medewerkers zijn geïnstrueerd om zodanig om te gaan met (telefoon)gesprekken, e-mail, faxen "
                         u"en ingesproken berichten op antwoordapparaten dat de kans op uitlekken van vertrouwelijke "
                         u"informatie geminimaliseerd wordt.",
                ),
                Verifier(
                    identifier="10.08.01/03",
                    title=u"",
                    text=u"Medewerkers zijn geïnstrueerd om zodanig om te gaan met mobiele apparatuur en verwijderbare "
                         u"media dat de kans op uitlekken van vertrouwelijke informatie geminimaliseerd wordt. Hierbij "
                         u"wordt minimaal aandacht besteed aan het risico van adreslijsten en opgeslagen boodschappen "
                         u"in mobiele telefoons.",
                ),
                Verifier(
                    identifier="10.08.01/03",
                    title=u"",
                    text=u"Medewerkers zijn geïnstrueerd om geen vertrouwelijke documenten bij de printer te laten "
                         u"liggen.",
                ),
                Verifier(
                    identifier="10.08.01/03",
                    title=u"",
                    text=u"Er zijn maatregelen getroffen om het automatisch doorsturen van interne e-mail berichten "
                         u"aar externe e-mail adressen te voorkomen.",
                ),
            ],
        ),
        Norm(
            identifier="10.08.02",
            title=u"Uitwisselingsovereenkomsten",
            text=u"Er behoren overeenkomsten te worden vastgesteld voor de uitwisseling van informatie en "
                 u"programmatuur tussen de organisatie en externe partijen.",
            fragments=[
                Verifier(
                    identifier="10.08.02/01",
                    title=u"",
                    text=u"Er zijn afspraken gemaakt over de beveiliging van de uitwisseling van gegevens en software "
                         u"tussen organisaties waarin de maatregelen om betrouwbaarheid, waaronder traceerbaarheid en "
                         u"onweerlegbaarheid, van gegevens te waarborgen zijn beschreven en getoetst.",
                ),
                Verifier(
                    identifier="10.08.02/02",
                    title=u"",
                    text=u"Verantwoordelijkheid en aansprakelijkheid in het geval van informatiebeveiligingsincidenten "
                         u"zijn beschreven, alsmede procedures over melding van incidenten.",
                ),
                Verifier(
                    identifier="10.08.02/03",
                    title=u"",
                    text=u"Het eigenaarschap van gegevens en programmatuur en de verantwoordelijkheid voor de "
                         u"gegevensbescherming, auteursrechten, licenties van programmatuur zijn vastgelegd.",
                ),
                Verifier(
                    identifier="10.08.02/04",
                    title=u"",
                    text=u"Indien mogelijk wordt binnenkomende programmatuur (zowel op fysieke media als gedownload) "
                         u"gecontroleerd op ongeautoriseerde wijzigingen aan de hand van een door de leverancier via "
                         u"een gescheiden kanaal geleverde checksum of certificaat.",
                ),
            ],
        ),
        Norm(
            identifier="10.08.03",
            title=u"Fysieke media die worden getransporteerd",
            text=u"Media die informatie bevatten behoren te worden beschermd tegen onbevoegde toegang, misbruik of "
                 u"corrumperen tijdens transport buiten de fysieke begrenzing van de organisatie.",
            fragments=[
                Verifier(
                    identifier="10.08.03/01",
                    title=u"",
                    text=u"""Om vertrouwelijke informatie te beschermen worden maatregelen genomen, zoals:
<ul>
<li>versleuteling</li>
<li>bescherming door fysieke maatregelen, zoals afgesloten containers</li>
<li>gebruik van verpakkingsmateriaal waaraan te zien is of getracht is het te openen</li>
<li>persoonlijke aflevering</li>
<li>opsplitsing van zendingen in meerdere delen en eventueel verzending via verschillende routes</li>
</ul>""",
                ),
                Verifier(
                    identifier="10.08.03/02",
                    title=u"",
                    text=u"Fysieke verzending van bijzondere informatie dient te geschieden met ministerieel "
                         u"goedgekeurde middelen, waardoor de inhoud niet zichtbaar, niet kenbaar en inbreuk "
                         u"detecteerbaar is.",
                ),
            ],
        ),
        Norm(
            identifier="10.08.04",
            title=u"Elektronisch berichtenuitwisseling",
            text=u"Informatie die een rol speelt bij elektronische berichtuitwisseling behoort op geschikte wijze te "
                 u"worden beschermd.",
            fragments=[
                Verifier(
                    identifier="10.08.04/01",
                    title=u"",
                    text=u"Digitale documenten binnen de rijksdienst waar eindgebruikers rechten aan kunnen ontlenen "
                         u"maken gebruik van PKI Overheid.",
                ),
                Verifier(
                    identifier="10.08.04/02",
                    title=u"",
                    text=u"Er is een (spam) filter geactiveerd voor e-mail berichten.",
                ),
            ],
        ),
        Norm(
            identifier="10.08.05",
            title=u"Systemen voor bedrijfsinformatie",
            text=u"Beleid en procedures behoren te worden ontwikkeld en geïmplementeerd om informatie te beschermen "
                 u"die een rol speelt bij de onderlinge koppeling van systemen voor bedrijfsinformatie.",
            fragments=[
                Verifier(
                    identifier="10.08.05/01",
                    title=u"",
                    text=u"Er zijn richtlijnen met betrekking tot het bepalen van de risico's die het gebruik van "
                         u"kantoorapplicaties met zich meebrengen en richtlijnen voor de bepaling van de beveiliging "
                         u"van kantoorapplicaties. Hierin is minimaal aandacht besteed aan de toegang tot de interne "
                         u"informatievoorziening, toegankelijkheid van agenda's, afscherming van documenten, "
                         u"beschikbaarheid en backup.",
                ),
            ],
        ),
    ],
)


S1009 = Section(
    identifier="10.09",
    title=u"Diensten voor e-commerce",
    fragments=[
        Norm(
            identifier="10.09.01",
            title=u"E-commerce",
            text=u"Informatie die een rol speelt bij e-commerce en die via openbare netwerken wordt uitgewisseld, "
                 u"behoort te worden beschermd tegen frauduleuze activiteiten, geschillen over contracten en "
                 u"onbevoegde openbaarmaking en modificatie.",
            fragments=[
                Verifier(
                    identifier="10.09.01/01",
                    title=u"",
                    text=u"Waar mogelijk worden authentieke basisregistraties van de overheid gebruikt (b.v. GBA).",
                ),
            ],
        ),
        Norm(
            identifier="10.09.02",
            title=u"Onlinetransacties",
            text=u"Informatie die een rol speelt bij online transacties behoort te worden beschermd om onvolledige "
                 u"overdracht, onjuiste routing, onbevoegde wijziging van berichten, onbevoegde openbaarmaking, "
                 u"onbevoegde duplicatie of weergave van berichten te voorkomen.",
            fragments=[
                Verifier(
                    identifier="10.09.02/01",
                    title=u"",
                    text=u"Een transactie wordt bevestigd door een (gekwalificeerde) elektronische handtekening of "
                         u"een andere wilsuiting (bijv. een TAN code) van de gebruiker.",
                ),
                Verifier(
                    identifier="10.09.02/02",
                    title=u"",
                    text=u"Een transactie is versleuteld, de partijen zijn geauthenticeerd en de privacy van "
                         u"betrokken partijen is gewaarborgd.",
                ),
            ],
        ),
        Norm(
            identifier="10.09.03",
            title=u"Openbaar beschikbare informatie",
            text=u"De betrouwbaarheid van de informatie die beschikbaar wordt gesteld op een openbaar toegankelijk "
                 u"systeem behoort te worden beschermd om onbevoegde modificatie te voorkomen.",
            fragments=[
                Verifier(
                    identifier="10.09.03/01",
                    title=u"",
                    text=u"Er zijn procedures die waarborgen dat gepubliceerde informatie is aangeleverd door daartoe "
                         u"geautoriseerde medewerkers.",
                ),
            ],
        ),
    ],
)


S1010 = Section(
    identifier="10.10",
    title=u"Controle",
    fragments=[
        Norm(
            identifier="10.10.01",
            title=u"Aanmaken audit-logbestanden",
            text=u"Activiteiten van gebruikers, uitzonderingen en informatiebeveiligingsgebeurtenissen behoren te "
                 u"worden vastgelegd in audit-logbestanden. Deze logbestanden behoren gedurende een overeengekomen "
                 u"periode te worden bewaard, ten behoeve van toekomstig onderzoek en toegangscontrole.",
            fragments=[
                Verifier(
                    identifier="10.10.01/01",
                    title=u"",
                    text=u"Van logbestanden worden rapportages gemaakt die periodiek, minimaal maandelijks, "
                         u"worden beoordeeld.",
                ),
                Verifier(
                    identifier="10.10.01/02",
                    title=u"",
                    text=u"""Een logregel bevat minimaal:
<ul>
<li>een tot een natuurlijk persoon herleidbare gebruikersnaam of ID</li>
<li>de gebeurtenis (zie [[#10.10.02/1]])</li>
<li>waar mogelijk de identiteit van het werkstation of de locatie</li>
<li>het object waarop de handeling werd uitgevoerd</li>
<li>het resultaat van de handeling</li>
<li>de datum en het tijdstip van de gebeurtenis</li>
</ul>""",
                ),
                Verifier(
                    identifier="10.10.01/03",
                    title=u"",
                    text=u"In een logregel worden in geen geval gevoelige gegevens opgenomen. Dit betreft onder "
                         u"meer gegevens waarmee de beveiliging doorbroken kan worden (zoals wachtwoorden, "
                         u"inbelnummers, enz.).",
                ),
                Verifier(
                    identifier="10.10.01/04",
                    title=u"",
                    text=u"Logberichten worden overzichtelijk samengevat. Daartoe zijn systemen die logberichten "
                         u"genereren aangesloten op een Security Information and Event Management systeem (SIEM15) "
                         u"waarmee meldingen en alarmoproepen aan de beheerorganisatie gegeven worden. Er is "
                         u"vastgelegd bij welke drempelwaarden meldingen en alarmoproepen gegenereerd worden.",
                ),
                Verifier(
                    identifier="10.10.01/04",
                    title=u"",
                    text=u"Controle op opslag van logging: het vollopen van het opslagmedium voor de logbestanden "
                         u"boven een bepaalde grens wordt gelogd en leidt tot automatische alarmering van de "
                         u"beheerorganisatie. Dit geldt ook als het bewaren van loggegevens niet (meer) mogelijk is "
                         u"(bijv. een logserver die niet bereikbaar is).",
                ),
            ],
        ),
        Norm(
            identifier="10.10.02",
            title=u"Controle van systeemgebruik",
            text=u"Er behoren procedures te worden vastgesteld om het gebruik van IT voorzieningen te controleren. "
                 u"Het resultaat van de controleactiviteiten behoort regelmatig te worden beoordeeld.",
            fragments=[
                Verifier(
                    identifier="10.10.02/01",
                    title=u"",
                    text=u"Van logbestanden worden rapportages gemaakt die periodiek, minimaal maandelijks, worden "
                         u"beoordeeld.",
                ),
            ],
        ),
        Norm(
            identifier="10.10.03",
            title=u"Bescherming van informatie in logbestanden",
            text=u"Logfaciliteiten en informatie in logbestanden behoren te worden beschermd tegen inbreuk en "
                 u"onbevoegde toegang.",
            fragments=[
                Verifier(
                    identifier="10.10.03/01",
                    title=u"",
                    text=u"Het (automatisch) overschrijven of verwijderen van logbestanden wordt gelogd in de nieuw "
                         u"aangelegde log.",
                ),
                Verifier(
                    identifier="10.10.03/02",
                    title=u"",
                    text=u"Het raadplegen van logbestanden is voorbehouden aan geautoriseerde gebruikers. Hierbij is "
                         u"de toegang beperkt tot leesrechten.",
                ),
                Verifier(
                    identifier="10.10.03/03",
                    title=u"",
                    text=u"Logbestanden worden zodanig beschermd dat deze niet aangepast of gemanipuleerd kunnen "
                         u"worden.",
                ),
                Verifier(
                    identifier="10.10.03/04",
                    title=u"",
                    text=u"De instellingen van logmechanismen worden zodanig beschermd dat deze niet aangepast of "
                         u"gemanipuleerd kunnen worden. Indien de instellingen aangepast moeten te worden zal daarbij "
                         u"altijd het vier ogen principe toegepast worden.",
                ),
                Verifier(
                    identifier="10.10.03/05",
                    title=u"",
                    text=u"De beschikbaarheid van loginformatie is gewaarborgd binnen de termijn waarin loganalyse "
                         u"noodzakelijk wordt geacht, met een minimum van drie maanden, conform de wensen van de "
                         u"systeemeigenaar. Bij een (vermoed) informatiebeveiligingsincident is de bewaartermijn "
                         u"minimaal drie jaar.",
                ),
                Verifier(
                    identifier="10.10.03/05",
                    title=u"",
                    text=u"Controle op opslag van logging: het vollopen van het opslagmedium voor de logbestanden "
                         u"boven een bepaalde grens wordt gelogd en leidt tot automatische alarmering van de "
                         u"beheerorganisatie. Dit geldt ook als het bewaren van loggegevens niet (meer) mogelijk is "
                         u"(bijv. een logserver die niet bereikbaar is).",
                ),
            ],
        ),
        Norm(
            identifier="10.10.04",
            title=u"Logbestanden van administrators en operators",
            text=u"Activiteiten van systeemadministrators en systeemoperators behoren in logbestanden te worden "
                 u"vastgelegd.",
            fragments=[
                Verifier(
                    identifier="10.10.04/01",
                    title=u"",
                    text=u"In een logregel worden in geen geval gevoelige gegevens opgenomen. Dit betreft onder "
                         u"meer gegevens waarmee de beveiliging doorbroken kan worden (zoals wachtwoorden, "
                         u"inbelnummers, enz.).",
                ),
                Verifier(
                    identifier="10.10.04/02",
                    title=u"",
                    text=u"Controle op opslag van logging: het vollopen van het opslagmedium voor de logbestanden "
                         u"boven een bepaalde grens wordt gelogd en leidt tot automatische alarmering van de "
                         u"beheerorganisatie. Dit geldt ook als het bewaren van loggegevens niet (meer) mogelijk is "
                         u"(bijv. een logserver die niet bereikbaar is).",
                ),
            ],
        ),
        Norm(
            identifier="10.10.05",
            title=u"Registratie van storingen",
            text=u"Storingen behoren in logbestanden te worden vastgelegd en te worden geanalyseerd en er behoren "
                 u"geschikte maatregelen te worden genomen.",
            fragments=[
                Verifier(
                    identifier="10.10.05/01",
                    title=u"",
                    text=u"In een logregel worden in geen geval gevoelige gegevens opgenomen. Dit betreft onder "
                         u"meer gegevens waarmee de beveiliging doorbroken kan worden (zoals wachtwoorden, "
                         u"inbelnummers, enz.).",
                ),
            ],
        ),
        Norm(
            identifier="10.10.06",
            title=u"Synchronisatie van systeemklokken",
            text=u"De klokken van alle relevante informatiesystemen binnen een organisatie of beveiligingsdomein "
                 u"behoren te worden gesynchroniseerd met een overeengekomen nauwkeurige tijdsbron.",
            fragments=[
                Verifier(
                    identifier="10.10.05/01",
                    title=u"",
                    text=u"Systeemklokken worden zodanig gesynchroniseerd dat altijd een betrouwbare analyse van "
                         u"logbestanden mogelijk is.",
                ),
            ],
        ),
    ],
)


CH10 = Chapter(
    identifier="10",
    title=u"Beheer van Communicatie en Bedieningsprocessen",
    fragments=[
        S1001,
        S1002,
        S1003,
        S1004,
        S1005,
        S1006,
        S1007,
        S1008,
        S1009,
        S1010,
    ]
)
