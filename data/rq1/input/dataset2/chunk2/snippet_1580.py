#Source: https://stackoverflow.com/questions/55506571/python-nameerror-name-engine-is-not-defined-driver-not-found
import sys
print(sys.path)

import speech_recognition as sr
import pyttsx3

try:
    engine = pyttsx3.init()
except ImportError:
    print("Driver not found")
except RuntimeError:
    print("Driver fails to init")

voices = engine.getProperty("voices")

for voice in voices:
    print(voice.id)