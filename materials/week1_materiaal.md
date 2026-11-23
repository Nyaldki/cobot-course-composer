# Week 1: Veiligheid, opbouw en handmatige bediening

**Cobot Course — zeven weken, één lesdag per week (240 minuten):**   
**Niveau:** NLQF 3  
**Machine (Track 1):** Doosan Robotics M1013 — SMEOT Hengelo  

> **Leerdoel:** De student zet de cobot veilig op en af en beweegt de arm handmatig naar een aangegeven positie.

## Lesprogramma (240 min)

| Duur | Blok |
|---|---|
| 15 min | Welkom en veiligheidscheck |
| 45 min | Directe instructie (Template A) |
| 25 min | Gecoachte praktijk (Template B, deel 1) |
| 10 min | Pauze |
| 100 min | Zelfstandige praktijk (Template B, deel 2) |
| 25 min | Reflectie en beoordeling (Template D) + afsluitprocedure |

## Informatieblad (Document Type 1 / Template A) — Week 1: Veiligheid, opbouw en handmatige bediening

**Leerdoel:** De student zet de cobot veilig op en af en beweegt de arm handmatig naar een aangegeven positie.

### Onderwerpen
- Robot vs. cobot; vijf vaste hoofdcomponenten
- Veiligheidsnormen (ISO 10218-1/2:2025) en de vier samenwerkingsvormen
- Noodstop vs. Protective Stop; vijf beschermingslagen
- Gewrichten J1 t/m J6 en X/Y/Z; joggen en Hand guiding

### Belangrijkste veiligheidsprincipe (Track 1)

> ⚠️ Een cobot is nooit automatisch veilig op zichzelf; een risicobeoordeling dekt altijd de combinatie van arm, gereedschap, werkstuk, proces en de nabijheid van mensen.

> ⚠️ Simuleer nieuwe programma's eerst en test daarna op lage snelheid met een hand aan de noodstop.

> 💡 Benoem je waypoints met vaste namen zoals Above_Pick, Pick, Place, Home.

## Praktijkopdracht (Document Type 2 / Template B) — Week 1: Veiligheid, opbouw en handmatige bediening

**Niveau:** NLQF 3 · 240 min (lesdag) / 100-150 min (praktijkblokken)

Vandaag werk je aan: veiligheid, opbouw en handmatige bediening.
Verwacht resultaat: je zet de cobot veilig op en af en beweegt de arm handmatig naar een aangegeven positie.

> **Verplichte voorbereiding:** Maak vóór het starten een kort werkplan: benoem je bewegingsspoor (waypoints), bewegingsopdrachten en veiligheidsmaatregelen.

### Opdrachten (progressieve oefenbank)
1. C1.1 Veilig in- en uitschakelen volgens vaste procedure
2. C1.2 Elk gewricht J1 t/m J6 afzonderlijk verkennen (Joint jogging)
3. C1.3 Cartesisch joggen langs X, Y en Z
4. C1.4 Hand guiding: de arm naar een markering op tafel bewegen
5. C1.5 Losse waypoints opslaan met een pointerpen

> Zie Informatieblad: Veilig opstarten en afsluiten. Zie Informatieblad: Handmatig verplaatsen (joggen en Hand guiding).

### Checkpoints


|  | Behaald | Deels | Niet behaald |
|---|---|---|---|
| Werkruimte gecontroleerd en noodstop getest vóór Servo On | ☐ | ☐ | ☐ |
| Waypoints herkenbaar benoemd (Home, Pick, Place) | ☐ | ☐ | ☐ |
| Programma eerst gesimuleerd / op lage snelheid getest | ☐ | ☐ | ☐ |
| Bewegingsvalidaties correct (MoveL zonder blending op pickpunt) | ☐ | ☐ | ☐ |
| Veilig afgesloten volgens procedure | ☐ | ☐ | ☐ |

## Beoordelingslijst (Template D) — Week 1 — beoordeling

> **Alle veiligheids-knock-outcriteria moeten zonder uitzondering worden gehaald: werkruimte gecontroleerd; noodstop geverifieerd vóór motorpower; geen onbevoegde wijziging van veiligheidsinstellingen; veilige afsluiting volgens procedure.**

| Competentie | 1 | 2 — NLQF 3 | 3 — NLQF 4 |
|---|---|---|---|
| Systeemopbouw & kalibratie | Herhaalde begeleiding nodig; grijper, TCP, payload of bedrading slordig/fout. | Monteert grijper, bedraadt basis-I/O en kalibreert TCP en payload zelfstandig en nauwkeurig. | Optimaliseert werkplekindeling en zwaartepuntinstelling voor ergonomie, bereik en cyclus. |
| Programmeren & proceslogica | Programma instabiel; lussen, frames of I/O bevatten fouten. | Combineert MoveJ/MoveL, lussen en werkende I/O tot een stabiele, veilige cyclus. | Modulair met nette subroutines, duidelijke naamgeving, bewuste blending en actieve foutafhandeling. |
| Storingzoeken & diagnostiek | Raadgedrag; verwijdert programmadelen zonder analyse. | Vindt en verhelpt de storing binnen de tijd met handleiding en gestructureerde controles. | Analyseert ruwe data (I/O-monitor, foutenlog, metingen), isoleert de oorzaak gericht en benoemt preventie. |
| Veiligheid, documentatie & vakmanschap | Rommig werken; kan keuzes niet uitleggen; geen bruikbare overdracht. | Werkt gedisciplineerd en veilig, gebruikt nette map- en taaknamen, legt werking helder uit. | Levert een complete, overdracht-klare cel met nette inline documentatie en onderbouwing richting klant. |

**Examenkoppeling:** Theorie: systeemcomponenten, veilig op- en afsluiten, samenwerkingsvormen, risicoanalyse.

---

*Samengesteld met de Cobot Course Composer op basis van de drie tracks (techniek · NLQF-pedagogiek · SMEOT-huisstijl). Ontbrekende machinegegevens verschijnen altijd als [REVIEW_MARKER] en nooit als verzonnen feiten.*
