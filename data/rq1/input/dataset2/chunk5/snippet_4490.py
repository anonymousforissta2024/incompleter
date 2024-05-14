#Source: https://stackoverflow.com/questions/61559860/getting-typeerror-module-object-is-not-callable
import multiprocessing as mp
import time as t

def do_something():
       t.sleep(1)
       print("Done Sleeping")

p1 = mp.process(target=do_something)
p2 = mp.process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()