#Source: https://stackoverflow.com/questions/57134703/why-this-reload-fails-with-nameerror-name-xxx-is-not-defined
#file: attempt1.py
import sys
from time import sleep
from importlib import reload
import foo_module  # <-- import the entire module

print(sys.modules['foo_module']) #Lets see if the module is loaded
while True:
    foo_module.foo()

    #simulate a delay or a condition by when foo_module would have changed
    sleep(2)

    #should reload foo_module to get the latest
    reload(foo_module)