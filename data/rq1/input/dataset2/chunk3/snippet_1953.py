#Source: https://stackoverflow.com/questions/57134703/why-this-reload-fails-with-nameerror-name-xxx-is-not-defined
#file: attempt2.py
import sys
from time import sleep
from importlib import reload
from foo_module import foo  # <-- import specific item only

#Lets see if the module is loaded
print(sys.modules['foo_module']) 

while True:
    foo()

    #simulate a delay or a condition by when foo_module would have changed
    sleep(2)

    #try to reload foo_module to get the latest
    reload(foo_module) #FAILS !