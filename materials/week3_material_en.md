# Week 3: Gripping and repetitive production logic

**Cobot Course — seven weeks, one lesson day per week (240 minutes):**   
**Level:** NLQF 3  
**Machine (Track 1):** Doosan Robotics M1013 — SMEOT Hengelo  

> **Learning objective:** The student builds a stable pick-and-place cycle with gripper and a Repeat loop.

## Lesson program (240 min)

| Duration | Block |
|---|---|
| 15 min | Welcome and safety check |
| 45 min | Direct instruction (Template A) |
| 25 min | Coached practice (Template B, part 1) |
| 10 min | Break |
| 100 min | Independent practice (Template B, part 2) |
| 25 min | Reflection and assessment (Template D) + shutdown procedure |

## Information sheet (Document type 1 / Template A) — Week 3: Gripping and repetitive production logic

**Learning objective:** The student builds a stable pick-and-place cycle with gripper and a Repeat loop.

### Subjects
- Standard pick-and-place trajectory (Home, Approach, Pick, Retreat, Place)
- Grippers: two/three-finger, vacuum, magnetic
- Repeat/loop with a counter; anti-cyclic design
- Calibrating TCP and payload correctly (Smart Setup)

### Key safety principle (Track 1)

> ⚠️ A cobot is never inherently safe on its own; a risk assessment must cover arm, tooling, workpiece, process, and human proximity.

> ⚠️ Always simulate new programs first and test at low speed with one hand on the emergency stop.

> 💡 Name your waypoints with fixed names such as Above_Pick, Pick, Place, Home.

## Practical assignment (Document type 2 / Template B) — Week 3: Gripping and repetitive production logic

**Level:** NLQF 3 · Estimated duration: 240 min (lesson day) / 100-150 min (practice blocks)

Today you will work on: gripping and repetitive production logic.
Expected result: you builds a stable pick-and-place cycle with gripper and a repeat loop.

> **Mandatory preparation:** Mandatory preparation: before starting, write a short work plan naming your motion trajectory (waypoints), motion commands, and safety measures.

### Assignments (progressive practice bank)
1. C3.1 Single pick-and-place
2. C3.2 Moving parts to multiple drop-off locations with approach and retreat points
3. C3.3 Repeat loop for ten cycles
4. C3.4 Stacking five blocks via a Z-offset

> See Information sheet: Safe startup and shutdown. See Information sheet: Manual motion (jogging and Hand guiding).

### Checkpoints


|  | Achieved | Partly | Not achieved |
|---|---|---|---|
| Workspace inspected and emergency stop tested before Servo On | ☐ | ☐ | ☐ |
| Waypoints clearly named (Home, Pick, Place) | ☐ | ☐ | ☐ |
| Program simulated / tested at low speed first | ☐ | ☐ | ☐ |
| Motion validation correct (MoveL without blending at the pick point) | ☐ | ☐ | ☐ |
| Safe shutdown according to procedure | ☐ | ☐ | ☐ |

## Assessment rubric (Template D) — Week 3 — assessment

> **Knock-out criteria: all safety knock-out criteria must be met without exception: workspace inspected; emergency stop verified before motor power; no unauthorized modification of safety settings; safe shutdown per procedure.**

| Competency | 1 | 2 — Level 3 | 3 — Level 4 |
|---|---|---|---|
| System setup & calibration | Needs repeated guidance; gripper, TCP, payload, or wiring are configured incorrectly or sloppily. | Mounts the gripper, wires basic I/O properly, and calibrates TCP and payload independently and accurately. | Demonstrably optimizes workspace layout and Center of Gravity settings for ergonomics, reach, and cycle efficiency. |
| Programming & process logic | Program runs unstably; loops, frames, or I/O blocks contain errors or lack structure. | Combines MoveJ/MoveL, loops, and working I/O control accurately into a stable, safe production cycle. | Builds modularly with clean subroutines, clear naming, deliberate blending, and active error handling. |
| Troubleshooting & diagnostics | Loses overview, guesses randomly, or deletes parts of the existing program without analysis. | Uses the manual and structured checks to locate and fix the fault within the allotted time. | Directly analyzes raw data (I/O monitor, fault logs, measurements), isolates the root cause purposefully, and identifies preventive measures. |
| Safety, documentation & craftsmanship | Works messily, cannot explain technical decisions, or fails to deliver a usable program handover. | Works with discipline and safety, uses clear folder and task names, and explains system operation clearly to a colleague. | Delivers a complete, hand-over-ready cell with clean inline documentation and substantiates choices to the client. |

**Exam alignment:** Theory: kinematics and coordinates (J1-J6, X/Y/Z, TCP, payload, Base/Tool/User frame).

---

*Composed with the Cobot Course Composer from the three tracks (technology - NLQF pedagogy - SMEOT house style). Missing machine data always appears as a [REVIEW_MARKER], never as invented facts.*
