"""Compose learning materials for one week from the three tracks.

Hierarchy (fixed, non-negotiable):
1. Track 1 is the hard technical/safety foundation; no pedagogical or stylistic
   choice may weaken it or invent parameters.
2. Track 2 governs level, instructional structure (Templates A-D), NLQF alignment.
3. Track 3 governs presentation: language (Dutch), layout roles, asset boundaries.
"""

from __future__ import annotations

from app.loader import REVIEW_MARKER, Semester, brand_term, load_machine


def format_minutes(value) -> str:
    if isinstance(value, str):  # ranges like "20-30"
        return f"{value} min"
    return f"{value} min"


def lesson_program(sem: Semester, week_number: int, machine_id: str | None = None) -> dict:
    weeks = {w["number"]: w for w in sem.curriculum["weeks"]}
    if week_number not in weeks:
        raise ValueError(f"Week {week_number} bestaat niet; kies 1 t/m {len(weeks)}.")
    week = weeks[week_number]
    machine = load_machine(machine_id) if machine_id else sem.machines and load_machine(
        next(m["id"] for m in sem.machines if m["active"])
    )

    blocks = []
    if week.get("phase") == "exam":
        blocks = [{"minutes": format_minutes(c["minutes"]), "label": c["name"]} for c in week["exam"]["components"]]
    else:
        blocks = [
            {"minutes": format_minutes(b["minutes"]), "label": b["label"]}
            for b in sem.curriculum["defaults"]["timeblocks"]
        ]

    return {
        "week": week,
        "machine": {"model": machine["robot"]["model"], "id": machine["meta"]["id"], "institution": machine["meta"]["institution_context"]},
        "phases": {
            "technical_basis": sem.track1_core["safety"]["principle"],
            "pedagogy": sem.track2["meta"]["scope"] if "scope" in sem.track2["meta"] else sem.track2["scope"]["foundation"],
            "presentation": sem.track3["language_rules"]["target"],
        },
        "blokkenschema": blocks,
        "totaal_minuten": sem.curriculum["defaults"]["day_minutes"],
    }


def info_sheet(sem: Semester, week_number: int) -> dict:
    """Template A — Informatieblad (Document Type 1)."""
    weeks = {w["number"]: w for w in sem.curriculum["weeks"]}
    week = weeks[week_number]
    style = sem.track3
    return {
        "doctype": "Informatieblad (Document Type 1 / Template A)",
        "titel": f"Week {week_number}: {week['theme']}",
        "leerdoel": week["learning_objective"],
        "onderwerpen": week.get("topics", ["Theorieherhaling en examen voorbereiding (zie examemateriaal)"]),
        "veiligheidskader": sem.track1_core["safety"]["principle"],
        "waarschuwing": "Simuleer nieuwe programma's eerst en test daarna op lage snelheid met een hand aan de noodstop.",
        "tip": "Benoem je waypoints met vaste namen zoals Above_Pick, Pick, Place, Home.",
        "toc_referenties": week.get("info_sheets_referenties", sem.curriculum["defaults"]["info_sheets"]) if week_number == 1 else [f"Zie Informatieblad: week {week_number} onderwerpen"],
        "hop-instructie": style["document_types"]["informatieblad"]["doc_type"],
    }


def practical_assignment(sem: Semester, week_number: int, machine_id: str | None = None, case_profile: int | None = None) -> dict:
    """Template B — Praktijkopdracht (Document Type 2), optionally based on an exam case."""
    weeks = {w["number"]: w for w in sem.curriculum["weeks"]}
    week = weeks[week_number]
    machine = load_machine(machine_id) if machine_id else load_machine(
        next(m["id"] for m in sem.machines if m["active"])
    )

    brief = None
    if case_profile:
        profiles = [p for c in sem.track2["exam_blueprint"]["components"] if "case_profiles" in c for p in c["case_profiles"]]
        match = next((p for p in profiles if p["nr"] == case_profile), None)
        if match:
            brief = {
                "titel": f"Praktijkcase {match['nr']}: {match['name']}",
                "context": match["context"],
                "verplichte_elementen": match["elements"],
                "snelheidsterm": brand_term(machine, "move_joint"),
            }

    return {
        "doctype": "Praktijkopdracht (Document Type 2 / Template B)",
        "titel": f"Week {week_number}: {week['theme']}",
        "duur_geschat": f"{sem.curriculum['defaults']['day_minutes']} min (lesdag) / 100-150 min (praktijkblokken)",
        "leerdoel": week["learning_objective"],
        "niveau": week["level"] if isinstance(week["level"], str) else f"NLQF {week['level']}",
        "materiaal": {
            "machine": machine["robot"]["model"],
            "grijper": machine.get("workshop_config", {}).get("gripper", REVIEW_MARKER.format(detail="Grijptype ontbreekt")),
            "drukknoppen": machine.get("workshop_config", {}).get("push_buttons", "N.v.t."),
        },
        "introductie":[
            f"Vandaag werk je aan: {week['theme'].lower()}.",
            f"Verwacht resultaat: {week['learning_objective'].lower().replace('de student ', 'je ', 1)}",
        ],
        "opdrachten": week["assignments"],
        "voorbereiding_verplicht": "Maak vóór het starten een kort werkplan: benoem je bewegingsspoor (waypoints), bewegingsopdrachten en veiligheidsmaatregelen.",
        "case_brief": brief,
        "kruisverwijzingen": "Zie Informatieblad: Veilig opstarten en afsluiten. Zie Informatieblad: Handmatig verplaatsen (joggen en Hand guiding).",
        "checkpointcriteria": [
            "Werkruimte gecontroleerd en noodstop getest vóór Servo On",
            "Waypoints herkenbaar benoemd (Home, Pick, Place)",
            "Programma eerst gesimuleerd / op lage snelheid getest",
            "Bewegingsvalidaties correct (MoveL zonder blending op pickpunt)",
            "Veilig afgesloten volgens procedure",
        ],
    }


