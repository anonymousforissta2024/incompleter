#Source: https://stackoverflow.com/questions/46080156/python-multiprocessing-typeerror-pickling-an-authenticationstring-object-is-d
import multiprocessing

class TestCrawler:
    def __init__(self):
        self.m = multiprocessing.Manager()
        self.queue = self.m.Queue()
        for i in range(50):
            self.queue.put(str(i))
        self.pool = multiprocessing.Pool(6)



    def mainloop(self):
        self.process_next_url(self.queue)

        while True:
            self.pool.map(self.process_next_url, (self.queue,))                

    def process_next_url(self, queue):
        url = queue.get()
        print(url)


c = TestCrawler()
c.mainloop()