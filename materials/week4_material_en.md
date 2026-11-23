# Week 4: Grids, crate filling, and palletizing

**Cobot Course — seven weeks, one lesson day per week (240 minutes):**   
**Level:** 3-4  
**Machine (Track 1):** Doosan Robotics M1013 — SMEOT Hengelo  

> **Learning objective:** The student fills a grid and a mini-pallet using mathematical offsets in X, Y, and Z.

## Lesson program (240 min)

| Duration | Block |
|---|---|
| 15 min | Welcome and safety check |
| 45 min | Direct instruction (Template A) |
| 25 min | Coached practice (Template B, part 1) |
| 10 min | Break |
| 100 min | Independent practice (Template B, part 2) |
| 25 min | Reflection and assessment (Template D) + shutdown procedure |

## Information sheet (Document type 1 / Template A) — Week 4: Grids, crate filling, and palletizing

**Learning objective:** The student fills a grid and a mini-pallet using mathematical offsets in X, Y, and Z.

### Subjects
- Matrix logic: rows and columns across X and Y
- Palletizing: fill a layer across X/Y, then step up in Z per layer
- Subroutines for gripping and releasing
- Deliberately shortening cycle time without compromising safety

### Key safety principle (Track 1)

> ⚠️ A cobot is never inherently safe on its own; a risk assessment must cover arm, tooling, workpiece, process, and human proximity.

> ⚠️ Always simulate new programs first and test at low speed with one hand on the emergency stop.

> 💡 Name your waypoints with fixed names such as Above_Pick, Pick, Place, Home.

## Practical assignment (Document type 2 / Template B) — Week 4: Grids, crate filling, and palletizing

**Level:** 3-4 · Estimated duration: 240 min (lesson day) / 100-150 min (practice blocks)

Today you will work on: grids, crate filling, and palletizing.
Expected result: you fills a grid and a mini-pallet using mathematical offsets in x, y, and z.

> **Mandatory preparation:** Mandatory preparation: before starting, write a short work plan naming your motion trajectory (waypoints), motion commands, and safety measures.

### Assignments (progressive practice bank)
1. C4.1 Filling a crate with twelve bottles in rows and columns (X and Y)
2. C4.2 Multi-layer palletizing

> See Information sheet: Safe startup and shutdown. See Information sheet: Manual motion (jogging and Hand guiding).

### Checkpoints


|  | Achieved | Partly | Not achieved |
|---|---|---|---|
| Workspace inspected and emergency stop tested before Servo On | ☐ | ☐ | ☐ |
| Waypoints clearly named (Home, Pick, Place) | ☐ | ☐ | ☐ |
| Program simulated / tested at low speed first | ☐ | ☐ | ☐ |
| Motion validation correct (MoveL without blending at the pick point) | ☐ | ☐ | ☐ |
| Safe shutdown according to procedure | ☐ | ☐ | ☐ |

## Assessment rubric (Template D) — Week 4 — assessment

> **Knock-out criteria: all safety knock-out criteria must be met without exception: workspace inspected; emergency stop verified before motor power; no unauthorized modification of safety settings; safe shutdown per procedure.**

| Competency | 1 | 2 — Level 3 | 3 — Level 4 |
|---|---|---|---|
| System setup & calibration | Needs repeated guidance; gripper, TCP, payload, or wiring are configured incorrectly or sloppily. | Mounts the gripper, wires basic I/O properly, and calibrates TCP and payload independently and accurately. | Demonstrably optimizes workspace layout and Center of Gravity settings for ergonomics, reach, and cycle efficiency. |
| Programming & process logic | Program runs unstably; loops, frames, or I/O blocks contain errors or lack structure. | Combines MoveJ/MoveL, loops, and working I/O control accurately into a stable, safe production cycle. | Builds modularly with clean subroutines, clear naming, deliberate blending, and active error handling. |
| Troubleshooting & diagnostics | Loses overview, guesses randomly, or deletes parts of the existing program without analysis. | Uses the manual and structured checks to locate and fix the fault within the allotted time. | Directly analyzes raw data (I/O monitor, fault logs, measurements), isolates the root cause purposefully, and identifies preventive measures. |
| Safety, documentation & craftsmanship | Works messily, cannot explain technical decisions, or fails to deliver a usable program handover. | Works with discipline and safety, uses clear folder and task names, and explains system operation clearly to a colleague. | Delivers a complete, hand-over-ready cell with clean inline documentation and substantiates choices to the client. |

**Exam alignment:** Practical case profiles 2 (palletizing) and 3 (crate filling): mandatory core elements.

---

*Composed with the Cobot Course Composer from the three tracks (technology - NLQF pedagogy - SMEOT house style). Missing machine data always appears as a [REVIEW_MARKER], never as invented facts.*
