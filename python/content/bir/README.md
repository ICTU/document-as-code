Document-as-code: BIR
=====================

De baseline informatiebeveiliging rijksdienst (BIR) bestaat uit elf hoofdstukken (05-15),
met in totaal 255 punten waaraan invulling gegeven moet worden.
Dit kan een knap lastige administratie worden.

Door in 'bir_measures.py' de getroffen maatregelen te creeren en aan te geven aan welke punten
(verifiers) een maatregel invulling geeft, kan eenvoudig een overzichtsrapportage gemaakt worden
met 'bir_document.py' uit het topniveau van deze codeboom.
Plaats punten waarvoor een geaccepteerde afwijking bestaat in 'Explained',
punten die als 'niet van toepassing' geaccepteerd zijn in 'NotApplicable'.
