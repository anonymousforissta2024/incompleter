#Source: https://stackoverflow.com/questions/61047969/how-do-i-fix-this-typeerror-listen-missing-1-required-positional-argument
import speech_recognition

recognizer = speech_recognition.Recognizer
with speech_recognition.Microphone() as source:
    print("Say something")
    audio = recognizer.listen(source)

print("Google thinks you said: ")
print(recognizer.recognize_google(audio))