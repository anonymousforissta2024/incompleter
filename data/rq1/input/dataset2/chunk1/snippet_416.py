#Source: https://stackoverflow.com/questions/34733871/attributeerror-recognizer-object-has-no-attribute-recognize
import pyaudio
import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold=4000

with sr.Microphone() as source:
    audio = r.listen(source)

try:
    print("Speech was:" + r.recognize(audio))
except LookupError:
    print('Speech not understood')