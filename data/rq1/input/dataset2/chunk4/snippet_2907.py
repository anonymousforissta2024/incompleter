#Source: https://stackoverflow.com/questions/64903387/getting-a-filenotfounderror-errno2-when-moving-files-using-shutil-move-metho
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import shutil

file_extension = ["dmg", "jpg", "pdf", "docx", "zip", "tar", "jpeg", "mp4,", "mp3", "png"]
src = '/Users/vibhorsagar/Downloads'
path = os.listdir(src)


class Watcher:

    def __init__(self):
        self.observer = Observer()

    def run(self):
        handler = Handler()
        self.observer.schedule(handler, src, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print("Received created event - %s." % event.src_path)
            c = Cleaner()
            for i in file_extension:
                if event.src_path.endswith(i):
                    c.clean(i, event.src_path)
                else:
                    print("Error 2")

        elif event.event_type == 'modified':
            print("Received modified event - %s." % event.src_path)

        elif event.event_type == 'moved':
            print("Received moved event - %s." % event.src_path)


class Cleaner():

    def clean(self, file_type, file):
        if file_type == "dmg":
            shutil.move(file, '/Users/vibhorsagar/dmgs')

        if file_type == "jpg" or "png" or "jpeg":
            shutil.move(file, '/Users/vibhorsagar/Pictures')

        if file_type == "pdf":
            shutil.move(file, '/Users/vibhorsagar/pdfs')

        if file_type == "docx":
            shutil.move(file, '/Users/vibhorsagar/docx')


if __name__ == '__main__':
    w = Watcher()
    w.run()