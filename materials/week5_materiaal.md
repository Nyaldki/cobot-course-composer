# Week 5: Ruimtelijk inzicht en coördinaatframes

**Cobot Course — zeven weken, één lesdag per week (240 minuten):**   
**Niveau:** NLQF 4  
**Machine (Track 1):** Doosan Robotics M1013 — SMEOT Hengelo  

> **Leerdoel:** De student past Tool frame en User frame toe op mechanische uitdagingen.

## Lesprogramma (240 min)

| Duur | Blok |
|---|---|
| 15 min | Welkom en veiligheidscheck |
| 45 min | Directe instructie (Template A) |
| 25 min | Gecoachte praktijk (Template B, deel 1) |
| 10 min | Pauze |
| 100 min | Zelfstandige praktijk (Template B, deel 2) |
| 25 min | Reflectie en beoordeling (Template D) + afsluitprocedure |

## Informatieblad (Document Type 1 / Template A) — Week 5: Ruimtelijk inzicht en coördinaatframes

**Leerdoel:** De student past Tool frame en User frame toe op mechanische uitdagingen.

### Onderwerpen
- Rotaties Rx, Ry en Rz in de praktijk
- Tool frame bij werk langs een hoek
- User frame bij een schuin of scheef geplaatst blad
- Singulariteit managen achter een obstakel

### Belangrijkste veiligheidsprincipe (Track 1)

> ⚠️ Een cobot is nooit automatisch veilig op zichzelf; een risicobeoordeling dekt altijd de combinatie van arm, gereedschap, werkstuk, proces en de nabijheid van mensen.

> ⚠️ Simuleer nieuwe programma's eerst en test daarna op lage snelheid met een hand aan de noodstop.

> 💡 Benoem je waypoints met vaste namen zoals Above_Pick, Pick, Place, Home.

## Praktijkopdracht (Document Type 2 / Template B) — Week 5: Ruimtelijk inzicht en coördinaatframes

**Niveau:** NLQF 4 · 240 min (lesdag) / 100-150 min (praktijkblokken)

Vandaag werk je aan: ruimtelijk inzicht en coördinaatframes.
Verwacht resultaat: je past tool frame en user frame toe op mechanische uitdagingen.

> **Verplichte voorbereiding:** Maak vóór het starten een kort werkplan: benoem je bewegingsspoor (waypoints), bewegingsopdrachten en veiligheidsmaatregelen.

### Opdrachten (progressieve oefenbank)
1. C5.1 Flesdop losdraaien (rotatie via J6/Rz)
2. C5.2 Water van het ene glas in het andere schenken (kantelen via Rx/Ry)
3. C5.3 Pennetje in een schuin gat steken (Tool frame)
4. C5.4 Werken op een scheef geplaatst blad (User frame)
5. C5.5 Achter een obstakel reiken met singulariteitsmanagement

> Zie Informatieblad: Veilig opstarten en afsluiten. Zie Informatieblad: Handmatig verplaatsen (joggen en Hand guiding).

### Checkpoints


|  | Behaald | Deels | Niet behaald |
|---|---|---|---|
| Werkruimte gecontroleerd en noodstop getest vóór Servo On | ☐ | ☐ | ☐ |
| Waypoints herkenbaar benoemd (Home, Pick, Place) | ☐ | ☐ | ☐ |
| Programma eerst gesimuleerd / op lage snelheid getest | ☐ | ☐ | ☐ |
| Bewegingsvalidaties correct (MoveL zonder blending op pickpunt) | ☐ | ☐ | ☐ |
| Veilig afgesloten volgens procedure | ☐ | ☐ | ☐ |

## Beoordelingslijst (Template D) — Week 5 — beoordeling

> **Alle veiligheids-knock-outcriteria moeten zonder uitzondering worden gehaald: werkruimte gecontroleerd; noodstop geverifieerd vóór motorpower; geen onbevoegde wijziging van veiligheidsinstellingen; veilige afsluiting volgens procedure.**

| Competentie | 1 | 2 — NLQF 3 | 3 — NLQF 4 |
|---|---|---|---|
| Systeemopbouw & kalibratie | Herhaalde begeleiding nodig; grijper, TCP, payload of bedrading slordig/fout. | Monteert grijper, bedraadt basis-I/O en kalibreert TCP en payload zelfstandig en nauwkeurig. | Optimaliseert werkplekindeling en zwaartepuntinstelling voor ergonomie, bereik en cyclus. |
| Programmeren & proceslogica | Programma instabiel; lussen, frames of I/O bevatten fouten. | Combineert MoveJ/MoveL, lussen en werkende I/O tot een stabiele, veilige cyclus. | Modulair met nette subroutines, duidelijke naamgeving, bewuste blending en actieve foutafhandeling. |
| Storingzoeken & diagnostiek | Raadgedrag; verwijdert programmadelen zonder analyse. | Vindt en verhelpt de storing binnen de tijd met handleiding en gestructureerde controles. | Analyseert ruwe data (I/O-monitor, foutenlog, metingen), isoleert de oorzaak gericht en benoemt preventie. |
| Veiligheid, documentatie & vakmanschap | Rommig werken; kan keuzes niet uitleggen; geen bruikbare overdracht. | Werkt gedisciplineerd en veilig, gebruikt nette map- en taaknamen, legt werking helder uit. | Levert een complete, overdracht-klare cel met nette inline documentatie en onderbouwing richting klant. |

**Examenkoppeling:** Praktijkcase 5 (precisie-assemblage) en 6 (schuin vlak); theorie L4: coördinaattransformaties.

---

*Samengesteld met de Cobot Course Composer op basis van de drie tracks (techniek · NLQF-pedagogiek · SMEOT-huisstijl). Ontbrekende machinegegevens verschijnen altijd als [REVIEW_MARKER] en nooit als verzonnen feiten.*
