#Source: https://stackoverflow.com/questions/56824119/getting-file-not-found-error-when-trying-to-load-eel-js
import eel

class GUI:
    def __init__(self):
        eel.init("web")
        eel.start("main.html", block = False)
        eel.sleep(5)