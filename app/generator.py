"""Compose learning materials for one week from the three tracks.

Hierarchy (fixed, non-negotiable):
1. Track 1 is the hard technical/safety foundation; no pedagogical or stylistic
   choice may weaken it or invent parameters.
2. Track 2 governs level, instructional structure (Templates A-D), NLQF alignment.
3. Track 3 governs presentation: language (Dutch or English), layout roles, asset boundaries.

Bilingual support: language="nl" (default, per Track 3 language rules) or
language="en". English rendering uses knowledge/translations_en.yaml; the
technical facts always come from Track 1 (never translated ad hoc).
"""

from __future__ import annotations

from app.loader import REVIEW_MARKER, Semester, brand_term, load_machine, load_translations


def _translations(sem: Semester, lang: str) -> dict | None:
    if lang == "en":
        return sem.translations_en
    return None


def _week(sem: Semester, week_number: int) -> dict:
    weeks = {w["number"]: w for w in sem.curriculum["weeks"]}
    if week_number not in weeks:
        raise ValueError(f"Week {week_number} bestaat niet; kies 1 t/m {len(weeks)}.")
    return weeks[week_number]


def _active_machine_id(sem: Semester, machine_id: str | None) -> str:
    if machine_id:
        return machine_id
    return next(m["id"] for m in sem.machines if m["active"])


def format_minutes(value) -> str:
    if isinstance(value, str):
        return f"{value} min"
    return f"{value} min"


def lesson_program(sem: Semester, week_number: int, machine_id: str | None = None, lang: str = "nl") -> dict:
    week = _week(sem, week_number)
    tr = _translations(sem, lang)
    machine = load_machine(_active_machine_id(sem, machine_id))

    if week.get("phase") == "exam":
        blocks = [{"minutes": format_minutes(c["minutes"]), "label": c["name"]} for c in week["exam"]["components"]]
    else:
        source = tr["timeblocks"] if tr else [b["label"] for b in sem.curriculum["defaults"]["timeblocks"]]
        defaults = [b["minutes"] for b in sem.curriculum["defaults"]["timeblocks"]]
        blocks = [{"minutes": format_minutes(m), "label": label} for m, label in zip(defaults, source)]
        if week_number == 1 and tr is None:
            blocks = blocks  # keep default nl labels

    theme = week["theme"]
    objective = week["learning_objective"]
    if tr and week_number in tr["weeks"]:
        theme = tr["weeks"][week_number]["theme"]
        objective = tr["weeks"][week_number]["objective"]

    return {
        "week": week,
        "theme": theme,
        "objective": objective,
        "machine": {"model": machine["robot"]["model"], "id": machine["meta"]["id"], "institution": machine["meta"]["institution_context"]},
        "phases": {
            "technical_basis": sem.track1_core["safety"].get("principle_nl" if lang == "nl" else "principle"),
            "pedagogy": sem.track2["scope"]["foundation"],
            "presentation": sem.track3["language_rules"]["target"],
        },
        "blokkenschema": blocks,
        "totaal_minuten": sem.curriculum["defaults"]["day_minutes"],
    }


def info_sheet(sem: Semester, week_number: int, lang: str = "nl") -> dict:
    """Template A — Informatieblad (Document Type 1)."""
    week = _week(sem, week_number)
    tr = _translations(sem, lang)
    topics = week.get("topics", [])
    if tr:
        topics = tr["weeks"][week_number]["topics"] if topics else [tr["doctypes"]["intro_note"]]
    else:
        topics = topics or [f"Zie examemateriaal week {week_number}"]
    title_theme = tr["weeks"][week_number]["theme"] if tr else week["theme"]

    return {
        "doctype": tr["doctypes"]["info_sheet"] if tr else "Informatieblad (Document Type 1 / Template A)",
        "titel": f"Week {week_number}: {title_theme}",
        "leerdoel": tr["weeks"][week_number]["objective"] if tr else week["learning_objective"],
        "onderwerpen": topics,
        "veiligheidskader": sem.track1_core["safety"].get("principle_nl" if lang == "nl" else "principle"),
        "waarschuwing": tr["labels"]["warning"] if tr else "Simuleer nieuwe programma's eerst en test daarna op lage snelheid met een hand aan de noodstop.",
        "tip": tr["labels"]["tip_text"] if tr else "Benoem je waypoints met vaste namen zoals Above_Pick, Pick, Place, Home.",
        "kruisverwijzingen": tr["labels"]["cross_references"] if tr else "Zie Informatieblad: Veilig opstarten en afsluiten. Zie Informatieblad: Handmatig verplaatsen (joggen en Hand guiding).",
    }


