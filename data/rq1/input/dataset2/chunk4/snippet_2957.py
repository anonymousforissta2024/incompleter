#Source: https://stackoverflow.com/questions/63417844/attributeerror-module-test-has-no-attribute-myfunc
import test
class myclass:
    ...
    def mainfunc(self):
        test.myfunc()
    ...
start = myclass()
start.mainfunc()