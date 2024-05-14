#Source: https://stackoverflow.com/questions/68231990/filenotfounderror-errno-2-no-such-file-or-directory-interview-part2-mp3
from os import path
from pydub import AudioSegment

#files
src = 'Interview-part2.mp3'
dst = 'Interview-part2.wav'
    
#Convert mp3 to wav
sound = AudioSegment.from_mp3(src)