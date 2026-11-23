# Cobot Course Composer

Webapplicatie die leermateriaal samenstelt voor een **zeven weken durend cobot-onderwijsprogramma** (1 lesdag per week, 4 uur per dag) op basis van drie strikt gescheiden, uitwisselbare tracks ("pillars") uit de Central Knowledge Base.

## De drie tracks

| Track | Bestand | Vervangbaar? | Inhoud |
|---|---|---|---|
| 1 — Universele cobot-kern | `knowledge/track1_core.yaml` | Nee (merk-onafhankelijk) | Mechanica, veiligheid (ISO 10218-1/2:2025, vier samenwerkingsvormen), kinematica, beweging, programmeren, I/O, troubleshooting |
| 1 — Machine-sub-module A | `knowledge/machines/doosan_m1013.yaml` | **Ja** (protocol 1.6) | Doosan M1013 + Dr. Dart, specs, op-/afstartprocedures, SMEOT-workshopconfig (RG2/RG6, 25 N, zone "Werkruimte") |
| 2 — Pedagogisch blauwdruk | `knowledge/track2_pedagogy.yaml` | Nee | NLQF 3/4-matrix, Templates A–D, examenblueprint met 7 caseprofielen en rubric |
| 3 — Visuele identiteit | `knowledge/track3_style_smeot.yaml` | **Ja** (protocol 3.6) | SMEOT style tokens, documenttypes, NL-taalregels, asset-regels |
| — Curriculum | `knowledge/curriculum.yaml` | Beheerbaar | 7 weken, fasen 1–5 van de oefenbank, tijdblokken per lesdag |

## Het zevenwekenprogramma

| Week | Thema | Fase oefenbank |
|---|---|---|
| 1 | Veiligheid, opbouw en handmatige bediening | 1 |
| 2 | Bewegingsprincipes (MoveJ/MoveL/MoveC, blending, singulariteit) | 2 |
| 3 | Grijpen en repetitieve productielogica | 3 |
| 4 | Rasters, crate-vulling en palletiseren | 3 |
| 5 | Ruimtelijk inzicht en coördinaatframes | 4 |
| 6 | I/O, integratie en troubleshooting | 5 |
| 7 | Certificeringsexamen (30 min theorie, 20–30 min storingzoeken, 180 min praktijkcase) | Examenblueprint |

## Vaste hiërarchie (afgedwongen door de code)

1. **Track 1 geeft de harde technische/veiligheidsgrens.** Track 2/3 kunnen feiten nooit verzachten of aanvullen.
2. **Een ontbrekende technische parameter wordt nooit uit algemene kennis aangevuld**, maar resulteert in een expliciete `[REVIEW_MARKER: ...]` voor de docent/technisch beheerder (zie `app/loader.py`).
3. Materiaal wordt in **Nederlands** gegenereerd met behoud van Engelse commandoterminologie, kruisverwijzingen in plaats van herhaling, en `[VERIFIED_ASSET: ...]`-placeholders in plaats van gefabriceerde schermafbeeldingen.

## Draaien

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000 — kies week, NLQF-niveau, machine-sub-module en praktijkcase, en stel het materiaal samen.

## API

- `GET /api/weeks` — volledige curriculumkaart
- `GET /api/weeks/{n}` — lesprogramma van week n (240 min)
- `GET /api/machines` — beschikbare machine-sub-modules
- `POST /api/generate?week=3&level=NLQF+4&case_profile=2` — volledig materiaalpakket als JSON

## Tests

```bash
python -m pytest tests/ -q
```
