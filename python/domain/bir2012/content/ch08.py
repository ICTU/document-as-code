# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S0801 = Section(
    identifier="08.01",
    title="Beveiligen van personeel",
    fragments=[
        Norm(
            identifier="08.01.01",
            title="Rollen en verantwoordelijkheden",
            text="De rollen en verantwoordelijkheden van werknemers, ingehuurd personeel en externe gebruikers ten "
                 "aanzien van beveiliging behoren te worden vastgesteld en gedocumenteerd overeenkomstig het beleid "
                 "voor informatiebeveiliging van de organisatie.",
            fragments=[
                Verifier(
                    identifier="08.01.01/01",
                    title="",
                    text="""De taken en verantwoordelijkheden van een medewerker zijn opgenomen in de 
                    functiebeschrijving (zie ook de Ambtenarenwet) en worden onderhouden. In de functiebeschrijving 
                    wordt minimaal aandacht besteed aan:
<ul>
<li>uitvoering van het informatiebeveiligingsbeleid</li>
<li>bescherming van bedrijfsmiddelen</li>
<li>rapportage van beveiligingsincidenten</li>
</ul>""",
                ),
                Verifier(
                    identifier="08.01.01/02",
                    title="",
                    text="Alle ambtenaren en ingehuurde medewerkers krijgen bij hun aanstelling hun "
                         "verantwoordelijkheden ten aanzien van informatiebeveiliging ter inzage. De schriftelijk "
                         "vastgestelde en voor hen geldende regelingen en instructies ten aanzien van "
                         "informatiebeveiliging, welke zij bij de vervulling van hun dienst hebben na te leven, "
                         "worden op een gemakkelijk toegankelijke plaats ter inzage gelegd. Overeenkomstige "
                         "voorschriften maken deel uit van de contracten met externe partijen. Ook voor hen geldt de "
                         "toegankelijkheid van geldende regelingen en instructies.",
                ),
                Verifier(
                    identifier="08.01.01/03",
                    title="",
                    text="Indien een medewerker speciale verantwoordelijkheden heeft t.a.v. informatiebeveiliging "
                         "dan is hem dat voor indiensttreding (of bij functiewijziging), bij voorkeur in de "
                         "aanstellingsbrief of bij het afsluiten van het contract, aantoonbaar duidelijk gemaakt.",
                ),
                Verifier(
                    identifier="08.01.01/04",
                    title="",
                    text="De algemene voorwaarden van het arbeidscontract van medewerkers bevatten de wederzijdse "
                         "verantwoordelijkheden ten aanzien van beveiliging. Het is aantoonbaar dat medewerkers "
                         "bekend zijn met hun verantwoordelijkheden op het gebied van beveiliging.",
                ),
            ],
        ),
        Norm(
            identifier="08.01.02",
            title="Screening",
            text="Verificatie van de achtergrond van alle kandidaten voor een dienstverband, ingehuurd personeel en "
                 "externe gebruikers behoren te worden uitgevoerd overeenkomstig relevante wetten, voorschriften en "
                 "ethische overwegingen, en behoren evenredig te zijn aan de bedrijfseisen, de classificatie van de "
                 "informatie waartoe toegang wordt verleend, en de waargenomen risico's.",
            fragments=[
                Verifier(
                    identifier="08.01.02/01",
                    title="",
                    text="Voor alle medewerkers (ambtenaren en externe medewerkers) is minimaal een relevante "
                         "Verklaring Omtrent het Gedrag (VOG) vereist. Indien het een vertrouwensfunctie betreft "
                         "wordt ook een veiligheidsonderzoek (Verklaring van Geen Bezwaar) uitgevoerd.",
                ),
                Verifier(
                    identifier="08.01.02/02",
                    title="",
                    text="Bij de aanstelling worden de gegevens die de medewerker heeft verstrekt over zijn "
                         "arbeidsverleden en scholing geverifieerd.",
                ),
            ],
        ),
        Norm(
            identifier="08.01.03",
            title="Arbeidsvoorwaarden",
            text="Als onderdeel van hun contractuele verplichting behoren werknemers, ingehuurd personeel en externe "
                 "gebruikers de algemene voorwaarden te aanvaarden en te ondertekenen van hun arbeidscontract, waarin "
                 "hun verantwoordelijkheden en die van de organisatie ten aanzien van informatiebeveiliging behoren "
                 "te zijn vastgelegd.",
            fragments=[
                Verifier(
                    identifier="08.01.03/01",
                    title="",
                    text="- conform norm -",
                ),
            ],
        ),
    ],
)


