# RW-01 - System Requirements

**Status:** Draft | November 2026  
**Related files:** [CONOPS.md](CONOPS.md) | [Verification Matrix](Requirements_Traceability.csv)

These are **proposed targets**, not measured results. I will check that the motor and flywheel can meet them before finalizing the design. Each requirement has a matching verification entry in the CSV.

## Test conditions

Unless otherwise stated, tests use a horizontal, enclosed platform starting at rest, with a calibrated zero angle. A standard maneuver lasts **5 seconds**. Position tests use **10 trials in each direction** (+30 and -30 degrees). Positive angles are counterclockwise when viewed from above.

## Core requirements

| ID | Requirement |
|---|---|
| **SYS-001** | The system shall accept commands for **-30, 0, and +30 degrees**. |
| **SYS-002** | The platform shall stay within **+/-2 degrees** of a +/-30 degree target during the final second of each 5-second test. |
| **SYS-003** | The platform shall settle within **+/-2 degrees** of the target by **4 seconds** and stay there until the test ends. |
| **SYS-004** | Overshoot shall not exceed **5 degrees** during a +/-30 degree maneuver. |
| **SYS-005** | The platform shall return from **+/-30 degrees to 0 degrees**, with no more than **2 degrees** of error during the final second. |
| **SYS-006** | The angle sensor shall provide timestamped readings at **100 Hz or faster**, with no gap longer than **20 ms**. |
| **SYS-007** | The attitude controller shall run at **200 Hz or faster**, with no execution gap longer than **10 ms**. |
| **SYS-008** | The system shall log target angle, actual angle, angular velocity, wheel speed, control output, and fault state at **100 Hz or faster**, with no more than **1% missing records**. |
| **SYS-009** | Wheel speed shall stay at or below **1,200 RPM** during normal maneuvers. |
| **SYS-010** | The controller shall operate from **10.8-13.2 V DC** without resetting or missing commands during normal maneuvers. |
| **SYS-011** | The **3.3 V** supply shall remain within **3.135-3.465 V** during normal operation. |
| **SYS-012** | A hardware emergency stop shall cut motor power within **100 ms**, without relying on firmware. |
| **SYS-013** | The motor driver shall be disabled within **150 ms** of losing valid platform-angle data. |
| **SYS-014** | The motor driver shall be disabled within **100 ms** of a wheel-speed reading of **1,500 RPM or higher**. Verify with simulated sensor data, not physical overspeed. |
| **SYS-015** | With the enclosure installed, a straight **12 mm probe** shall not be able to touch the flywheel through an opening. |
| **SYS-016** | The design shall include a calculated or CAD-derived **platform moment of inertia**, with a mass breakdown and units. |
| **SYS-017** | The final prototype shall use a **custom four-layer PCB** for the microcontroller and motor-control functions. |
| **SYS-018** | Total input current shall stay at or below **2.5 A** during normal maneuvers at **12 V**. |
| **SYS-019** | The system shall complete **20 minutes** of repeated 0, +30, 0, -30 degree commands without an unexpected microcontroller reset. |
| **SYS-020** | Following a motor-drive fault, the motor shall remain disabled until the operator explicitly arms it again. |

## Optional stretch goals

| ID | Requirement |
|---|---|
| **STR-001** | After a +/-5 degree disturbance around a 0 degree hold position, the platform shall return within **+/-2 degrees** in **4 seconds** and hold for **1 second** (10 trials, initial rate <=5 degrees/s). |
| **STR-002** | The system shall support both a **PD controller** and a **state-feedback controller**, with separate recorded results for the same maneuver. Both must meet SYS-002. |
| **STR-003** | An IMU-based angular-rate estimate shall have an **RMSE <=5 degrees/s** against an encoder-based reference during +/-30 degree maneuvers. |

## Notes

- These limits are subject to simulation and motor sizing. If a target changes, record why and update the verification matrix.
- A guarded rotor and a mechanical safety review are required before powered spin tests. **SYS-015 checks access only; it does not prove the enclosure can contain fragments from a failed flywheel.**
- Motor power-off does not mean the flywheel has stopped.
- No requirement is marked as passed until it has supporting test data or other documented evidence.
