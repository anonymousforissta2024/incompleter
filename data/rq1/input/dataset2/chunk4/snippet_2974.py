#Source: https://stackoverflow.com/questions/76676400/python-thread-typeerror-main-generate-num-argument-after-must-be-an-i
from threading import Thread, Event
import queue
import random

def generate_num(e):
    print('e',e.is_set())
    while True:
        if e.is_set():
            print('g', random.randint(15, 20))
        else:
            print('g', 0)
    
def start_generating():
    i = 0
    e = Event()
    r_thread = Thread(target=generate_num, args=(e), daemon=True).start()
    print('starting')

    while True:
        print('i', i)
        if i %5 == 0:
            e.set()
        if i ==12:
            exit(0)
        i+=1

start_generating()