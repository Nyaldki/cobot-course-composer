# Week 7: Certification exam (4 hours, 240 minutes)

**Cobot Course — seven weeks, one lesson day per week (240 minutes):**   
**Level:** 3-4  
**Machine (Track 1):** Doosan Robotics M1013 — SMEOT Hengelo  

> **Learning objective:** The candidate completes the full certification exam: theory, troubleshooting, and a practical case.

## Lesson program (240 min)

| Duration | Block |
|---|---|
| 30 min | Theorie-examen |
| 20-30 min | Find the Error / storingzoeken |
| 180 min | Praktijkcase-examen |

## Information sheet (Document type 1 / Template A) — Week 7: Certification exam (4 hours, 240 minutes)

**Learning objective:** The candidate completes the full certification exam: theory, troubleshooting, and a practical case.

### Subjects
- Theory recap and exam preparation (see examination sheet)

### Key safety principle (Track 1)

> ⚠️ A cobot is never inherently safe on its own; a risk assessment must cover arm, tooling, workpiece, process, and human proximity.

> ⚠️ Always simulate new programs first and test at low speed with one hand on the emergency stop.

> 💡 Name your waypoints with fixed names such as Above_Pick, Pick, Place, Home.

## Practical assignment (Document type 2 / Template B) — Week 7: Certification exam (4 hours, 240 minutes)

**Level:** 3-4 · Estimated duration: 240 min (lesson day) / 100-150 min (practice blocks)

Today you will work on: certification exam (4 hours, 240 minutes).
Expected result: the candidate completes the full certification exam: theory, troubleshooting, and a practical case.

> **Mandatory preparation:** Mandatory preparation: before starting, write a short work plan naming your motion trajectory (waypoints), motion commands, and safety measures.

### Practical case 1: Machine Tending

Loading and unloading a simulated CNC machine or press.

**Mandatory core elements:** I/O handshaking (incoming ready signal and outgoing start signal), safe entry and exit via Move Line, return to Home.

### Assignments (progressive practice bank)
1. C7.1 Exam preparation: summary of the theory domains
2. C7.2 Find-the-Error dry run with the four fault classes

> See Information sheet: Safe startup and shutdown. See Information sheet: Manual motion (jogging and Hand guiding).

### Checkpoints


|  | Achieved | Partly | Not achieved |
|---|---|---|---|
| Workspace inspected and emergency stop tested before Servo On | ☐ | ☐ | ☐ |
| Waypoints clearly named (Home, Pick, Place) | ☐ | ☐ | ☐ |
| Program simulated / tested at low speed first | ☐ | ☐ | ☐ |
| Motion validation correct (MoveL without blending at the pick point) | ☐ | ☐ | ☐ |
| Safe shutdown according to procedure | ☐ | ☐ | ☐ |

## Assessment rubric (Template D) — Week 7 — assessment

> **Knock-out criteria: all safety knock-out criteria must be met without exception: workspace inspected; emergency stop verified before motor power; no unauthorized modification of safety settings; safe shutdown per procedure.**

| Competency | 1 | 2 — Level 3 | 3 — Level 4 |
|---|---|---|---|
| System setup & calibration | Needs repeated guidance; gripper, TCP, payload, or wiring are configured incorrectly or sloppily. | Mounts the gripper, wires basic I/O properly, and calibrates TCP and payload independently and accurately. | Demonstrably optimizes workspace layout and Center of Gravity settings for ergonomics, reach, and cycle efficiency. |
| Programming & process logic | Program runs unstably; loops, frames, or I/O blocks contain errors or lack structure. | Combines MoveJ/MoveL, loops, and working I/O control accurately into a stable, safe production cycle. | Builds modularly with clean subroutines, clear naming, deliberate blending, and active error handling. |
| Troubleshooting & diagnostics | Loses overview, guesses randomly, or deletes parts of the existing program without analysis. | Uses the manual and structured checks to locate and fix the fault within the allotted time. | Directly analyzes raw data (I/O monitor, fault logs, measurements), isolates the root cause purposefully, and identifies preventive measures. |
| Safety, documentation & craftsmanship | Works messily, cannot explain technical decisions, or fails to deliver a usable program handover. | Works with discipline and safety, uses clear folder and task names, and explains system operation clearly to a colleague. | Delivers a complete, hand-over-ready cell with clean inline documentation and substantiates choices to the client. |

## Examination sheet (Document type 3 / Template C) — Certification exam — week 7

**Total duration:** 240 min

### Component 1: Theory examination (30 min)

- Industrial robots vs. cobots and the core functions of all system components
- Safe startup, shutdown, and safety standards (ISO 10218-1/2:2025, the four collaborative modes, emergency stop vs. Protective Stop, risk assessment)
- Kinematics and coordinate systems (J1-J6, X/Y/Z, TCP, payload, Base, Tool, and User frames)
- Motion control and manual operation (jogging, hand guiding, Move Joint, Move Line, Move Circle, blending, singularity)
- Programming logic and structure (Wait, Repeat, If/Else, subroutines, variables, tidy program management)
- Connectivity and diagnostics (24V DC digital and analog I/O, sensors, machine handshaking, systematically resolving stops)

**Extra for NLQF Level 4:** coordinate transformations, error-handling logic, digital simulation, foundational industrial communication protocols

### Component 2: Find the Error / Troubleshooting (20-30)

**Fault classes (1) hardware- en I/O-fouten, (2) kalibratie- en instelfouten, (3) bewegings- en veiligheidsfouten, (4) logische programmafouten**

**Grading:** Level 3: resolves the fault methodically using the manual and standard checks. Level 4: reads raw diagnostic data (I/O monitor, fault log) directly, isolates the root cause without deleting existing code, and validates the fix.

### Component 3: Practical case examination (180 min)

**Case 1 — Machine Tending:** Loading and unloading a simulated CNC machine or press.

*Mandatory core elements:* I/O handshaking (incoming ready signal and outgoing start signal), safe entry and exit via Move Line, return to Home.

**Exam shell (applied to every issued exam sheet):**
- Industrial brief with concrete product specifications
- Available hardware and constraints
- Mandatory preparation check (work plan and safety analysis)
- Functional final demonstration of a continuous production cycle
- Oral explanation by the candidate justifying safety and programming choices

### Knock-out criteria (immediate fail)
- Workspace not demonstrably inspected and cleared prior to operation
- Emergency stop functionality not verified before engaging motor power
- Safety settings bypassed or modified without authorization
- System not shut down safely according to procedure

### Pass rules
- **NLQF 3:** At least score 2 on every single competency.
- **NLQF 4:** Score 3 on at least three of the four competencies (mandatorily including Programming & Process Logic and Troubleshooting & Diagnostics), and no competency below 2.

**Exam alignment:** Complete examination blueprint including knock-out criteria and rubric (Track 2, section 2.4).

---

*Composed with the Cobot Course Composer from the three tracks (technology - NLQF pedagogy - SMEOT house style). Missing machine data always appears as a [REVIEW_MARKER], never as invented facts.*
