# Week 2: Bewegingsprincipes en bewegingsopdrachten

**Cobot Course — zeven weken, één lesdag per week (240 minuten):**   
**Niveau:** NLQF 3  
**Machine (Track 1):** Doosan Robotics M1013 — SMEOT Hengelo  

> **Leerdoel:** De student past MoveJ, MoveL en MoveC gericht toe en herkent het effect van blending en singulariteit.

## Lesprogramma (240 min)

| Duur | Blok |
|---|---|
| 15 min | Welkom en veiligheidscheck |
| 45 min | Directe instructie (Template A) |
| 25 min | Gecoachte praktijk (Template B, deel 1) |
| 10 min | Pauze |
| 100 min | Zelfstandige praktijk (Template B, deel 2) |
| 25 min | Reflectie en beoordeling (Template D) + afsluitprocedure |

## Informatieblad (Document Type 1 / Template A) — Week 2: Bewegingsprincipes en bewegingsopdrachten

**Leerdoel:** De student past MoveJ, MoveL en MoveC gericht toe en herkent het effect van blending en singulariteit.

### Onderwerpen
- MoveJ vs. MoveL vs. MoveC (Move Joint, Move Line, Move Circle)
- Snelheid, versnelling en Blending
- Singulariteit bij lineaire bewegingen
- Wisselen tussen MoveJ en MoveL op het juiste moment

### Belangrijkste veiligheidsprincipe (Track 1)

> ⚠️ Een cobot is nooit automatisch veilig op zichzelf; een risicobeoordeling dekt altijd de combinatie van arm, gereedschap, werkstuk, proces en de nabijheid van mensen.

> ⚠️ Simuleer nieuwe programma's eerst en test daarna op lage snelheid met een hand aan de noodstop.

> 💡 Benoem je waypoints met vaste namen zoals Above_Pick, Pick, Place, Home.

## Praktijkopdracht (Document Type 2 / Template B) — Week 2: Bewegingsprincipes en bewegingsopdrachten

**Niveau:** NLQF 3 · 240 min (lesdag) / 100-150 min (praktijkblokken)

Vandaag werk je aan: bewegingsprincipes en bewegingsopdrachten.
Verwacht resultaat: je past movej, movel en movec gericht toe en herkent het effect van blending en singulariteit.

> **Verplichte voorbereiding:** Maak vóór het starten een kort werkplan: benoem je bewegingsspoor (waypoints), bewegingsopdrachten en veiligheidsmaatregelen.

### Opdrachten (progressieve oefenbank)
1. C2.1 Een rechte lijn tekenen met MoveL
2. C2.2 Een vierkant als doorlopend bewegingssporen traceren
3. C2.3 Een cirkel tekenen met MoveC
4. C2.4 Snelle MoveJ-verplaatsingen combineren met nauwkeurige MoveL-aanritten
5. C2.5 Beweging gladstrijken met Blending

> Zie Informatieblad: Veilig opstarten en afsluiten. Zie Informatieblad: Handmatig verplaatsen (joggen en Hand guiding).

### Checkpoints


|  | Behaald | Deels | Niet behaald |
|---|---|---|---|
| Werkruimte gecontroleerd en noodstop getest vóór Servo On | ☐ | ☐ | ☐ |
| Waypoints herkenbaar benoemd (Home, Pick, Place) | ☐ | ☐ | ☐ |
| Programma eerst gesimuleerd / op lage snelheid getest | ☐ | ☐ | ☐ |
| Bewegingsvalidaties correct (MoveL zonder blending op pickpunt) | ☐ | ☐ | ☐ |
| Veilig afgesloten volgens procedure | ☐ | ☐ | ☐ |

## Beoordelingslijst (Template D) — Week 2 — beoordeling

> **Alle veiligheids-knock-outcriteria moeten zonder uitzondering worden gehaald: werkruimte gecontroleerd; noodstop geverifieerd vóór motorpower; geen onbevoegde wijziging van veiligheidsinstellingen; veilige afsluiting volgens procedure.**

| Competentie | 1 | 2 — NLQF 3 | 3 — NLQF 4 |
|---|---|---|---|
| Systeemopbouw & kalibratie | Herhaalde begeleiding nodig; grijper, TCP, payload of bedrading slordig/fout. | Monteert grijper, bedraadt basis-I/O en kalibreert TCP en payload zelfstandig en nauwkeurig. | Optimaliseert werkplekindeling en zwaartepuntinstelling voor ergonomie, bereik en cyclus. |
| Programmeren & proceslogica | Programma instabiel; lussen, frames of I/O bevatten fouten. | Combineert MoveJ/MoveL, lussen en werkende I/O tot een stabiele, veilige cyclus. | Modulair met nette subroutines, duidelijke naamgeving, bewuste blending en actieve foutafhandeling. |
| Storingzoeken & diagnostiek | Raadgedrag; verwijdert programmadelen zonder analyse. | Vindt en verhelpt de storing binnen de tijd met handleiding en gestructureerde controles. | Analyseert ruwe data (I/O-monitor, foutenlog, metingen), isoleert de oorzaak gericht en benoemt preventie. |
| Veiligheid, documentatie & vakmanschap | Rommig werken; kan keuzes niet uitleggen; geen bruikbare overdracht. | Werkt gedisciplineerd en veilig, gebruikt nette map- en taaknamen, legt werking helder uit. | Levert een complete, overdracht-klare cel met nette inline documentatie en onderbouwing richting klant. |

**Examenkoppeling:** Theorie: bewegingssturing en handbediening (MoveJ/MoveL/MoveC, blending, singulariteit).

---

*Samengesteld met de Cobot Course Composer op basis van de drie tracks (techniek · NLQF-pedagogiek · SMEOT-huisstijl). Ontbrekende machinegegevens verschijnen altijd als [REVIEW_MARKER] en nooit als verzonnen feiten.*
