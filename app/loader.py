"""Loads the three tracks, machine sub-modules, and curriculum from YAML.

The three pillars are strictly separated:
- Track 1 = technical ground truth (universal core + swappable machine module)
- Track 2 = pedagogical blueprint & NLQF framework
- Track 3 = visual identity & language rules (swappable)

Track 1 facts are never invented or overridden by Tracks 2/3. Any technical
parameter that is missing from the active machine sub-module surfaces as an
explicit review marker instead of generated content.
"""

from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

import yaml

BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge"
MACHINES_DIR = KNOWLEDGE_DIR / "machines"

REVIEW_MARKER = "[REVIEW_MARKER: {detail} | Onvoldoende geverifieerd in het actieve machine-sub-module; docent/technisch beheerder controleert deze waarde.]"


@dataclass
class Semester:
    track1_core: dict
    track2: dict
    track3: dict
    curriculum: dict
    machines: list = field(default_factory=list)


def _load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def list_machine_modules() -> list[dict]:
    modules = []
    for path in sorted(MACHINES_DIR.glob("*.yaml")):
        data = _load_yaml(path)
        modules.append(
            {
                "id": data["meta"]["id"],
                "model": data["robot"]["model"],
                "institution": data["meta"]["institution_context"],
                "status": data["meta"]["status"],
                "active": data["meta"]["status"] == "active",
            }
        )
    return modules


def load_semester(machine_id: str | None = None) -> Semester:
    machines = list_machine_modules()
    active_id = machine_id
    if active_id is None:
        active = [m for m in machines if m["active"]]
        if not active:
            raise ValueError("Geen actief machine-sub-module gevonden in knowledge/machines/.")
        active_id = active[0]["id"]

    machine_file = MACHINES_DIR / (active_id.replace("machine_", "", 1) + ".yaml")
    # id 'machine_doosan_m1013' maps to file doosan_m1013.yaml
    if not machine_file.exists():
        matches = [p for p in MACHINES_DIR.glob("*.yaml") if active_id.endswith(p.stem)]
        if not matches:
            raise ValueError(f"Machine-sub-module '{active_id}' bestaat niet.")
        machine_file = matches[0]

    return Semester(
        track1_core=_load_yaml(KNOWLEDGE_DIR / "track1_core.yaml"),
        track2=_load_yaml(KNOWLEDGE_DIR / "track2_pedagogy.yaml"),
        track3=_load_yaml(KNOWLEDGE_DIR / "track3_style_smeot.yaml"),
        curriculum=_load_yaml(KNOWLEDGE_DIR / "curriculum.yaml"),
        machines=machines,
    )


def load_machine(machine_id: str) -> dict:
    matches = [p for p in MACHINES_DIR.glob("*.yaml") if machine_id.endswith(p.stem)]
    if not matches:
        raise ValueError(f"Machine-sub-module '{machine_id}' bestaat niet.")
    return _load_yaml(matches[0])


def brand_term(machine: dict, key: str) -> str:
    """Return the brand-specific term; NEVER fall back to a generic guess.
    Missing values become explicit review markers per the Track 1 hierarchy."""
    value = machine.get("brand_terms", {}).get(key)
    if not value:
        return REVIEW_MARKER.format(detail=f"Merkterm '{key}' ontbreekt")
    return value


@lru_cache(maxsize=8)
def _cached_semester(machine_id: str | None) -> Semester:
    return load_semester(machine_id)
