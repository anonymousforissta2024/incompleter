#Source: https://stackoverflow.com/questions/55657722/python-multiprocessing-errors-when-wrapped-inside-a-function-attributeerror-ca
from multiprocessing import Pool
import time

def test():
  def _foo(my_number):
    square = my_number * my_number
    time.sleep(1)
    return square 

  with Pool() as p:
    r = list(p.imap(_foo, range(30)))
  print(r)

test()