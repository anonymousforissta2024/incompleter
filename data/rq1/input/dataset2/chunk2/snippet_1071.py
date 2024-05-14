#Source: https://stackoverflow.com/questions/60586521/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-while
from pysndfx import AudioEffectsChain
import os

in_file = os.getcwd() + "\\" + "a.mp3"
in_file = in_file.replace("\\", "//")#tried many things here, tried to it without any replacing

if os.path.isfile(in_file):
    print("fileyes") #This returns true
else:
    print("not a file")
print(in_file)


fs = 44100
fx = (AudioEffectsChain().
    reverb().
    delay().
    phaser()
)

fx(in_file,"apro.mp3")