S0802 = Section(
    identifier="08.02",
    title="Tijdens het dienstverband",
    fragments=[
        Norm(
            identifier="08.02.01",
            title="Directieverantwoordelijkheid",
            text="De directie behoort van werknemers, ingehuurd personeel en externe gebruikers te eisen dat "
                 "ze beveiliging toepassen overeenkomstig vastgesteld beleid en vastgestelde procedures van de "
                 "organisatie.",
            fragments=[
                Verifier(
                    identifier="08.02.01/01",
                    title="",
                    text="Het lijnmanagement heeft een strategie ontwikkeld en geÔmplementeerd om blijvend over "
                         "specialistische kennis en vaardigheden van rijksambtenaren en ingehuurd personeel (die "
                         "kritische bedrijfsactiviteiten op het gebied van IB uitoefenen) te kunnen beschikken.",
                ),
                Verifier(
                    identifier="08.02.01/02",
                    title="",
                    text="Het lijnmanagement bevordert dat rijksambtenaren, ingehuurd personeel en (waar van "
                         "toepassing) externe gebruikers van interne systemen algemene beveiligingsaspecten toepassen "
                         "in hun gedrag en handelingen overeenkomstig vastgesteld beleid.",
                ),
            ],
        ),
        Norm(
            identifier="08.02.02",
            title="Bewustzijn, opleiding en training ten aanzien van informatiebeveiliging",
            text="Alle werknemers van de organisatie en, voorzover van toepassing, ingehuurd personeel en externe "
                 "gebruikers, behoren geschikte training en regelmatige bijscholing te krijgen met betrekking tot "
                 "beleid en procedures van de organisatie, voor zover relevant voor hun functie.",
            fragments=[
                Verifier(
                    identifier="08.02.02/01",
                    title="",
                    text="Alle medewerkers van de organisatie worden regelmatig attent gemaakt op het "
                         "beveiligingsbeleid en de beveiligingsprocedures van de organisatie, voor zover relevant "
                         "voor hun functie.",
                ),
            ],
        ),
        Norm(
            identifier="08.02.03",
            title="Disciplinaire maatregelen",
            text="Er behoort een formeel disciplinair proces te zijn vastgesteld voor werknemers die inbreuk op de "
                 "beveiliging hebben gepleegd.",
            fragments=[
                Verifier(
                    identifier="08.02.03/01",
                    title="",
                    text="Er is een disciplinair proces vastgelegd voor medewerkers die inbreuk maken op het "
                         "beveiligingsbeleid.",
                ),
            ],
        ),
    ],
)


S0803 = Section(
    identifier="08.03",
    title="BeŽindiging of wijziging van het dienstverband",
    fragments=[
        Norm(
            identifier="08.03.01",
            title="BeŽindiging van verantwoordelijkheden",
            text="De verantwoordelijkheden voor beŽindiging of wijziging van het dienstverband behoren duidelijk te "
                 "zijn vastgesteld en toegewezen.",
            fragments=[
                Verifier(
                    identifier="08.03.01/01",
                    title="",
                    text="Voor ambtenaren is in de ambtseed of belofte vastgelegd welke verplichtingen ook na "
                         "beŽindiging van het dienstverband of bij functiewijziging nog van kracht blijven en "
                         "voor hoe lang. Voor ingehuurd personeel (zowel in dienst van een derde bedrijf als "
                         "individueel) is dit contractueel vastgelegd. Indien nodig wordt een "
                         "geheimhoudingsverklaring ondertekend.",
                ),
                Verifier(
                    identifier="08.03.01/02",
                    title="",
                    text="Het lijnmanagement heeft een procedure vastgesteld voor beŽindiging van dienstverband, "
                         "contract of overeenkomst waarin minimaal aandacht besteed wordt aan het intrekken van "
                         "toegangsrechten, innemen van bedrijfsmiddelen en welke verplichtingen ook na beŽindiging "
                         "van het dienstverband blijven gelden.",
                ),
                Verifier(
                    identifier="08.03.01/03",
                    title="",
                    text="Het lijnmanagement heeft een procedure vastgesteld voor verandering van functie binnen de "
                         "organisatie, waarin minimaal aandacht besteed wordt aan het intrekken van toegangsrechten "
                         "en innemen van bedrijfsmiddelen die niet meer nodig zijn na het beŽindigen van de oude "
                         "functie.",
                ),
            ],
        ),
        Norm(
            identifier="08.03.02",
            title="Retournering van bedrijfsmiddelen",
            text="Alle werknemers, ingehuurd personeel en externe gebruikers behoren alle bedrijfsmiddelen van de "
                 "organisatie die ze in hun bezit hebben te retourneren bij beŽindiging van hun dienstverband, "
                 "contract of overeenkomst.",
            fragments=[
                Verifier(
                    identifier="08.03.02/01",
                    title="",
                    text="Het lijnmanagement heeft een procedure vastgesteld voor verandering van functie binnen de "
                         "organisatie, waarin minimaal aandacht besteed wordt aan het intrekken van toegangsrechten "
                         "en innemen van bedrijfsmiddelen die niet meer nodig zijn na het beŽindigen van de oude "
                         "functie.",
                ),
            ],
        ),
        Norm(
            identifier="08.03.03",
            title="Blokkering van toegangsrechten",
            text="De toegangsrechten van alle werknemers, ingehuurd personeel en externe gebruikers tot informatie "
                 "en ICT-voorzieningen behoren te worden geblokkeerd bij beŽindiging van het dienstverband, het "
                 "contract of de overeenkomst, of behoort na wijziging te worden aangepast.",
            fragments=[
                Verifier(
                    identifier="08.03.03/01",
                    title="",
                    text="Het lijnmanagement heeft een procedure vastgesteld voor verandering van functie binnen de "
                         "organisatie, waarin minimaal aandacht besteed wordt aan het intrekken van toegangsrechten "
                         "en innemen van bedrijfsmiddelen die niet meer nodig zijn na het beŽindigen van de oude "
                         "functie.",
                ),
            ],
        ),
    ],
)


CH08 = Chapter(
    identifier="08",
    title="Personele beveiliging",
    fragments=[
        S0801,
        S0802,
        S0803,
    ]
)