def practical_assignment(sem: Semester, week_number: int, machine_id: str | None = None, case_profile: int | None = None, lang: str = "nl") -> dict:
    """Template B — Praktijkopdracht (Document Type 2), optionally based on an exam case."""
    week = _week(sem, week_number)
    tr = _translations(sem, lang)
    machine = load_machine(_active_machine_id(sem, machine_id))
    tw = tr["weeks"][week_number] if tr else None

    assignments = tw["assignments"] if tr else week["assignments"]
    objective = tw["objective"] if tr else week["learning_objective"]

    brief = None
    if case_profile:
        profiles = [p for c in sem.track2["exam_blueprint"]["components"] if "case_profiles" in c for p in c["case_profiles"]]
        match = next((p for p in profiles if p["nr"] == case_profile), None)
        if match:
            brief = {
                "titel": f"{'Practical case' if tr else 'Praktijkcase'} {match['nr']}: {match['name']}",
                "context": tr["exam"]["case_context"][case_profile] if tr else match["context"],
                "verplichte_elementen": tr["exam"]["case_elements"][case_profile] if tr else match["elements"],
            }

    checkpoints = tr["checkpoint_criteria"] if tr else [
        "Werkruimte gecontroleerd en noodstop getest vóór Servo On",
        "Waypoints herkenbaar benoemd (Home, Pick, Place)",
        "Programma eerst gesimuleerd / op lage snelheid getest",
        "Bewegingsvalidaties correct (MoveL zonder blending op pickpunt)",
        "Veilig afgesloten volgens procedure",
    ]

    return {
        "doctype": tr["doctypes"]["practical"] if tr else "Praktijkopdracht (Document Type 2 / Template B)",
        "titel": f"Week {week_number}: {tw['theme'] if tr else week['theme']}",
        "duur_geschat": tr["labels"]["estimated_duration"] if tr else "240 min (lesdag) / 100-150 min (praktijkblokken)",
        "leerdoel": objective,
        "niveau": week["level"] if isinstance(week["level"], str) else f"NLQF {week['level']}",
        "materiaal": {
            "machine": machine["robot"]["model"],
            "grijper": machine.get("workshop_config", {}).get("gripper", REVIEW_MARKER.format(detail="Grijptype ontbreekt")),
            "drukknoppen": machine.get("workshop_config", {}).get("push_buttons", "N.v.t."),
        },
        "introductie": [
            f"{'Today you will work on:' if tr else 'Vandaag werk je aan:'} {(tw['theme'] if tr else week['theme']).lower()}.",
            f"{'Expected result:' if tr else 'Verwacht resultaat:'} {objective.lower().replace('de student ', 'je ', 1).replace('the student ', 'you ', 1)}",
        ],
        "opdrachten": assignments,
        "voorbereiding_verplicht": tr["labels"]["mandatory_preparation"] if tr else "Maak vóór het starten een kort werkplan: benoem je bewegingsspoor (waypoints), bewegingsopdrachten en veiligheidsmaatregelen.",
        "case_brief": brief,
        "kruisverwijzingen": tr["labels"]["cross_references"] if tr else "Zie Informatieblad: Veilig opstarten en afsluiten. Zie Informatieblad: Handmatig verplaatsen (joggen en Hand guiding).",
        "checkpointcriteria": checkpoints,
    }


