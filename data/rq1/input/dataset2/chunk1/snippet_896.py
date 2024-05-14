#Source: https://stackoverflow.com/questions/51842008/multiprocessing-attributeerror-imported-object-has-no-attribute-private-m
from multiprocessing import Process
from ImportedExample import Imported

class Example:
    def __init__(self, number):
        self.imported = Imported(number)

def func(example: Example):
    print(example)

if __name__ == "__main__":
    ex = Example(3)

    p = Process(target=func, args=(ex,))
    p.start()