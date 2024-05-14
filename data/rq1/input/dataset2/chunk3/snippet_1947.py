#Source: https://stackoverflow.com/questions/62054195/python-name-error-when-calling-a-previously-defined-function-in-the-same-class
class OurHandler(FileSystemEventHandler):

    # def __init__(self, source):
    #     self.source = source

    def move_epub(self):
        for i in os.listdir(self.source):
            print("Hello World")

    def on_any_event(self, event):
        print(f"\n\n{self}\t\t {event}\n\n")
        move_epub()

track_this_folder = "pathname"
a = OurHandler()
observer = Observer()
observer.schedule(a, track_this_folder)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()