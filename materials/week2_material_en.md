# Week 2: Motion principles and motion commands

**Cobot Course — seven weeks, one lesson day per week (240 minutes):**   
**Level:** NLQF 3  
**Machine (Track 1):** Doosan Robotics M1013 — SMEOT Hengelo  

> **Learning objective:** The student applies MoveJ, MoveL, and MoveC purposefully and recognizes the effect of blending and singularity.

## Lesson program (240 min)

| Duration | Block |
|---|---|
| 15 min | Welcome and safety check |
| 45 min | Direct instruction (Template A) |
| 25 min | Coached practice (Template B, part 1) |
| 10 min | Break |
| 100 min | Independent practice (Template B, part 2) |
| 25 min | Reflection and assessment (Template D) + shutdown procedure |

## Information sheet (Document type 1 / Template A) — Week 2: Motion principles and motion commands

**Learning objective:** The student applies MoveJ, MoveL, and MoveC purposefully and recognizes the effect of blending and singularity.

### Subjects
- MoveJ vs. MoveL vs. MoveC (Move Joint, Move Line, Move Circle)
- Speed, acceleration, and Blending
- Singularity during linear moves
- Switching between MoveJ and MoveL at the right moment

### Key safety principle (Track 1)

> ⚠️ A cobot is never inherently safe on its own; a risk assessment must cover arm, tooling, workpiece, process, and human proximity.

> ⚠️ Always simulate new programs first and test at low speed with one hand on the emergency stop.

> 💡 Name your waypoints with fixed names such as Above_Pick, Pick, Place, Home.

## Practical assignment (Document type 2 / Template B) — Week 2: Motion principles and motion commands

**Level:** NLQF 3 · Estimated duration: 240 min (lesson day) / 100-150 min (practice blocks)

Today you will work on: motion principles and motion commands.
Expected result: you applies movej, movel, and movec purposefully and recognizes the effect of blending and singularity.

> **Mandatory preparation:** Mandatory preparation: before starting, write a short work plan naming your motion trajectory (waypoints), motion commands, and safety measures.

### Assignments (progressive practice bank)
1. C2.1 Drawing a straight line with MoveL
2. C2.2 Tracing a square as one connected motion track
3. C2.3 Drawing a circle with MoveC
4. C2.4 Combining fast MoveJ transfers with precise MoveL approaches
5. C2.5 Smoothing motion with blending

> See Information sheet: Safe startup and shutdown. See Information sheet: Manual motion (jogging and Hand guiding).

### Checkpoints


|  | Achieved | Partly | Not achieved |
|---|---|---|---|
| Workspace inspected and emergency stop tested before Servo On | ☐ | ☐ | ☐ |
| Waypoints clearly named (Home, Pick, Place) | ☐ | ☐ | ☐ |
| Program simulated / tested at low speed first | ☐ | ☐ | ☐ |
| Motion validation correct (MoveL without blending at the pick point) | ☐ | ☐ | ☐ |
| Safe shutdown according to procedure | ☐ | ☐ | ☐ |

## Assessment rubric (Template D) — Week 2 — assessment

> **Knock-out criteria: all safety knock-out criteria must be met without exception: workspace inspected; emergency stop verified before motor power; no unauthorized modification of safety settings; safe shutdown per procedure.**

| Competency | 1 | 2 — Level 3 | 3 — Level 4 |
|---|---|---|---|
| System setup & calibration | Needs repeated guidance; gripper, TCP, payload, or wiring are configured incorrectly or sloppily. | Mounts the gripper, wires basic I/O properly, and calibrates TCP and payload independently and accurately. | Demonstrably optimizes workspace layout and Center of Gravity settings for ergonomics, reach, and cycle efficiency. |
| Programming & process logic | Program runs unstably; loops, frames, or I/O blocks contain errors or lack structure. | Combines MoveJ/MoveL, loops, and working I/O control accurately into a stable, safe production cycle. | Builds modularly with clean subroutines, clear naming, deliberate blending, and active error handling. |
| Troubleshooting & diagnostics | Loses overview, guesses randomly, or deletes parts of the existing program without analysis. | Uses the manual and structured checks to locate and fix the fault within the allotted time. | Directly analyzes raw data (I/O monitor, fault logs, measurements), isolates the root cause purposefully, and identifies preventive measures. |
| Safety, documentation & craftsmanship | Works messily, cannot explain technical decisions, or fails to deliver a usable program handover. | Works with discipline and safety, uses clear folder and task names, and explains system operation clearly to a colleague. | Delivers a complete, hand-over-ready cell with clean inline documentation and substantiates choices to the client. |

**Exam alignment:** Theory: motion control and manual operation (MoveJ/MoveL/MoveC, blending, singularity).

---

*Composed with the Cobot Course Composer from the three tracks (technology - NLQF pedagogy - SMEOT house style). Missing machine data always appears as a [REVIEW_MARKER], never as invented facts.*