def assessment_sheet(sem: Semester, week_number: int, lang: str = "nl") -> dict:
    """Template D — Shop-floor rubric (sign-off sheet)."""
    tr = _translations(sem, lang)
    rubric = sem.track2["rubric"]
    cells = tr["rubric_cells"] if tr else None
    competencies = tr["rubric"]["competencies"] if tr else None

    matrix = []
    for i, r in enumerate(rubric):
        comp = competencies[i] if competencies else r["competency"]
        if cells:
            key = ["setup", "programming", "troubleshooting", "craft"][i]
            s1, s2, s3 = cells[key][1], cells[key][2], cells[key][3]
        else:
            s1, s2, s3 = r["1"], r["2"], r["3"]
        matrix.append({"competentie": comp, "1_onvoldoende": s1, "2_voldoende_nlqf3": s2, "3_uitstekend_nlqf4": s3})

    return {
        "doctype": tr["doctypes"]["assessment"] if tr else "Beoordelingslijst (Template D)",
        "titel": f"Week {week_number} — {'assessment' if tr else 'beoordeling'}",
        "knockoutcriteria": tr["labels"]["knockout"] if tr else "Alle veiligheids-knock-outcriteria moeten zonder uitzondering worden gehaald: werkruimte gecontroleerd; noodstop geverifieerd vóór motorpower; geen onbevoegde wijziging van veiligheidsinstellingen; veilige afsluiting volgens procedure.",
        "matrix": matrix,
    }


def exam_materials(sem: Semester, week_number: int = 7, case_profile: int | None = None, lang: str = "nl") -> dict:
    """Document Type 3 — Exam sheet assembly from the Track 2 blueprint."""
    week = _week(sem, week_number)
    if week.get("phase") != "exam":
        raise ValueError("Examemateriaal is alleen beschikbaar voor week 7 (examenweek).")
    tr = _translations(sem, lang)
    ex_tr = tr["exam"] if tr else None
    blueprint = sem.track2["exam_blueprint"]
    theory = next(c for c in blueprint["components"] if c["id"] == "theory")
    find_error = next(c for c in blueprint["components"] if c["id"] == "find_error")
    practical = next(c for c in blueprint["components"] if c["id"] == "practical")

    profile = None
    if case_profile:
        profile = next((p for p in practical["case_profiles"] if p["nr"] == case_profile), None)
    if profile and tr:
        profile = dict(profile)
        profile["context"] = ex_tr["case_context"][case_profile]
        profile["elements"] = ex_tr["case_elements"][case_profile]

    return {
        "doctype": tr["doctypes"]["exam"] if tr else "Toets-/Examenblad (Document Type 3 / Template C)",
        "titel": f"{'Certification exam' if tr else 'Certificeringsexamen'} — week {week_number}",
        "totale_duur": f"{blueprint['total_minutes']} min",
        "knockoutcriteria": ex_tr["knockout"] if tr else blueprint["knockout_criteria"],
        "slagingsregels": (
            {"level3": ex_tr["pass3"], "level4": ex_tr["pass4"]} if tr else blueprint["pass_rules"]
        ),
        "onderdeel_theorie": {
            "naam": theory["name"], "duur": theory["minutes"],
            "domeinen": ex_tr["theory"] if tr else theory["domains"],
            "niveau4": ex_tr["theory_level4"] if tr else theory["level4_extra"],
        },
        "onderdeel_find_error": {
            "naam": find_error["name"], "duur": find_error["minutes"],
            "foutklassen": find_error["fault_classes"],
            "beoordeling": ex_tr["find_error_grading"] if tr else find_error["grading"],
        },
        "onderdeel_praktijk": {
            "naam": practical["name"], "duur": practical["minutes"],
            "caseschil": ex_tr["shell"] if tr else practical["shell"],
            "case": profile,
        },
    }


def generate_week(
    sem: Semester,
    week_number: int,
    level: str | None = None,
    machine_id: str | None = None,
    case_profile: int | None = None,
    lang: str = "nl",
) -> dict:
    materials = {
        "week_programma": lesson_program(sem, week_number, machine_id=machine_id, lang=lang),
        "informatieblad": info_sheet(sem, week_number, lang=lang),
        "praktijkopdracht": practical_assignment(sem, week_number, machine_id=machine_id, case_profile=case_profile, lang=lang),
        "beoordelingslijst": assessment_sheet(sem, week_number, lang=lang),
    }
    if _week(sem, week_number).get("phase") == "exam":
        materials["examemateriaal"] = exam_materials(sem, week_number, case_profile=case_profile, lang=lang)
    if level:
        materials["niveau"] = level
    return materials
