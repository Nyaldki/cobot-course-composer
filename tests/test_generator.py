import pytest
from fastapi.testclient import TestClient

from app.generator import (
    assessment_sheet,
    exam_materials,
    generate_week,
    info_sheet,
    lesson_program,
    practical_assignment,
)
from app.loader import REVIEW_MARKER, load_semester, load_machine, brand_term


@pytest.fixture
def sem():
    return load_semester()


def test_curriculum_has_seven_weeks(sem):
    assert len(sem.curriculum["weeks"]) == 7
    assert [w["number"] for w in sem.curriculum["weeks"]] == list(range(1, 8))


def test_day_is_four_hours(sem):
    assert sem.curriculum["defaults"]["day_minutes"] == 240


def test_week_program(sem):
    program = lesson_program(sem, 3)
    assert program["week"]["number"] == 3
    assert program["machine"]["model"] == "Doosan Robotics M1013"
    assert program["totaal_minuten"] == 240
    assert program["blokkenschema"]


def test_week_program_unknown_week(sem):
    with pytest.raises(ValueError):
        lesson_program(sem, 9)


def test_info_sheet_uses_dutch_body(sem):
    sheet = info_sheet(sem, 1)
    assert sheet["doctype"].startswith("Informatieblad")
    assert "De student" in sheet["leerdoel"]
    assert sheet["waarschuwing"].startswith("Simuleer")


def test_practical_assignment(sem):
    assignment = practical_assignment(sem, 2)
    assert assignment["niveau"]
    assert any("C2." in a for a in assignment["opdrachten"])
    assert "gripper" in assignment["materiaal"]["grijper"].lower()


def test_practical_assignment_case_profile(sem):
    assignment = practical_assignment(sem, 7, case_profile=2)
    brief = assignment["case_brief"]
    assert brief["titel"].startswith("Praktijkcase 2")
    assert "Repeat" in brief["verplichte_elementen"]


def test_rubric_matrix(sem):
    sheet = assessment_sheet(sem, 5)
    assert len(sheet["matrix"]) == 4
    assert "knock-out" in sheet["knockoutcriteria"].lower()


def test_exam_materials_only_week7(sem):
    materials = exam_materials(sem, 7, case_profile=1)
    assert "Machine Tending" in materials["onderdeel_praktijk"]["case"]["name"]
    with pytest.raises(ValueError):
        exam_materials(sem, 2)


def test_review_marker_on_missing_brand_term():
    machine = load_machine("machine_doosan_m1013")
    assert brand_term(machine, "move_joint") == "Move J"
    assert brand_term(machine, "nonexistent") .startswith(REVIEW_MARKER[:15])


def test_generate_week_includes_all_templates(sem):
    materials = generate_week(sem, 4, level="NLQF 4")
    for key in ("week_programma", "informatieblad", "praktijkopdracht", "beoordelingslijst"):
        assert key in materials
    assert materials["niveau"] == "NLQF 4"


def test_generate_week_exam_includes_exam_materials(sem):
    materials = generate_week(sem, 7)
    assert "examemateriaal" in materials
    assert materials["examemateriaal"]["totale_duur"] == "240 min"


# --- HTTP layer ---

client = TestClient(app := __import__("app.main", fromlist=["app"]).app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "week" in response.text.lower()


def test_compose_form():
    response = client.post("/compose", data={"week": 3, "level": "NLQF 3", "machine_id": "", "case_profile": 0})
    assert response.status_code == 200
    assert "pick-and-place" in response.text.lower()


def test_api_weeks():
    response = client.get("/api/weeks")
    assert response.status_code == 200
    assert len(response.json()["weeks"]) == 7


def test_api_week_detail():
    response = client.get("/api/weeks/5")
    assert response.status_code == 200
    assert response.json()["week"]["theme"].startswith("Ruimtelijk")


def test_api_generate():
    response = client.post("/api/generate?week=7&case_profile=3")
    assert response.status_code == 200
    body = response.json()
    assert body["examemateriaal"]["onderdeel_praktijk"]["case"]["nr"] == 3


def test_api_generate_invalid_week():
    response = client.post("/api/generate?week=99")
    assert response.status_code == 400


# --- English rendering ---

def test_english_info_sheet(sem):
    sheet = info_sheet(sem, 1, lang="en")
    assert sheet["doctype"] == "Information sheet (Document type 1 / Template A)"
    assert sheet["titel"] == "Week 1: Safety, system components, and manual operation"
    assert sheet["onderwerpen"][0].startswith("Industrial robot vs. cobot")
    assert sheet["veiligheidskader"].startswith("A cobot is never")


def test_english_practical_assignment(sem):
    assignment = practical_assignment(sem, 3, lang="en")
    assert assignment["opdrachten"][0].startswith("C3.1 Single pick-and-place")
    assert "work plan" in assignment["voorbereiding_verplicht"]


def test_english_rubric(sem):
    sheet = assessment_sheet(sem, 5, lang="en")
    assert sheet["matrix"][0]["competentie"] == "System setup & calibration"
    assert sheet["matrix"][0]["2_voldoende_nlqf3"].startswith("Mounts the gripper")


def test_english_exam_materials(sem):
    materials = exam_materials(sem, 7, case_profile=2, lang="en")
    assert materials["onderdeel_praktijk"]["case"]["context"].startswith("Fully automated stacking")
    assert materials["slagingsregels"]["level4"].startswith("Score 3 on at least three")


def test_english_via_api():
    response = client.post("/api/generate?week=2&lang=en")
    assert response.status_code == 200
    body = response.json()
    assert body["informatieblad"]["titel"] == "Week 2: Motion principles and motion commands"


def test_dutch_still_default_via_api():
    response = client.post("/api/generate?week=2")
    body = response.json()
    assert body["informatieblad"]["titel"].startswith("Week 2: Bewegingsprincipes")
