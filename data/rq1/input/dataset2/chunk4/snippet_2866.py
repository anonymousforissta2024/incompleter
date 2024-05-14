#Source: https://stackoverflow.com/questions/8041625/multithreading-attempt-using-python-3-2-2-attributeerror-str-object-has-no
import threading

class AsyncScript(threading.Thread):
    def __init__(self, s):
        threading.Thread.__init__(self)
        self.script = s
    def run(self):
        print("This would run script " + self.script)

AsyncScript("sample script path string").start()