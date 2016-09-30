# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""

from __future__ import absolute_import
from __future__ import print_function


from domain.document.model.chapter import Chapter
from domain.document.model.section import Section
from domain.document.model.norm import Norm
from domain.document.model.verifier import Verifier


S0801 = Section(
    identifier="08.01",
    title=u"Beveiligen van personeel",
    fragments=[
        Norm(
            identifier="08.01.01",
            title=u"Rollen en verantwoordelijkheden",
            text=u"De rollen en verantwoordelijkheden van werknemers, ingehuurd personeel en externe gebruikers ten aanzien van beveiliging behoren te worden vastgesteld en gedocumenteerd overeenkomstig het beleid voor informatiebeveiliging van de organisatie.",
            fragments=[
                Verifier(
                    identifier="08.01.01/01",
                    title=u"",
                    text=u"""De taken en verantwoordelijkheden van een medewerker zijn opgenomen in de functiebeschrijving (zie ook de Ambtenarenwet) en worden onderhouden. In de functiebeschrijving wordt minimaal aandacht besteed aan:
<ul>
<li> uitvoering van het informatiebeveiligingsbeleid
<li> bescherming van bedrijfsmiddelen
<li> rapportage van beveiligingsincidenten
</ul>""",
                ),
                Verifier(
                    identifier="08.01.01/02",
                    title=u"",
                    text=u"Alle ambtenaren en ingehuurde medewerkers krijgen bij hun aanstelling hun verantwoordelijkheden ten aanzien van informatiebeveiliging ter inzage. De schriftelijk vastgestelde en voor hen geldende regelingen en instructies ten aanzien van informatiebeveiliging, welke zij bij de vervulling van hun dienst hebben na te leven, worden op een gemakkelijk toegankelijke plaats ter inzage gelegd. Overeenkomstige voorschriften maken deel uit van de contracten met externe partijen. Ook voor hen geldt de toegankelijkheid van geldende regelingen en instructies.",
                ),
                Verifier(
                    identifier="08.01.01/03",
                    title=u"",
                    text=u"Indien een medewerker speciale verantwoordelijkheden heeft t.a.v. informatiebeveiliging dan is hem dat voor indiensttreding (of bij functiewijziging), bij voorkeur in de aanstellingsbrief of bij het afsluiten van het contract, aantoonbaar duidelijk gemaakt.",
                ),
                Verifier(
                    identifier="08.01.01/04",
                    title=u"",
                    text=u"De algemene voorwaarden van het arbeidscontract van medewerkers bevatten de wederzijdse verantwoordelijkheden ten aanzien van beveiliging. Het is aantoonbaar dat medewerkers bekend zijn met hun verantwoordelijkheden op het gebied van beveiliging.",
                ),
            ],
        ),
        Norm(
            identifier="08.01.02",
            title=u"Screening",
            text=u"Verificatie van de achtergrond van alle kandidaten voor een dienstverband, ingehuurd personeel en externe gebruikers behoren te worden uitgevoerd overeenkomstig relevante wetten, voorschriften en ethische overwegingen, en behoren evenredig te zijn aan de bedrijfseisen, de classificatie van de informatie waartoe toegang wordt verleend, en de waargenomen risico's.",
            fragments=[
                Verifier(
                    identifier="08.01.02/01",
                    title=u"",
                    text=u"Voor alle medewerkers (ambtenaren en externe medewerkers) is minimaal een relevante Verklaring Omtrent het Gedrag (VOG) vereist. Indien het een vertrouwensfunctie betreft wordt ook een veiligheidsonderzoek (Verklaring van Geen Bezwaar) uitgevoerd.",
                ),
                Verifier(
                    identifier="08.01.02/02",
                    title=u"",
                    text=u"Bij de aanstelling worden de gegevens die de medewerker heeft verstrekt over zijn arbeidsverleden en scholing geverifieerd.",
                ),
            ],
        ),
        Norm(
            identifier="08.01.03",
            title=u"Arbeidsvoorwaarden",
            text=u"Als onderdeel van hun contractuele verplichting behoren werknemers, ingehuurd personeel en externe gebruikers de algemene voorwaarden te aanvaarden en te ondertekenen van hun arbeidscontract, waarin hun verantwoordelijkheden en die van de organisatie ten aanzien van informatiebeveiliging behoren te zijn vastgelegd.",
            fragments=[
                Verifier(
                    identifier="08.01.03/01",
                    title=u"",
                    text=u"- conform norm -",
                ),
            ],
        ),
    ],
)


