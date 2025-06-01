from pynput import keyboard
import time

def on_press(key):
    if key == keyboard.Key.space:
        print("¡Se presionó SPACE!")
    elif key == keyboard.Key.esc:
        print("Saliendo...")
        # Detener el listener para salir del programa
        return False



with keyboard.Listener(on_press=on_press) as listener:
    print("Presiona SPACE para ver un mensaje, ESC para salir.")
    listener.join()

