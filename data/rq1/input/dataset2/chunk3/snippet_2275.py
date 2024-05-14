#Source: https://stackoverflow.com/questions/65547733/attributeerror-engine-object-has-no-attribute-runandwait
import pyttsx3 as tts

def speak(text):
    engine = tts.init("sapi5")
    engine.say(text)
    engine.runandwait()

speak('Hello user this is a test message.')