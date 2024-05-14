#Source: https://stackoverflow.com/questions/76245831/how-do-i-resolve-error-nameerror-name-stream-is-not-defined-pyaudio-python
import RPi.GPIO as GPIO
# ... (other imports)

# Define global variable 'stream'
stream = None

# ... (other code)

def on_turn(pin):
    global paused
    global stream

    if stream is not None and stream.is_active():
        print('Audio skipped')
        paused = False

# ... (other code)

GPIO.add_event_detect(27, GPIO.BOTH, callback=on_turn, bouncetime=200)

# ... (rest of the code)