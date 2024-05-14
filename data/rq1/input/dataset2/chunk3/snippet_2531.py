#Source: https://stackoverflow.com/questions/66467222/typeerror-int-object-is-not-callable-unique-problem-in-python3
from fuzzywuzzy import fuzz
import sys
#sys.path.insert(0, '/home/pi/AIY-voice-kit-python/src/aiy/voice')
from aiy.voice import tts
#import tts
tts.say('Harry activated')
from os import environ, path
import os
#sys.path.insert(0, '/home/pi/AIY-voice-kit-python/src/examples/voice')
#from __init__ import LiveSpeech, get_model_path
from pocketsphinx import LiveSpeech, get_model_path
model_path = get_model_path()
print("active")
speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'en-us'),
    lm=os.path.join(model_path, 'en-us.lm.bin'),
    dic=os.path.join(model_path, 'cmudict-en-us.dict')
)

for phrase in speech:
    p = str(phrase)
    print(p)
    r1 = (fuzz.ratio(p,"harry"))
    print(r1)
    ri = int(r1)
    if ri > 60():
        print("you said my name")