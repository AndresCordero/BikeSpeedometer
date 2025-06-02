from pynput import keyboard
import time

wheel_cycles = 0
distance_per_cycle = 2.1
last_press_time = None;
initial_time = None
ending_time = None

def main():
    print("Press SPACE to pedal and press ESC to exit.")
    
    # Start listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Esperar hasta que se presione ESC

    # Distance mesurement
    distance = round((wheel_cycles * distance_per_cycle) , 2)

    #Velocity Average
    total_time = ending_time - initial_time
    average_vel = round ((distance / total_time) , 2)

    print(f'\nDistance traveled in this trip: {distance} meters')
    print(f'The average speed was: {average_vel} m/s')





#Getting data from keyboard (wheel cycle simulaton)
def on_press(key):
    global wheel_cycles, last_press_time, initial_time, ending_time;
    
    if key == keyboard.Key.space:
        current_time = time.time()

        #Setting initial time to calculate average
        if initial_time is None:
            initial_time = current_time

        if last_press_time is not None:
            elapsed_time = current_time - last_press_time
            velocity = round((distance_per_cycle / elapsed_time), 2)
            distance_so_far = round(distance_per_cycle * wheel_cycles)
            print(f"Total cycles: {wheel_cycles} -- Distance: {distance_so_far} meters -- Velocity: {velocity} m/s")
        else:  
            print(f"SPACE! Vueltas: {wheel_cycles + 1} -- Velocidad: N/A (first cycle)")   

        last_press_time = current_time    
        wheel_cycles += 1

    elif key == keyboard.Key.esc:
        ending_time = time.time()
        print("exiting...")
        return False  # stop listener

if __name__ == "__main__":
    main()
