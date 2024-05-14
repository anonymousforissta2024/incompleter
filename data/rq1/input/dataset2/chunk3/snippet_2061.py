#Source: https://stackoverflow.com/questions/73832064/sharing-dictionary-over-multiprocesses-typeerror-cannot-pickle-weakref-objec
from multiprocessing import Process, Manager

class Storage():
    def __init__(self,manager):
        self.manager = manager
        self.orderbooks = self.manager.dict()

    def store_value(self,el):
        self.orderbooks[el[0]] = el[1]

    def write(self,el:list):
        p = Process(target=self.store_value,args=(el,))
        p.start()


if __name__ == '__main__':

    manager=Manager()
    book1 = Storage(manager)
    book1.write([0,1])