#Source: https://stackoverflow.com/questions/44144584/typeerror-cant-pickle-thread-lock-objects
from multiprocessing import Process
from queue import Queue
import logging

def main():
    x = DataGenerator()
    try:
        x.run()
    except Exception as e:
        logging.exception("message")


class DataGenerator:

    def __init__(self):
        logging.basicConfig(filename='testing.log', level=logging.INFO)

    def run(self):
        logging.info("Running Generator")
        queue = Queue()
        Process(target=self.package, args=(queue,)).start()
        logging.info("Process started to generate data")
        Process(target=self.send, args=(queue,)).start()
        logging.info("Process started to send data.")

    def package(self, queue): 
        while True:
            for i in range(16):
                datagram = bytearray()
                datagram.append(i)
                queue.put(datagram)

    def send(self, queue):
        byte_array = bytearray()
        while True:
            size_of__queue = queue.qsize()
            logging.info(" queue size %s", size_of_queue)
            if size_of_queue > 7:
                for i in range(1, 8):
                    packet = queue.get()
                    byte_array.append(packet)
                logging.info("Sending datagram ")
                print(str(datagram))
                byte_array(0)

if __name__ == "__main__":
    main()