"""Render full learning materials for weeks 1-7 to Markdown files in materials/."""

from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from app.generator import generate_week, lesson_program
from app.loader import load_semester

OUT = Path(__file__).resolve().parent.parent / "materials"
OUT.mkdir(exist_ok=True)


def md_table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    lines += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(lines)


def week_markdown(sem, n, level="NLQF 3", case=None):
    week = lesson_program(sem, n)
    mats = generate_week(sem, n, level=level, case_profile=case)
    w = mats["week_programma"]["week"]
    lines = []
    lines.append(f"# Week {n}: {w['theme']}")
    lines.append("")
    lines.append(f"**Programma:** Cobot Course — zeven weken, één lesdag per week (240 minuten)  ")
    lines.append(f"**Niveau:** {mats['praktijkopdracht']['niveau']}  ")
    lines.append(f"**Machine (Track 1):** {week['machine']['model']} — {week['machine']['institution']}  ")
    lines.append("")
    lines.append(f"> **Leerdoel:** {w['learning_objective']}")
    lines.append("")

    lines.append("## Lesprogramma (240 min)")
    lines.append("")
    lines.append(md_table(["Duur", "Blok"], [[b["minutes"], b["label"]] for b in week["blokkenschema"]]))
    lines.append("")

    info = mats["informatieblad"]
    lines.append(f"## {info['doctype']} — {info['titel']}")
    lines.append("")
    lines.append(f"**Leerdoel:** {info['leerdoel']}")
    lines.append("")
    lines.append("### Onderwerpen")
    lines.extend(f"- {t}" for t in info["onderwerpen"])
    lines.append("")
    lines.append("### Belangrijkste veiligheidsprincipe (Track 1)")
    lines.append("")
    lines.append(f"> ⚠️ {info['veiligheidskader']}")
    lines.append("")
    lines.append(f"> ⚠️ {info['waarschuwing']}")
    lines.append("")
    lines.append(f"> 💡 **Tip:** {info['tip']}")
    lines.append("")

    pr = mats["praktijkopdracht"]
    lines.append(f"## {pr['doctype']} — {pr['titel']}")
    lines.append("")
    lines.append(f"**Niveau:** {pr['niveau']} · **Geschatte duur:** {pr['duur_geschat']}")
    lines.append("")
    lines.append(f"**Materiaal:** {pr['materiaal']['machine']} met {pr['materiaal']['grijper']}; {pr['materiaal']['drukknoppen']}")
    lines.append("")
    lines.extend(pr["introductie"])
    lines.append("")
    lines.append(f"> **Verplichte voorbereiding:** {pr['voorbereiding_verplicht']}")
    lines.append("")
    if pr.get("case_brief"):
        cb = pr["case_brief"]
        lines.append(f"### {cb['titel']}")
        lines.append("")
        lines.append(cb["context"])
        lines.append("")
        lines.append(f"**Verplichte kernelementen:** {cb['verplichte_elementen']}")
        lines.append("")
    lines.append("### Opdrachten (progressieve oefenbank)")
    lines.extend(f"{i}. {a}" for i, a in enumerate(pr["opdrachten"], 1))
    lines.append("")
    lines.append(f"> {pr['kruisverwijzingen']}")
    lines.append("")
    lines.append("### Checkpoints")
    lines.append("")
    lines.append(md_table(["Criterium", "Behaald", "Deels", "Niet behaald"], [[c, "☐", "☐", "☐"] for c in pr["checkpointcriteria"]]))
    lines.append("")

    as_ = mats["beoordelingslijst"]
    lines.append(f"## {as_['doctype']} — week {n}")
    lines.append("")
    lines.append(f"> **Knock-outcriteria:** {as_['knockoutcriteria']}")
    lines.append("")
    lines.append(md_table(
        ["Competentie", "1 — Onvoldoende", "2 — NLQF 3", "3 — NLQF 4"],
        [[r["competentie"], r["1_onvoldoende"], r["2_voldoende_nlqf3"], r["3_uitstekend_nlqf4"]] for r in as_["matrix"]],
    ))
    lines.append("")

    if "examemateriaal" in mats:
        ex = mats["examemateriaal"]
        lines.append(f"## {ex['doctype']} — {ex['titel']}")
        lines.append("")
        lines.append(f"**Totale duur:** {ex['totale_duur']}")
        lines.append("")
        th = ex["onderdeel_theorie"]
        lines.append(f"### Onderdeel 1: {th['naam']} ({th['duur']} min)")
        lines.append("")
        lines.extend(f"- {d}" for d in th["domeinen"])
        lines.append("")
        lines.append(f"**Extra voor NLQF 4:** {', '.join(th['niveau4'])}")
        lines.append("")
        fe = ex["onderdeel_find_error"]
        lines.append(f"### Onderdeel 2: {fe['naam']} ({fe['duur']})")
        lines.append("")
        lines.append(f"**Foutklassen:** {', '.join(fe['foutklassen'])}")
        lines.append("")
        lines.append(f"**Beoordeling:** {fe['beoordeling']}")
        lines.append("")
        pa = ex["onderdeel_praktijk"]
        lines.append(f"### Onderdeel 3: {pa['naam']} ({pa['duur']} min)")
        lines.append("")
        if pa.get("case"):
            lines.append(f"**Case {pa['case']['nr']} — {pa['case']['name']}:** {pa['case']['context']}")
            lines.append("")
            lines.append(f"*Verplichte kernelementen:* {pa['case']['elements']}")
            lines.append("")
        lines.append("**Caseschil (voor elk uitgegeven examenblad):**")
        lines.extend(f"- {s}" for s in pa["caseschil"])
        lines.append("")
        lines.append("### Knock-outcriteria (direct onvoldoend)")
        lines.extend(f"- {k}" for k in ex["knockoutcriteria"])
        lines.append("")
        lines.append("### Slagingsregels")
        lines.append(f"- **NLQF 3:** {ex['slagingsregels']['level3']}")
        lines.append(f"- **NLQF 4:** {ex['slagingsregels']['level4']}")
        lines.append("")

    lines.append(f"**Examenkoppeling:** {w['exam_link']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Samengesteld met de Cobot Course Composer op basis van de drie tracks (techniek · NLQF-pedagogiek · SMEOT-huisstijl). Ontbrekende machinegegevens verschijnen altijd als [REVIEW_MARKER] en nooit als verzonnen feiten.*")
    lines.append("")
    return "\n".join(lines)


def main():
    sem = load_semester()
    cases = {4: None, 7: 1}
    for n in range(1, 8):
        level = "NLQF 4" if n in (5, 6, 7) else "NLQF 3"
        text = week_markdown(sem, n, level=level, case=cases.get(n))
        path = OUT / f"week{n}_materiaal.md"
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
