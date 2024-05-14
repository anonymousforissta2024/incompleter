#Source: https://stackoverflow.com/questions/55507226/attributeerror-module-pyaudio-has-no-attribute-version
import speech_recognition as sr 

r = sr.Recognizer()
with sr.Microphone() as source:
     print('speak say anything')
     audio = r.listen(source)
     try:
        text = r.recognize_google(audio)
        print("you said:{}".format(text))
     except:
            print("cant recognize")