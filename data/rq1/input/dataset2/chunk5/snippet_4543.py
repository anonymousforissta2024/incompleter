#Source: https://stackoverflow.com/questions/60939090/why-do-i-keep-getting-a-attributeerror-nonetype-object-has-no-attribute-lowe
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pythoncom

print("Initializing Karren")

MASTER = "Bob"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)


   # speak("I am Karren. How may I assist you?") # deliberately on not included for now

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, Language = 'en-uk')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Sorry i didn't catch that...")
        query = None
    return query 

speak("Initializing Karren...")
wishMe()
query = takeCommand()


if 'wikipedia' in query.lower():
    speak("Searching wikipedia")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak(results)