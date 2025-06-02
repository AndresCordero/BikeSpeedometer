# 🚴‍♂️ BikeSpeeddometer.py

A Python script that simulates a bicycle speedometer by tracking virtual wheel rotations.

Each time you press the **spacebar (`SPACE`)**, the program simulates a full wheel rotation. It calculates and displays:

- 🚀 **Instantaneous speed** in meters per second (m/s)
- 📍 **Distance traveled** in meters
- 📊 **Average speed** (at the end of the session)

---

## 📦 Requirements

- Python 3.6+
- [`pynput`](https://pypi.org/project/pynput/) module

Install the dependency:

pip install pynput

### ⚙️ How It Works
Press the SPACE key to simulate a wheel cycle.

The program calculates:

Velocity based on the time between key presses.

Distance by multiplying total cycles by wheel circumference.

Press ESC to end the simulation and get a summary.

### 🧠 Calculation Details

Distance per cycle: 2.1 meters (modifiable in code)

Speed = distance_per_cycle / time_between_cycles (in m/s)

Total distance = wheel_cycles * 2.1 (in meters)

Average speed = total_distance / total_time (in m/s)



### 🖥️ How to Run

- python BikeSpeeddometer.py

Then:
Press SPACE to simulate each wheel rotation.

Press ESC to finish and view the summary.



### Sample Output:

Press SPACE to pedal and press ESC to exit.
SPACE! Vueltas: 1 -- Velocidad: N/A (first cycle)
Total cycles: 1 -- Distance: 2 meters -- Velocity: 4.2 m/s
Total cycles: 2 -- Distance: 4 meters -- Velocity: 5.9 m/s
...

exiting...

Distance traveled in this trip: 12.6 meters
The average speed was: 2.87 m/s
