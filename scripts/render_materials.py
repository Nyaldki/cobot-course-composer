"""Render full learning materials for weeks 1-7 to Markdown files in materials/.

Rendered in both languages: Dutch (week{n}_materiaal.md) and English
(week{n}_material_en.md), per the Track 3 language rules.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.generator import generate_week, lesson_program
from app.loader import load_semester

OUT = Path(__file__).resolve().parent.parent / "materials"
OUT.mkdir(exist_ok=True)

EN = {
    "program": "Cobot Course — seven weeks, one lesson day per week (240 minutes)",
    "level": "Level", "machine": "Machine (Track 1)",
    "objective": "Learning objective",
    "lesson": "Lesson program (240 min)", "duration": "Duration", "block": "Block",
    "subjects": "Subjects", "safety": "Key safety principle (Track 1)",
    "assignments": "Assignments (progressive practice bank)",
    "preparation": "Mandatory preparation",
    "checkpoints": "Checkpoints", "achieved": "Achieved", "partly": "Partly", "not": "Not achieved",
    "exam": "Exam alignment", "footer": ("Composed with the Cobot Course Composer from the three tracks "
                                          "(technology - NLQF pedagogy - SMEOT house style). Missing machine "
                                          "data always appears as a [REVIEW_MARKER], never as invented facts."),
}
NL = {
    "program": "Cobot Course — zeven weken, één lesdag per week (240 minuten)",
    "level": "Niveau", "machine": "Machine (Track 1)",
    "objective": "Leerdoel",
    "lesson": "Lesprogramma (240 min)", "duration": "Duur", "block": "Blok",
    "subjects": "Onderwerpen", "safety": "Belangrijkste veiligheidsprincipe (Track 1)",
    "assignments": "Opdrachten (progressieve oefenbank)",
    "preparation": "Verplichte voorbereiding",
    "checkpoints": "Checkpoints", "achieved": "Behaald", "partly": "Deels", "not": "Niet behaald",
    "exam": "Examenkoppeling", "footer": ("Samengesteld met de Cobot Course Composer op basis van de drie "
                                          "tracks (techniek · NLQF-pedagogiek · SMEOT-huisstijl). Ontbrekende "
                                          "machinegegevens verschijnen altijd als [REVIEW_MARKER] en nooit "
                                          "als verzonnen feiten."),
}


def md_table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    lines += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(lines)


def week_markdown(sem, n, lang="nl", level="NLQF 3", case=None):
    L = EN if lang == "en" else NL
    mats = generate_week(sem, n, level=level, case_profile=case, lang=lang)
    week = mats["week_programma"]
    pr = mats["praktijkopdracht"]
    info = mats["informatieblad"]
    theme = week["theme"]
    lines = []
    lines.append(f"# {'Week' if lang == 'en' else 'Week'} {n}: {theme}")
    lines.append("")
    lines.append(f"**{L['program']}:**   ")
    lines.append(f"**{L['level']}:** {mats['praktijkopdracht']['niveau']}  ")
    lines.append(f"**{L['machine']}:** {week['machine']['model']} — {week['machine']['institution']}  ")
    lines.append("")
    lines.append(f"> **{L['objective']}:** {week['objective']}")
    lines.append("")
    lines.append(f"## {L['lesson']}")
    lines.append("")
    lines.append(md_table([L["duration"], L["block"]],
                          [[b["minutes"], b["label"]] for b in week["blokkenschema"]]))
    lines.append("")
    lines.append(f"## {info['doctype']} — {info['titel']}")
    lines.append("")
    lines.append(f"**{L['objective']}:** {info['leerdoel']}")
    lines.append("")
    lines.append(f"### {L['subjects']}")
    lines.extend(f"- {t}" for t in info["onderwerpen"])
    lines.append("")
    lines.append(f"### {L['safety']}")
    lines.append("")
    lines.append(f"> ⚠️ {info['veiligheidskader']}")
    lines.append("")
    lines.append(f"> ⚠️ {info['waarschuwing']}")
    lines.append("")
    lines.append(f"> 💡 {info['tip']}")
    lines.append("")
    lines.append(f"## {pr['doctype']} — {pr['titel']}")
    lines.append("")
    lines.append(f"**{L['level']}:** {pr['niveau']} · {pr['duur_geschat']}")
    lines.append("")
    lines.extend(pr["introductie"])
    lines.append("")
    lines.append(f"> **{L['preparation']}:** {pr['voorbereiding_verplicht']}")
    lines.append("")
    if pr.get("case_brief"):
        cb = pr["case_brief"]
        lines.append(f"### {cb['titel']}")
        lines.append("")
        lines.append(cb["context"])
        lines.append("")
        elements_label = "Mandatory core elements" if lang == "en" else "Verplichte kernelementen"
        lines.append(f"**{elements_label}:** {cb['verplichte_elementen']}")
        lines.append("")
    lines.append(f"### {L['assignments']}")
    lines.extend(f"{i}. {a}" for i, a in enumerate(pr["opdrachten"], 1))
    lines.append("")
    lines.append(f"> {pr['kruisverwijzingen']}")
    lines.append("")
    lines.append(f"### {L['checkpoints']}")
    lines.append("")
    lines.append("")
    ckpt = md_table(["", L["achieved"], L["partly"], L["not"]],
                    [[c, "☐", "☐", "☐"] for c in pr["checkpointcriteria"]])
    lines.append(ckpt)
    lines.append("")
    as_ = mats["beoordelingslijst"]
    lines.append(f"## {as_['doctype']} — {as_['titel']}")
    lines.append("")
    lines.append(f"> **{as_['knockoutcriteria']}**")
    lines.append("")
    lines.append(md_table(
        ["Competentie" if lang == "nl" else "Competency", "1", "2 — NLQF 3" if lang == "nl" else "2 — Level 3", "3 — NLQF 4" if lang == "nl" else "3 — Level 4"],
        [[r["competentie"], r["1_onvoldoende"], r["2_voldoende_nlqf3"], r["3_uitstekend_nlqf4"]] for r in as_["matrix"]],
    ))
    lines.append("")
    if "examemateriaal" in mats:
        ex = mats["examemateriaal"]
        theory_label = "Theory" if lang == "en" else "Theorie"
        lines.append(f"## {ex['doctype']} — {ex['titel']}")
        lines.append("")
        dur_label = "Total duration" if lang == "en" else "Totale duur"
        lines.append(f"**{dur_label}:** {ex['totale_duur']}")
        lines.append("")
        th = ex["onderdeel_theorie"]
        comp_label = "Component" if lang == "en" else "Onderdeel"
        lines.append(f"### {comp_label} 1: {th['naam']} ({th['duur']} min)")
        lines.append("")
        lines.extend(f"- {d}" for d in th["domeinen"])
        lines.append("")
        if lang == "en":
            lines.append(f"**Extra for NLQF Level 4:** {', '.join(th['niveau4'])}")
        else:
            lines.append(f"**Extra voor NLQF 4:** {', '.join(th['niveau4'])}")
        lines.append("")
        fe = ex["onderdeel_find_error"]
        lines.append(f"### {comp_label} 2: {fe['naam']} ({fe['duur']})")
        lines.append("")
        fc_label = "Fault classes" if lang == "en" else "Foutklassen"
        lines.append(f"**{fc_label} (1) {fe['foutklassen'][0]}, (2) {fe['foutklassen'][1]}, (3) {fe['foutklassen'][2]}, (4) {fe['foutklassen'][3]}**")
        lines.append("")
        gr_label = "Grading" if lang == "en" else "Beoordeling"
        lines.append(f"**{gr_label}:** {fe['beoordeling']}")
        lines.append("")
        pa = ex["onderdeel_praktijk"]
        lines.append(f"### {comp_label} 3: {pa['naam']} ({pa['duur']} min)")
        lines.append("")
        if pa.get("case"):
            cs = pa["case"]
            lines.append(f"**Case {cs['nr']} — {cs['name']}:** {cs['context']}")
            lines.append("")
            lines.append(f"*{elements_label}:* {cs['elements']}")
            lines.append("")
        shell_label = "Exam shell (applied to every issued exam sheet)" if lang == "en" else "Caseschil (voor elk uitgegeven examenblad)"
        lines.append(f"**{shell_label}:**")
        lines.extend(f"- {s}" for s in pa["caseschil"])
        lines.append("")
        ko_label = "Knock-out criteria (immediate fail)" if lang == "en" else "Knock-outcriteria (direct onvoldoend)"
        lines.append(f"### {ko_label}")
        lines.extend(f"- {k}" for k in ex["knockoutcriteria"])
        lines.append("")
        pass_label = "Pass rules" if lang == "en" else "Slagingsregels"
        lines.append(f"### {pass_label}")
        lines.append(f"- **NLQF 3:** {ex['slagingsregels']['level3']}")
        lines.append(f"- **NLQF 4:** {ex['slagingsregels']['level4']}")
        lines.append("")
    exam_link = mats["week_programma"]["week"].get("exam_link_en" if lang == "en" else "exam_link")
    if exam_link is None:
        tw = sem.translations_en["weeks"][n] if lang == "en" else None
        exam_link = tw["exam_link"] if tw else mats["week_programma"]["week"].get("exam_link")
    lines.append(f"**{L['exam']}:** {exam_link}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*{L['footer']}*")
    lines.append("")
    return "\n".join(lines)


def main():
    sem = load_semester()
    cases = {7: 1}
    for n in range(1, 8):
        level = "NLQF 4" if n in (5, 6, 7) else "NLQF 3"
        for lang, suffix in (("nl", "materiaal"), ("en", "material_en")):
            text = week_markdown(sem, n, lang=lang, level=level, case=cases.get(n))
            path = OUT / f"week{n}_{suffix}.md"
            path.write_text(text, encoding="utf-8")
            print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
