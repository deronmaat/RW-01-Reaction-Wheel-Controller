# RW-01 - Concept of Operations

**Project:** Reaction-Wheel Attitude Controller  
**Status:** Draft | November 2026

## Overview

I am building a small, single-axis reaction-wheel system to test how a satellite can change its orientation without pushing against anything outside itself.

A platform will rotate on a low-friction vertical bearing. A brushless motor and flywheel will be mounted on the platform. When the motor speeds up or slows down the flywheel, the platform experiences torque in the opposite direction. A controller will use an angle sensor to rotate the platform to a selected position and bring it to rest.


## How it will work

1. Turn on the system and check that the sensors and motor driver are working.
2. Set the platform's starting angle to 0 degrees.
3. Send a command for +30 degrees, -30 degrees, or 0 degrees from a computer.
4. The controller adjusts the reaction wheel to move and stop the platform at the target angle.
5. Record the platform angle, wheel speed, and controller output so the results can be compared with a simulation.

The wheel and platform will rotate about the same vertical axis. The platform's angle must be measured relative to the fixed base, not relative to the wheel.

## What I plan to build

- A simple mechanical platform with an enclosed flywheel.
- A motor-control prototype using development boards.
- A mathematical model and feedback controller in Python/C.
- A custom four-layer PCB with a microcontroller, motor driver, and sensor connections.
- A test setup for measuring accuracy, settling time, wheel speed, and reliability.

## Main limits

The first version will only control one rotational axis. It will run indoors from a nominal 12 V supply. 


## Project goal

Demonstrate repeatable 0 to +/-30 degree movements with measured results, then replace the development electronics with my own PCB. The proposed performance targets and tests are listed in [System_Requirements.md](System_Requirements.md) and [Requirements_Traceability.csv](Requirements_Traceability.csv).
