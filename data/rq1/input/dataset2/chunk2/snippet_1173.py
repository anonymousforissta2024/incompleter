#Source: https://stackoverflow.com/questions/44036914/why-do-i-get-attributeerror-super-object-has-no-attribute-del-when-ca
class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()
        ...

    def __del__(self):
        ...
        super(type(self), self).__del__()

    def run(self):
        ...