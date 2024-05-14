#Source: https://stackoverflow.com/questions/58365301/how-do-i-fix-typeerror-dispatch-missing-1-required-positional-argument-even
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import json

event = None

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = '/Users/Balduin/Pictures/Florens1019'
folder_destination = '/Users/Balduin/Pictures/Florens1019/raw-jpeg'
event_handler = MyHandler
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join