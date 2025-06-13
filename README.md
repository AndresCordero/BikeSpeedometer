# 🚴‍♂️ BikeSpeeddometer.py

A Python script that simulates a bicycle speedometer by tracking virtual wheel rotations.

Each time you press the **spacebar (`SPACE`)**, the program simulates a full wheel rotation. It calculates and displays:

- 🚀 **Instantaneous speed** in meters per second (km/h)
- 📍 **Distance traveled** in Kilometers
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

Distance per cycle: 2.1 meters 

Speed = distance_per_cycle / time_between_cycles 

Total distance = wheel_cycles * distance_per_cycle

Average speed = total_distance / total_time



### 🖥️ How to Run

- python BikeSpeeddometer.py

Then:
Press SPACE to simulate each wheel rotation.

Press ESC to finish and view the summary.



### Sample Output:

Press SPACE to pedal and press ESC to exit.
SPACE!
Total Cycles: 1 -- Distance: N/A  -- Velocity: N/A (first cycle)
Total cycles: 2 -- Distance: 0.0 Kms -- Velocity: 43.96 km/h
Total cycles: 3 -- Distance: 0.0 Kms -- Velocity: 47.92 km/h
Total cycles: 4 -- Distance: 0.01 Kms -- Velocity: 53.15 km/h
Total cycles: 5 -- Distance: 0.01 Kms -- Velocity: 47.75 km/h
Total cycles: 6 -- Distance: 0.01 Kms -- Velocity: 43.95 km/h
Total cycles: 7 -- Distance: 0.01 Kms -- Velocity: 56.15 km/h
Total cycles: 8 -- Distance: 0.01 Kms -- Velocity: 45.54 km/h

exiting...

Distance traveled in this trip: 0.02 Kilometers
The average speed was: 56.45 km/h
