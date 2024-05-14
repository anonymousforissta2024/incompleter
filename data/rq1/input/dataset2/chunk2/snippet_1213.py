#Source: https://stackoverflow.com/questions/55770064/python-typeerror-listen-missing-1-required-positional-argument-self
import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random

speech = sr.Recognizer
speech.energy_threshold = 4000

greeting_dictionary = {'sup' : 'whats good','ay' : 'wassup'}

def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    play_sound(mp3)

def read_input():
    voice_text = ''
    print('Listening...')
    with sr.Microphone() as source:
        audio = speech.listen(source=source, timeout=10, phrase_time_limit=5) #The error is here
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network error')
    except sr.WaitTimeoutError:
        pass
    return voice_text

if __name__ == '__main__':

    playsound('mp3/dawg/greet.mp3')

    while True:

        input = read_input()

        print('You: '.format(input))

        if 'hello' in input:
            continue
        elif 'open' in input:
            os.system('explorer ~/Desktop {}'.format(input.replace('Open ', '')))
        elif 'bye' in input:
            exit()