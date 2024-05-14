#Source: https://stackoverflow.com/questions/51110863/mutagen-python-filenotfounderror-handling
from mutagen.easyid3 import EasyID3

def getGenre(filename):
    try:
        audiofile = EasyID3(filename)
        #No genre
        if not audiofile['genre']:
            return None
        else:
            return audiofile['genre']

    except (FileNotFoundError,IOError):
        print("Wrong file or file path")


getGenre("xyz.mp3")