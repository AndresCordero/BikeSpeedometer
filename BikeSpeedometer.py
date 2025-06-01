from pynput import keyboard
import time

wheel_cycles = 0
distance_per_cycle = 2.1  

def main():
    print("Presiona SPACE para contar vueltas, ESC para salir.")
    
    # Start listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Esperar hasta que se presione ESC

    # Distance mesurement
    distance = wheel_cycles * distance_per_cycle
    print(f'\nThe distance traveled is {distance} meters')



#Getting data from keyboard
def on_press(key):
    global wheel_cycles

    if key == keyboard.Key.space:
        wheel_cycles += 1
        print(f"SPACE has been pushed! Total cycles: {wheel_cycles}")

    elif key == keyboard.Key.esc:
        print("exiting...")
        return False  # stop listener


if __name__ == "__main__":
    main()
