# Week 7: Certificeringsexamen (4 uur, 240 minuten)

**Cobot Course — zeven weken, één lesdag per week (240 minuten):**   
**Niveau:** 3-4  
**Machine (Track 1):** Doosan Robotics M1013 — SMEOT Hengelo  

> **Leerdoel:** De kandidaat doorloopt het volledige certificeringsexamen: theorie, storing zoeken en praktijkcase.

## Lesprogramma (240 min)

| Duur | Blok |
|---|---|
| 30 min | Theorie-examen |
| 20-30 min | Find the Error / storingzoeken |
| 180 min | Praktijkcase-examen |

## Informatieblad (Document Type 1 / Template A) — Week 7: Certificeringsexamen (4 uur, 240 minuten)

**Leerdoel:** De kandidaat doorloopt het volledige certificeringsexamen: theorie, storing zoeken en praktijkcase.

### Onderwerpen
- Zie examemateriaal week 7

### Belangrijkste veiligheidsprincipe (Track 1)

> ⚠️ Een cobot is nooit automatisch veilig op zichzelf; een risicobeoordeling dekt altijd de combinatie van arm, gereedschap, werkstuk, proces en de nabijheid van mensen.

> ⚠️ Simuleer nieuwe programma's eerst en test daarna op lage snelheid met een hand aan de noodstop.

> 💡 Benoem je waypoints met vaste namen zoals Above_Pick, Pick, Place, Home.

## Praktijkopdracht (Document Type 2 / Template B) — Week 7: Certificeringsexamen (4 uur, 240 minuten)

**Niveau:** 3-4 · 240 min (lesdag) / 100-150 min (praktijkblokken)

Vandaag werk je aan: certificeringsexamen (4 uur, 240 minuten).
Verwacht resultaat: de kandidaat doorloopt het volledige certificeringsexamen: theorie, storing zoeken en praktijkcase.

> **Verplichte voorbereiding:** Maak vóór het starten een kort werkplan: benoem je bewegingsspoor (waypoints), bewegingsopdrachten en veiligheidsmaatregelen.

### Praktijkcase 1: Machine Tending

In-/uitladen van gesimuleerde CNC-machine of pers.

**Verplichte kernelementen:** I/O-handshaking (inkomende klaar- en uitgaande startsignaal), veilig in-/uitrijden via MoveL, terug naar Home.

### Opdrachten (progressieve oefenbank)
1. C7.1 Examenvoorbereiding: samenvatting theoriedomeinen
2. C7.2 Droogoefening Find the Error met de vier foutklassen

> Zie Informatieblad: Veilig opstarten en afsluiten. Zie Informatieblad: Handmatig verplaatsen (joggen en Hand guiding).

### Checkpoints


|  | Behaald | Deels | Niet behaald |
|---|---|---|---|
| Werkruimte gecontroleerd en noodstop getest vóór Servo On | ☐ | ☐ | ☐ |
| Waypoints herkenbaar benoemd (Home, Pick, Place) | ☐ | ☐ | ☐ |
| Programma eerst gesimuleerd / op lage snelheid getest | ☐ | ☐ | ☐ |
| Bewegingsvalidaties correct (MoveL zonder blending op pickpunt) | ☐ | ☐ | ☐ |
| Veilig afgesloten volgens procedure | ☐ | ☐ | ☐ |

## Beoordelingslijst (Template D) — Week 7 — beoordeling

> **Alle veiligheids-knock-outcriteria moeten zonder uitzondering worden gehaald: werkruimte gecontroleerd; noodstop geverifieerd vóór motorpower; geen onbevoegde wijziging van veiligheidsinstellingen; veilige afsluiting volgens procedure.**

