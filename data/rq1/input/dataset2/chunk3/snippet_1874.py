#Source: https://stackoverflow.com/questions/56161667/typeerror-in-number-of-arguments-passed-to-the-target
import threading

class Example:
    def instruct(self, message_type):
        instruction_thread = threading.Thread(target=self.speak, args=message_type)
        instruction_thread.start()

    def speak(self, message_type):
        if message_type == 'send':
            print('send the message')
        elif message_type == 'inbox':
            print('read the message')


e = Example()
e.instruct('send')