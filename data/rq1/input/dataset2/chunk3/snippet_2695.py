#Source: https://stackoverflow.com/questions/76448088/python-attribute-error-not-recocgnising-object
import numpy as np
import speech_recognition as sr

# Beginning of the AI
class ChatBot():
    def __init__(self, name):
        print("----- starting up", name, "-----")
        self.name = name
# Execute the AI
if __name__ == "__main__":
    ai = ChatBot(name="Dev")
#name of AI is Dev
# Execute the AI

#speech recognition with microphone, it converts it to text
def speech_to_text(self):
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
         print("listening...")
         audio = recognizer.listen(mic)
    try:
         self.text = recognizer.recognize_google(audio)
         print("me --> ", self.text)
    except:
         print("me -->  ERROR")

def wake_up(self, text):
    return True if self.name in text.lower() else False

# Execute the AI
if __name__ == "__main__":
     ai = ChatBot(name="Dev")
     while True:
         ai.speech_to_text()

def wake_up(self, text):
    return True if self.name in text.lower() else False

from gtts import gTTS
import os
@staticmethod
def text_to_speech(text):
    print("AI --> ", text)
    speaker = gTTS(text=text, lang="en", slow=False)
    speaker.save("res.mp3")
    os.system("start res.mp3")  # windows use->start
    os.remove("res.mp3")