def assessment_sheet(sem: Semester, week_number: int) -> dict:
    """Template D — Shop-floor rubric (sign-off sheet)."""
    rubric = sem.track2["rubric"]
    return {
        "doctype": "Beoordelingslijst (Template D)",
        "titel": f"Week {week_number} — beoordeling",
        "knockoutcriteria": "Alle veiligheids-knock-outcriteria moeten zonder uitzondering worden gehaald: werkruimte gecontroleerd; noodstop geverifieerd vóór motorpower; geen onbevoegde wijziging van veiligheidsinstellingen; veilige afsluiting volgens procedure.",
        "matrix": [
            {"competentie": r["competency"], "1_onvoldoende": r["1"], "2_voldoende_nlqf3": r["2"], "3_uitstekend_nlqf4": r["3"]}
            for r in rubric
        ],
    }


def exam_materials(sem: Semester, week_number: int = 7, case_profile: int | None = None) -> dict:
    """Document Type 3 — Exam sheet assembly from the Track 2 blueprint."""
    weeks = {w["number"]: w for w in sem.curriculum["weeks"]}
    week = weeks.get(week_number)
    if not week or week.get("phase") != "exam":
        raise ValueError("Examemateriaal is alleen beschikbaar voor week 7 (examenweek).")
    blueprint = sem.track2["exam_blueprint"]
    components = blueprint["components"]
    theory = next(c for c in components if c["id"] == "theory")
    find_error = next(c for c in components if c["id"] == "find_error")
    practical = next(c for c in components if c["id"] == "practical")

    profile = None
    if case_profile:
        profile = next((p for p in practical["case_profiles"] if p["nr"] == case_profile), None)

    return {
        "doctype": "Toets-/Examenblad (Document Type 3 / Template C)",
        "titel": f"Certificeringsexamen — week {week_number}",
        "totale_duur": f"{blueprint['total_minutes']} min",
        "knockoutcriteria": blueprint["knockout_criteria"],
        "slagingsregels": blueprint["pass_rules"],
        "onderdeel_theorie": {"naam": theory["name"], "duur": theory["minutes"], "domeinen": theory["domains"], "niveau4": theory["level4_extra"]},
        "onderdeel_find_error": {"naam": find_error["name"], "duur": find_error["minutes"], "foutklassen": find_error["fault_classes"], "beoordeling": find_error["grading"]},
        "onderdeel_praktijk": {"naam": practical["name"], "duur": practical["minutes"], "caseschil": practical["shell"], "case": profile},
    }


def generate_week(sem: Semester, week_number: int, level: str | None = None, machine_id: str | None = None, case_profile: int | None = None) -> dict:
    materials = {
        "week_programma": lesson_program(sem, week_number, machine_id=machine_id),
        "informatieblad": info_sheet(sem, week_number),
        "praktijkopdracht": practical_assignment(sem, week_number, machine_id=machine_id, case_profile=case_profile),
        "beoordelingslijst": assessment_sheet(sem, week_number),
    }
    weeks = {w["number"]: w for w in sem.curriculum["weeks"]}
    if weeks[week_number].get("phase") == "exam":
        materials["examemateriaal"] = exam_materials(sem, week_number, case_profile=case_profile)
    if level:
        materials["niveau"] = level
    return materials
