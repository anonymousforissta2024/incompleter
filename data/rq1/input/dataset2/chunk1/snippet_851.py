#Source: https://stackoverflow.com/questions/55984129/attributeerror-could-not-find-pyaudio-check-installation-cant-use-speech-re
def hear():
    import speech_recognition as sr
    ear = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("listening...")
        audio = ear.listen(sourse)
        try:
            text = ear.recognize_google(audio)
            print(text)
        except:
            print("i didn't get that...")

hear()