# Autonomous Rover

## About
This repository contains an early, unfinished implementation of a control system for a 6-wheeled autonomous rover. The project focuses on the low-level hardware interface between Python and an Arduino Mega, specifically managing a complex array of 12 motors (6 steering and 6 driving). The core challenge addressed here is the precise control of steering angles using potentiometer feedback to translate desired rover trajectories into specific motor rotations.

## Technical Details
The system is built on a Python-to-Arduino bridge using the `pyFirmata` protocol. The architecture is divided into two main approaches: an experimental driver set in `RoverMotorDriver` and a structured object-oriented framework in `Rough`.

**Hardware Configuration:**
- **Control Unit:** Arduino Mega (chosen for its higher number of I/O pins).
- **Actuators:** 6 steering motors and 6 driving motors.
- **Feedback:** 6 potentiometers used to determine the current angular position $\theta$ of each steering wheel.

**Key Implementations:**
- **Steering Calibration:** The system maps raw analog sensor values to a $0^\circ$ to $360^\circ$ range. It employs a calibration routine to record sensor values across a full rotation to account for hardware variance.
- **Motor Control:** Velocity is managed by manipulating the potential difference between a PWM pin and a digital pin. For a given velocity $v \in [-100, 100]$, the potential difference is scaled relative to the $5\text{V}$ supply.
- **Pin Mapping:** Due to the limited number of PWM pins on the Arduino Mega, the project utilizes a hybrid configuration where one pin per motor is a standard digital output and the other is a PWM pin, allowing for bidirectional speed control across all 12 motors.

![Arduino Mega Pinout](RoverMotorDriver/Arduino-Mega-Pinout.png)

## Execution
This project is provided as a reference for unfinished hardware control logic. To attempt to run the code, you will need an Arduino Mega flashed with StandardFirmata.

1. Install the required Python libraries:
   ```bash
   pip install pyfirmata pyserial
   ```

2. Configure the communication port:
   - In `Rough/settings.py`, update the `PORT` variable (e.g., `PORT = "COM7"` or `"/dev/ttyACM0"`).
   - In `RoverMotorDriver/Arduino through Python/main.py`, update the `portf` and `portb` variables.

3. Run the main control script:
   ```bash
   python Rough/main.py
   ```
   (Note: The `Rough` directory contains the most structured version of the codebase, while `RoverMotorDriver` contains specific calibration and testing logic).