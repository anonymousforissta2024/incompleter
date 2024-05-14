#Source: https://stackoverflow.com/questions/68341487/python-keyboard-module-error-typeerror-nonetype-object-is-not-callable
import keyboard

pressed = ""

def on_key_press():
    print("Key pressed.")
    global pressed
    # Took me 1 hour to figure out this.
    if charset.chars.__contains__(keyboard.read_key()):
        print("processing slangs...")
        print("*process*")
    else:
        print("registered key.")
        pressed += keyboard.read_key()
    print(pressed)

keyboard.on_press(on_key_press())
keyboard.wait()