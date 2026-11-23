# Week 6: I/O, integratie en troubleshooting

**Cobot Course — zeven weken, één lesdag per week (240 minuten):**   
**Niveau:** NLQF 4  
**Machine (Track 1):** Doosan Robotics M1013 — SMEOT Hengelo  

> **Leerdoel:** De student koppelt externe signalen, programma's modulair en lost een storing systematisch op.

## Lesprogramma (240 min)

| Duur | Blok |
|---|---|
| 15 min | Welkom en veiligheidscheck |
| 45 min | Directe instructie (Template A) |
| 25 min | Gecoachte praktijk (Template B, deel 1) |
| 10 min | Pauze |
| 100 min | Zelfstandige praktijk (Template B, deel 2) |
| 25 min | Reflectie en beoordeling (Template D) + afsluitprocedure |

## Informatieblad (Document Type 1 / Template A) — Week 6: I/O, integratie en troubleshooting

**Leerdoel:** De student koppelt externe signalen, programma's modulair en lost een storing systematisch op.

### Onderwerpen
- 24V DC I/O: ingangen, uitgangen, Flange I/O vs. Controller I/O
- Wait/If-Else met sensoren en drukknoppen
- Handshaking met een machine (machine tending)
- Systematisch storingzoeken op basis van I O-monitor en foutenlog
- DRL/Python: visueel programma naar tekstcode

### Belangrijkste veiligheidsprincipe (Track 1)

> ⚠️ Een cobot is nooit automatisch veilig op zichzelf; een risicobeoordeling dekt altijd de combinatie van arm, gereedschap, werkstuk, proces en de nabijheid van mensen.

> ⚠️ Simuleer nieuwe programma's eerst en test daarna op lage snelheid met een hand aan de noodstop.

> 💡 Benoem je waypoints met vaste namen zoals Above_Pick, Pick, Place, Home.

## Praktijkopdracht (Document Type 2 / Template B) — Week 6: I/O, integratie en troubleshooting

**Niveau:** NLQF 4 · 240 min (lesdag) / 100-150 min (praktijkblokken)

Vandaag werk je aan: i/o, integratie en troubleshooting.
Verwacht resultaat: je koppelt externe signalen, programma's modulair en lost een storing systematisch op.

> **Verplichte voorbereiding:** Maak vóór het starten een kort werkplan: benoem je bewegingsspoor (waypoints), bewegingsopdrachten en veiligheidsmaatregelen.

### Opdrachten (progressieve oefenbank)
1. C6.1 Taken starten en pauzeren via drukknoppen (Input + If)
2. C6.2 Een statuslamp schakelen (Output)
3. C6.3 Sensorgetriggerde wachttijd (Wait)
4. C6.4 Kleuren sorteren met sensor of camera (If/Else)
5. C6.5 Modulair programmeren met grijp- en loslaat-subroutines
6. C6.6 Rommelige code opruimen en herstructureren
7. C6.7 Zwaar werkstuk kalibreren (payload)
8. C6.8 Systematisch troubleshooten na een stop
9. C6.9 Snelheid verlagen via veiligheidszones
10. C6.10 Machine tending met handshaking
11. C6.11 Taak omzetten naar tekstcode (DRL/Python)

> Zie Informatieblad: Veilig opstarten en afsluiten. Zie Informatieblad: Handmatig verplaatsen (joggen en Hand guiding).

### Checkpoints


|  | Behaald | Deels | Niet behaald |
|---|---|---|---|
| Werkruimte gecontroleerd en noodstop getest vóór Servo On | ☐ | ☐ | ☐ |
| Waypoints herkenbaar benoemd (Home, Pick, Place) | ☐ | ☐ | ☐ |
| Programma eerst gesimuleerd / op lage snelheid getest | ☐ | ☐ | ☐ |
| Bewegingsvalidaties correct (MoveL zonder blending op pickpunt) | ☐ | ☐ | ☐ |
| Veilig afgesloten volgens procedure | ☐ | ☐ | ☐ |

## Beoordelingslijst (Template D) — Week 6 — beoordeling

> **Alle veiligheids-knock-outcriteria moeten zonder uitzondering worden gehaald: werkruimte gecontroleerd; noodstop geverifieerd vóór motorpower; geen onbevoegde wijziging van veiligheidsinstellingen; veilige afsluiting volgens procedure.**

| Competentie | 1 | 2 — NLQF 3 | 3 — NLQF 4 |
|---|---|---|---|
| Systeemopbouw & kalibratie | Herhaalde begeleiding nodig; grijper, TCP, payload of bedrading slordig/fout. | Monteert grijper, bedraadt basis-I/O en kalibreert TCP en payload zelfstandig en nauwkeurig. | Optimaliseert werkplekindeling en zwaartepuntinstelling voor ergonomie, bereik en cyclus. |
| Programmeren & proceslogica | Programma instabiel; lussen, frames of I/O bevatten fouten. | Combineert MoveJ/MoveL, lussen en werkende I/O tot een stabiele, veilige cyclus. | Modulair met nette subroutines, duidelijke naamgeving, bewuste blending en actieve foutafhandeling. |
| Storingzoeken & diagnostiek | Raadgedrag; verwijdert programmadelen zonder analyse. | Vindt en verhelpt de storing binnen de tijd met handleiding en gestructureerde controles. | Analyseert ruwe data (I/O-monitor, foutenlog, metingen), isoleert de oorzaak gericht en benoemt preventie. |
| Veiligheid, documentatie & vakmanschap | Rommig werken; kan keuzes niet uitleggen; geen bruikbare overdracht. | Werkt gedisciplineerd en veilig, gebruikt nette map- en taaknamen, legt werking helder uit. | Levert een complete, overdracht-klare cel met nette inline documentatie en onderbouwing richting klant. |

**Examenkoppeling:** Theorie L4: connectiviteit, protocollen, foutafhandeling; examinonderdeel 2 (Find the Error).

---

*Samengesteld met de Cobot Course Composer op basis van de drie tracks (techniek · NLQF-pedagogiek · SMEOT-huisstijl). Ontbrekende machinegegevens verschijnen altijd als [REVIEW_MARKER] en nooit als verzonnen feiten.*
