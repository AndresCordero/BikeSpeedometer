from pynput import keyboard
import time

wheel_cycles = 0
distance_per_cycle = 2.1
last_press_time = None;

def main():
    print("Presiona SPACE para contar vueltas, ESC para salir.")
    
    # Start listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Esperar hasta que se presione ESC

    # Distance mesurement
    distance = wheel_cycles * distance_per_cycle
    print(f'\nThe distance traveled is {distance} meters')

#Getting data from keyboard (wheel cycle simulaton)
def on_press(key):
    global wheel_cycles, last_press_time;
    
    if key == keyboard.Key.space:
        current_time = time.time()

        if last_press_time is not None:
            elapsed_time = current_time - last_press_time
            velocity = distance_per_cycle / elapsed_time
            print(f"SPACE has been pushed! Total cycles: {wheel_cycles} -- Velocidad: {velocity} m/s")

        else:  
            print(f"SPACE! Vueltas: {wheel_cycles + 1} -- Velocidad: N/A (primera vuelta)")   

        last_press_time = current_time    
        wheel_cycles += 1

    elif key == keyboard.Key.esc:
        print("exiting...")
        return False  # stop listener


if __name__ == "__main__":
    main()