| Competentie | 1 | 2 — NLQF 3 | 3 — NLQF 4 |
|---|---|---|---|
| Systeemopbouw & kalibratie | Herhaalde begeleiding nodig; grijper, TCP, payload of bedrading slordig/fout. | Monteert grijper, bedraadt basis-I/O en kalibreert TCP en payload zelfstandig en nauwkeurig. | Optimaliseert werkplekindeling en zwaartepuntinstelling voor ergonomie, bereik en cyclus. |
| Programmeren & proceslogica | Programma instabiel; lussen, frames of I/O bevatten fouten. | Combineert MoveJ/MoveL, lussen en werkende I/O tot een stabiele, veilige cyclus. | Modulair met nette subroutines, duidelijke naamgeving, bewuste blending en actieve foutafhandeling. |
| Storingzoeken & diagnostiek | Raadgedrag; verwijdert programmadelen zonder analyse. | Vindt en verhelpt de storing binnen de tijd met handleiding en gestructureerde controles. | Analyseert ruwe data (I/O-monitor, foutenlog, metingen), isoleert de oorzaak gericht en benoemt preventie. |
| Veiligheid, documentatie & vakmanschap | Rommig werken; kan keuzes niet uitleggen; geen bruikbare overdracht. | Werkt gedisciplineerd en veilig, gebruikt nette map- en taaknamen, legt werking helder uit. | Levert een complete, overdracht-klare cel met nette inline documentatie en onderbouwing richting klant. |

## Toets-/Examenblad (Document Type 3 / Template C) — Certificeringsexamen — week 7

**Totale duur:** 240 min

### Onderdeel 1: Theory examination (30 min)

- robots vs cobots en systeemcomponenten
- veilig op- en afsluiten, ISO 10218-1/2:2025, vier samenwerkingsvormen, noodstop vs Protective Stop, risicoanalyse
- kinematica en coördinaten (J1-J6, X/Y/Z, TCP, payload, Base/Tool/User frame)
- bewegingssturing en handbediening (joggen, handguiding, MoveJ/MoveL/MoveC, blending, singulariteit)
- programmalogica en structuur (Wait, Repeat, If/Else, subroutines, variabelen, netjes programmabeheer)
- connectiviteit en diagnostiek (24V DC digitaal/analoog I/O, sensoren, handshaking, stops systematisch oplossen)

**Extra voor NLQF 4:** coördinaattransformaties, foutafhandelingslogica, digitale simulatie, industriele communicatieprotocollen

### Onderdeel 2: Find the Error / Troubleshooting (20-30)

**Foutklassen (1) hardware- en I/O-fouten, (2) kalibratie- en instelfouten, (3) bewegings- en veiligheidsfouten, (4) logische programmafouten**

**Beoordeling:** Level 3: methodisch met handleiding en standaardcontroles. Level 4: directe ruwe diagnosegegevens, root cause zonder code verwijderen, fix valideren.

### Onderdeel 3: Practical case examination (180 min)

**Case 1 — Machine Tending:** In-/uitladen van gesimuleerde CNC-machine of pers.

*Verplichte kernelementen:* I/O-handshaking (inkomende klaar- en uitgaande startsignaal), veilig in-/uitrijden via MoveL, terug naar Home.

**Caseschil (voor elk uitgegeven examenblad):**
- industrieel brief met concrete productspecificaties
- beschikbare hardware en randvoorwaarden
- verplichte voorbereidingscheck (werkplan en veiligheidsanalyse)
- functionele einddemonstratie van een doorlopende productiecyclus
- mondelinge toelichting op veiligheids- en programmakeuzes

### Knock-outcriteria (direct onvoldoend)
- Werkruimte niet zichtbaar gecontroleerd en vrijgemaakt voor gebruik
- Noodstop niet geverifieerd vóór het inschakelen van de motorkracht
- Veiligheidsinstellingen zonder authorisatie omzeild of gewijzigd
- Niet volgens procedure veilig afgesloten

### Slagingsregels
- **NLQF 3:** Minimaal score 2 op élke competentie.
- **NLQF 4:** Score 3 op minimaal drie van de vier competenties (verplicht incl. Programming & Process Logic en Troubleshooting & Diagnostics), en nergens onder score 2.

**Examenkoppeling:** Volledig examenblueprint inclusief knock-outcriteria en rubric (Track 2, sectie 2.4).

---

*Samengesteld met de Cobot Course Composer op basis van de drie tracks (techniek · NLQF-pedagogiek · SMEOT-huisstijl). Ontbrekende machinegegevens verschijnen altijd als [REVIEW_MARKER] en nooit als verzonnen feiten.*
