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
#name of AI is codakai
# Execute the AI