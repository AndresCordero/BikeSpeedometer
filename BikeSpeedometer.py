from pynput import keyboard
import time

with keyboard.Listener() as listener:
    print("Presioná SPACE para simular vueltas de rueda. Ctrl+C para salir.")
    listener.join()

    