# Week 3: Grijpen en repetitieve productielogica

**Programma:** Cobot Course — zeven weken, één lesdag per week (240 minuten)  
**Niveau:** NLQF 3  
**Machine (Track 1):** Doosan Robotics M1013 — SMEOT Hengelo  

> **Leerdoel:** De student bouwt een stabiele pick-and-place-cyclus met grijper en Repeat-lus.

## Lesprogramma (240 min)

| Duur | Blok |
|---|---|
| 15 min | Welkom en veiligheidscheck |
| 45 min | Directe instructie (Template A) |
| 25 min | Gecoachte praktijk (Template B, deel 1) |
| 10 min | Pauze |
| 100 min | Zelfstandige praktijk (Template B, deel 2) |
| 25 min | Reflectie en beoordeling (Template D) + afsluitprocedure |

## Informatieblad (Document Type 1 / Template A) — Week 3: Grijpen en repetitieve productielogica

**Leerdoel:** De student bouwt een stabiele pick-and-place-cyclus met grijper en Repeat-lus.

### Onderwerpen
- Standaard pick-and-place-traject (Home, Approach, Pick, Retreat, Place)
- Grijpers: tweedrievingers, vacuüm, magnetisch
- Repeat/lus met teller; anti-cyclisch ontwerpen
- TCP en payload correct kalibreren (Smart Setup)

### Belangrijkste veiligheidsprincipe (Track 1)

> ⚠️ Een cobot is nooit automatisch veilig op zichzelf; een risicobeoordeling dekt altijd de combinatie van arm, gereedschap, werkstuk, proces en de nabijheid van mensen.

> ⚠️ Simuleer nieuwe programma's eerst en test daarna op lage snelheid met een hand aan de noodstop.

> 💡 **Tip:** Benoem je waypoints met vaste namen zoals Above_Pick, Pick, Place, Home.

## Praktijkopdracht (Document Type 2 / Template B) — Week 3: Grijpen en repetitieve productielogica

**Niveau:** NLQF 3 · **Geschatte duur:** 240 min (lesdag) / 100-150 min (praktijkblokken)

**Materiaal:** Doosan Robotics M1013 met Electric OnRobot two-finger gripper (RG2/RG6 series); Three physical push buttons (red, blue, white) wired to the controller; freely assignable in student tasks.

Vandaag werk je aan: grijpen en repetitieve productielogica.
Verwacht resultaat: je bouwt een stabiele pick-and-place-cyclus met grijper en repeat-lus.

> **Verplichte voorbereiding:** Maak vóór het starten een kort werkplan: benoem je bewegingsspoor (waypoints), bewegingsopdrachten en veiligheidsmaatregelen.

### Opdrachten (progressieve oefenbank)
1. C3.1 Enkele pick-and-place
2. C3.2 Producten naar meerdere afzetpunten met aan- en terugrijpunten
3. C3.3 Repeat-lus voor tien cycli
4. C3.4 Vijf blokken stapelen via Z-offset

> Zie Informatieblad: Veilig opstarten en afsluiten. Zie Informatieblad: Handmatig verplaatsen (joggen en Hand guiding).

### Checkpoints

| Criterium | Behaald | Deels | Niet behaald |
|---|---|---|---|
| Werkruimte gecontroleerd en noodstop getest vóór Servo On | ☐ | ☐ | ☐ |
| Waypoints herkenbaar benoemd (Home, Pick, Place) | ☐ | ☐ | ☐ |
| Programma eerst gesimuleerd / op lage snelheid getest | ☐ | ☐ | ☐ |
| Bewegingsvalidaties correct (MoveL zonder blending op pickpunt) | ☐ | ☐ | ☐ |
| Veilig afgesloten volgens procedure | ☐ | ☐ | ☐ |

## Beoordelingslijst (Template D) — week 3

> **Knock-outcriteria:** Alle veiligheids-knock-outcriteria moeten zonder uitzondering worden gehaald: werkruimte gecontroleerd; noodstop geverifieerd vóór motorpower; geen onbevoegde wijziging van veiligheidsinstellingen; veilige afsluiting volgens procedure.

| Competentie | 1 — Onvoldoende | 2 — NLQF 3 | 3 — NLQF 4 |
|---|---|---|---|
| Systeemopbouw & kalibratie | Herhaalde begeleiding nodig; grijper, TCP, payload of bedrading slordig/fout. | Monteert grijper, bedraadt basis-I/O en kalibreert TCP en payload zelfstandig en nauwkeurig. | Optimaliseert werkplekindeling en zwaartepuntinstelling voor ergonomie, bereik en cyclus. |
| Programmeren & proceslogica | Programma instabiel; lussen, frames of I/O bevatten fouten. | Combineert MoveJ/MoveL, lussen en werkende I/O tot een stabiele, veilige cyclus. | Modulair met nette subroutines, duidelijke naamgeving, bewuste blending en actieve foutafhandeling. |
| Storingzoeken & diagnostiek | Raadgedrag; verwijdert programmadelen zonder analyse. | Vindt en verhelpt de storing binnen de tijd met handleiding en gestructureerde controles. | Analyseert ruwe data (I/O-monitor, foutenlog, metingen), isoleert de oorzaak gericht en benoemt preventie. |
| Veiligheid, documentatie & vakmanschap | Rommig werken; kan keuzes niet uitleggen; geen bruikbare overdracht. | Werkt gedisciplineerd en veilig, gebruikt nette map- en taaknamen, legt werking helder uit. | Levert een complete, overdracht-klare cel met nette inline documentatie en onderbouwing richting klant. |

**Examenkoppeling:** Theorie: kinematica en coördinaten (J1-J6, X/Y/Z, TCP, payload, Base/Tool/User frame).

---

*Samengesteld met de Cobot Course Composer op basis van de drie tracks (techniek · NLQF-pedagogiek · SMEOT-huisstijl). Ontbrekende machinegegevens verschijnen altijd als [REVIEW_MARKER] en nooit als verzonnen feiten.*
