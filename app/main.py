"""Cobot Course Composer — FastAPI teacher interface.

Compose cobot learning materials from three separated tracks:
Track 1 (technical ground truth), Track 2 (NLQF pedagogy), Track 3 (visual identity & language).
"""

from pathlib import Path

import yaml
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.generator import generate_week, lesson_program
from app.loader import load_semester, list_machine_modules

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=BASE_DIR / "app" / "templates")

app = FastAPI(title="Cobot Course Composer", version="0.1.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "app" / "static"), name="static")


def _week_numbers():
    sem = load_semester()
    return [w["number"] for w in sem.curriculum["weeks"]]


def _case_profiles():
    sem = load_semester()
    practical = next(
        c for c in sem.track2["exam_blueprint"]["components"] if "case_profiles" in c
    )
    return practical["case_profiles"]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    sem = load_semester()
    weeks = sem.curriculum["weeks"]
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "weeks": [
                {"number": w["number"], "theme": w["theme"], "phase": w["phase"], "level": w["level"]}
                for w in weeks
            ],
            "machines": sem.machines,
            "style": sem.track3,
        },
    )


@app.post("/compose", response_class=HTMLResponse)
async def compose(
    request: Request,
    week: int = Form(...),
    level: str = Form("NLQF 3"),
    machine_id: str = Form(""),
    case_profile: int = Form(0),
):
    sem = load_semester(machine_id or None)
    case = case_profile if case_profile > 0 else None
    try:
        materials = generate_week(sem, week, level=level, machine_id=machine_id or None, case_profile=case)
    except ValueError as exc:
        return templates.TemplateResponse(
            request,
            "error.html",
            {"message": str(exc)},
            status_code=400,
        )
    return templates.TemplateResponse(
        request,
        "materials.html",
        {
            "materials": materials,
            "week": week,
            "level": level,
            "machine_id": machine_id or sem.machines[0]["id"],
            "case_profile": case,
        },
    )


@app.get("/api/weeks")
async def weeks():
    sem = load_semester()
    return {"weeks": sem.curriculum["weeks"]}


@app.get("/api/weeks/{number}")
async def week_detail(number: int):
    sem = load_semester()
    return lesson_program(sem, number)


@app.get("/api/machines")
async def machines():
    return {"machines": list_machine_modules()}


@app.post("/api/generate")
async def generate(
    week: int,
    level: str | None = None,
    machine_id: str | None = None,
    case_profile: int | None = None,
):
    sem = load_semester(machine_id)
    try:
        return generate_week(
            sem, week, level=level, machine_id=machine_id, case_profile=case_profile
        )
    except ValueError as exc:
        return JSONResponse({"error": str(exc)}, status_code=400)
