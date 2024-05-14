#Source: https://stackoverflow.com/questions/76245831/how-do-i-resolve-error-nameerror-name-stream-is-not-defined-pyaudio-python
global stream
stream = None


global paused
paused = False    # global to track if the audio is skipped
def on_turn(pin):
    global paused
    global stream
    if stream is not None and stream.is_active():   # time to pause audio
        print ('audio skipped')
        paused = False


GPIO.add_event_detect(27, GPIO.BOTH, callback=on_turn, bouncetime=200) #this event is when the dial is turning

def bigcheck():
    pick_up_state = GPIO.input(22)
    old_pick_up_state = 1
    if pick_up_state != old_pick_up_state:
        if pick_up_state == 1: #the handset is picked up!
            print("handset lifted")
            is_picked_up = True
            old_pick_up_state = 1
        else: #the handset is put down
            print("handset down")
            is_picked_up = False
            global still_picked_up
            still_picked_up = False
            global has_recorded
            has_recorded = False
            global has_recorded_options
            has_recorded_options = False
            play_menu = True
            old_pick_up_state = 0
            call(["amixer", "-D", "pulse", "sset", "Master", "100%+"])
            return


c=0 
last = 1

def count(pin):
    global c 
    c = c + 1
#this c and count script is used in translating the dialed number

while True:
    
    pick_up_state = GPIO.input(22)
    if pick_up_state != old_pick_up_state:
        if pick_up_state == 1: #the handset is picked up!
            print("handset lifted")
            is_picked_up = True
            old_pick_up_state = 1
        else: #the handset is put down
            print("handset down")
            is_picked_up = False
            still_picked_up = False
            has_recorded = False
            play_menu = True
            old_pick_up_state = 0
            call(["amixer", "-D", "pulse", "sset", "Master", "100%+"])

    if is_picked_up: #plays the intro upon handset pickup
        sleep(1)
        call(["amixer", "-D", "pulse", "sset", "Master", "100%+"])
        intro = AudioSegment.from_wav("/home/brian/Music/Rotary_Recordings/Intro.wav")
        print('playing intro')
        play(intro)
        still_picked_up = True
        is_picked_up = False
        paused = True