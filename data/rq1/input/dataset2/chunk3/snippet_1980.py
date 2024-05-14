#Source: https://stackoverflow.com/questions/66145096/typeerror-listen-missing-1-required-positional-argument-source
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import random 
import os

#Speakfunction BACKEND
print("Initializing FRIDAY")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour  >= 0 and hour<12:
        speak("Good Morning Sam I am up and running")

    elif hour>=12 and hour<18:
            speak("Good afternoon Sam I am up and running")

    else:
        speak("Good Night Sam I am up and running")    

def takecom():
    r = sr.Recognizer
    with sr.Microphone() as source:
        print("Listening ...")
        audio = r.listen(source)
    try:
        print("Recognizing")
        text = r.recognize_google(audio,language='en-in') 
        print(text)
    except Exception:
        speak("error ... ")
        print("Network error")
        return "none"
    return text

if __name__ == "__main__":
    wish()

    while True:
        query = takecom().lower()

        if wikipedia in query:
            speak("Searching details...Wait")
            query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("Opening Youtube")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak("Opening Google")
        elif 'good bye' in query:
            speak("Good bye sam")
            exit()