S0802 = Section(
    identifier="08.02",
    title=u"Tijdens het dienstverband",
    fragments=[
        Norm(
            identifier="08.02.01",
            title=u"Directieverantwoordelijkheid",
            text=u"De directie behoort van werknemers, ingehuurd personeel en externe gebruikers te eisen dat ze beveiliging toepassen overeenkomstig vastgesteld beleid en vastgestelde procedures van de organisatie.",
            fragments=[
                Verifier(
                    identifier="08.02.01/01",
                    title=u"",
                    text=u"Het lijnmanagement heeft een strategie ontwikkeld en geïmplementeerd om blijvend over specialistische kennis en vaardigheden van rijksambtenaren en ingehuurd personeel (die kritische bedrijfsactiviteiten op het gebied van IB uitoefenen) te kunnen beschikken.",
                ),
                Verifier(
                    identifier="08.02.01/02",
                    title=u"",
                    text=u"Het lijnmanagement bevordert dat rijksambtenaren, ingehuurd personeel en (waar van toepassing) externe gebruikers van interne systemen algemene beveiligingsaspecten toepassen in hun gedrag en handelingen overeenkomstig vastgesteld beleid.",
                ),
            ],
        ),
        Norm(
            identifier="08.02.02",
            title=u"Bewustzijn, opleiding en training ten aanzien van informatiebeveiliging",
            text=u"Alle werknemers van de organisatie en, voorzover van toepassing, ingehuurd personeel en externe gebruikers, behoren geschikte training en regelmatige bijscholing te krijgen met betrekking tot beleid en procedures van de organisatie, voor zover relevant voor hun functie.",
            fragments=[
                Verifier(
                    identifier="08.02.02/01",
                    title=u"",
                    text=u"Alle medewerkers van de organisatie worden regelmatig attent gemaakt op het beveiligingsbeleid en de beveiligingsprocedures van de organisatie, voor zover relevant voor hun functie.",
                ),
            ],
        ),
        Norm(
            identifier="08.02.03",
            title=u"Disciplinaire maatregelen",
            text=u"Er behoort een formeel disciplinair proces te zijn vastgesteld voor werknemers die inbreuk op de beveiliging hebben gepleegd.",
            fragments=[
                Verifier(
                    identifier="08.02.03/01",
                    title=u"",
                    text=u"Er is een disciplinair proces vastgelegd voor medewerkers die inbreuk maken op het beveiligingsbeleid.",
                ),
            ],
        ),
    ],
)


S0803 = Section(
    identifier="08.03",
    title=u"Beëindiging of wijziging van het dienstverband",
    fragments=[
        Norm(
            identifier="08.03.01",
            title=u"Beëindiging van verantwoordelijkheden",
            text=u"De verantwoordelijkheden voor beëindiging of wijziging van het dienstverband behoren duidelijk te zijn vastgesteld en toegewezen.",
            fragments=[
                Verifier(
                    identifier="08.03.01/01",
                    title=u"",
                    text=u"Voor ambtenaren is in de ambtseed of belofte vastgelegd welke verplichtingen ook na beëindiging van het dienstverband of bij functiewijziging nog van kracht blijven en voor hoe lang. Voor ingehuurd personeel (zowel in dienst van een derde bedrijf als individueel) is dit contractueel vastgelegd. Indien nodig wordt een geheimhoudingsverklaring ondertekend.",
                ),
                Verifier(
                    identifier="08.03.01/02",
                    title=u"",
                    text=u"Het lijnmanagement heeft een procedure vastgesteld voor beëindiging van dienstverband, contract of overeenkomst waarin minimaal aandacht besteed wordt aan het intrekken van toegangsrechten, innemen van bedrijfsmiddelen en welke verplichtingen ook na beëindiging van het dienstverband blijven gelden.",
                ),
                Verifier(
                    identifier="08.03.01/03",
                    title=u"",
                    text=u"Het lijnmanagement heeft een procedure vastgesteld voor verandering van functie binnen de organisatie, waarin minimaal aandacht besteed wordt aan het intrekken van toegangsrechten en innemen van bedrijfsmiddelen die niet meer nodig zijn na het beëindigen van de oude functie.",
                ),
            ],
        ),
        Norm(
            identifier="08.03.02",
            title=u"Retournering van bedrijfsmiddelen",
            text=u"Alle werknemers, ingehuurd personeel en externe gebruikers behoren alle bedrijfsmiddelen van de organisatie die ze in hun bezit hebben te retourneren bij beëindiging van hun dienstverband, contract of overeenkomst.",
            fragments=[
                Verifier(
                    identifier="08.03.02/01",
                    title=u"",
                    text=u"Het lijnmanagement heeft een procedure vastgesteld voor verandering van functie binnen de organisatie, waarin minimaal aandacht besteed wordt aan het intrekken van toegangsrechten en innemen van bedrijfsmiddelen die niet meer nodig zijn na het beëindigen van de oude functie.",
                ),
            ],
        ),
        Norm(
            identifier="08.03.03",
            title=u"Blokkering van toegangsrechten",
            text=u"De toegangsrechten van alle werknemers, ingehuurd personeel en externe gebruikers tot informatie en ICT-voorzieningen behoren te worden geblokkeerd bij beëindiging van het dienstverband, het contract of de overeenkomst, of behoort na wijziging te worden aangepast.",
            fragments=[
                Verifier(
                    identifier="08.03.03/01",
                    title=u"",
                    text=u"Het lijnmanagement heeft een procedure vastgesteld voor verandering van functie binnen de organisatie, waarin minimaal aandacht besteed wordt aan het intrekken van toegangsrechten en innemen van bedrijfsmiddelen die niet meer nodig zijn na het beëindigen van de oude functie.",
                ),
            ],
        ),
    ],
)


CH08 = Chapter(
    identifier="08",
    title=u"Personele beveiliging",
    fragments=[
        S0801,
        S0802,
        S0803,
    ]
)


