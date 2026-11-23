# Week 1: Safety, system components, and manual operation

**Cobot Course — seven weeks, one lesson day per week (240 minutes):**   
**Level:** NLQF 3  
**Machine (Track 1):** Doosan Robotics M1013 — SMEOT Hengelo  

> **Learning objective:** The student powers the cobot safely on and off and moves the arm manually to an indicated position.

## Lesson program (240 min)

| Duration | Block |
|---|---|
| 15 min | Welcome and safety check |
| 45 min | Direct instruction (Template A) |
| 25 min | Coached practice (Template B, part 1) |
| 10 min | Break |
| 100 min | Independent practice (Template B, part 2) |
| 25 min | Reflection and assessment (Template D) + shutdown procedure |

## Information sheet (Document type 1 / Template A) — Week 1: Safety, system components, and manual operation

**Learning objective:** The student powers the cobot safely on and off and moves the arm manually to an indicated position.

### Subjects
- Industrial robot vs. cobot; the five fixed main components
- Safety standards (ISO 10218-1/2:2025) and the four collaborative modes
- Emergency stop vs. Protective Stop; five protection layers
- Joints J1 through J6 and X/Y/Z; jogging and Hand guiding

### Key safety principle (Track 1)

> ⚠️ A cobot is never inherently safe on its own; a risk assessment must cover arm, tooling, workpiece, process, and human proximity.

> ⚠️ Always simulate new programs first and test at low speed with one hand on the emergency stop.

> 💡 Name your waypoints with fixed names such as Above_Pick, Pick, Place, Home.

## Practical assignment (Document type 2 / Template B) — Week 1: Safety, system components, and manual operation

**Level:** NLQF 3 · Estimated duration: 240 min (lesson day) / 100-150 min (practice blocks)

Today you will work on: safety, system components, and manual operation.
Expected result: you powers the cobot safely on and off and moves the arm manually to an indicated position.

> **Mandatory preparation:** Mandatory preparation: before starting, write a short work plan naming your motion trajectory (waypoints), motion commands, and safety measures.

### Assignments (progressive practice bank)
1. C1.1 Safely switching on and off following the fixed procedure
2. C1.2 Exploring each joint J1 through J6 individually (Joint jogging)
3. C1.3 Cartesian jogging along X, Y, and Z
4. C1.4 Hand guiding the arm to a mark on the table
5. C1.5 Saving individual waypoints with a pointer pin

> See Information sheet: Safe startup and shutdown. See Information sheet: Manual motion (jogging and Hand guiding).

### Checkpoints


|  | Achieved | Partly | Not achieved |
|---|---|---|---|
| Workspace inspected and emergency stop tested before Servo On | ☐ | ☐ | ☐ |
| Waypoints clearly named (Home, Pick, Place) | ☐ | ☐ | ☐ |
| Program simulated / tested at low speed first | ☐ | ☐ | ☐ |
| Motion validation correct (MoveL without blending at the pick point) | ☐ | ☐ | ☐ |
| Safe shutdown according to procedure | ☐ | ☐ | ☐ |

## Assessment rubric (Template D) — Week 1 — assessment

> **Knock-out criteria: all safety knock-out criteria must be met without exception: workspace inspected; emergency stop verified before motor power; no unauthorized modification of safety settings; safe shutdown per procedure.**

| Competency | 1 | 2 — Level 3 | 3 — Level 4 |
|---|---|---|---|
| System setup & calibration | Needs repeated guidance; gripper, TCP, payload, or wiring are configured incorrectly or sloppily. | Mounts the gripper, wires basic I/O properly, and calibrates TCP and payload independently and accurately. | Demonstrably optimizes workspace layout and Center of Gravity settings for ergonomics, reach, and cycle efficiency. |
| Programming & process logic | Program runs unstably; loops, frames, or I/O blocks contain errors or lack structure. | Combines MoveJ/MoveL, loops, and working I/O control accurately into a stable, safe production cycle. | Builds modularly with clean subroutines, clear naming, deliberate blending, and active error handling. |
| Troubleshooting & diagnostics | Loses overview, guesses randomly, or deletes parts of the existing program without analysis. | Uses the manual and structured checks to locate and fix the fault within the allotted time. | Directly analyzes raw data (I/O monitor, fault logs, measurements), isolates the root cause purposefully, and identifies preventive measures. |
| Safety, documentation & craftsmanship | Works messily, cannot explain technical decisions, or fails to deliver a usable program handover. | Works with discipline and safety, uses clear folder and task names, and explains system operation clearly to a colleague. | Delivers a complete, hand-over-ready cell with clean inline documentation and substantiates choices to the client. |

**Exam alignment:** Theory: system components, safe startup and shutdown, collaborative modes, risk assessment.

---

*Composed with the Cobot Course Composer from the three tracks (technology - NLQF pedagogy - SMEOT house style). Missing machine data always appears as a [REVIEW_MARKER], never as invented facts.*
