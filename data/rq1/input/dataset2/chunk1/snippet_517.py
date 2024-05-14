#Source: https://stackoverflow.com/questions/63428694/how-to-fix-visual-studio-attributeerror-engine-object-has-no-attribute-getp
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__=="__main__":
    speak("hello world")