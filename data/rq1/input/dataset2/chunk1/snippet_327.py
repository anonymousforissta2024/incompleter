#Source: https://stackoverflow.com/questions/20826430/start-method-on-thread-fails-with-typeerror
class TimerQueue(threading.Thread):

    def __init__(self, qyoo, kwargs):
        threading.Thread.__init__(self)
        self.queue = qyoo
        self.work = kwargs
        self.start = ceiling(time.time())
        self.times = kwargs.keys()


    def run(self):
        while True:
            for t in self.times:
                if ceiling(time.time()) - self.start == t:
                    logger.debug("adding {} to the queue".format(self.work[t]))
                    self.queue.put(self.work[t])
            time.sleep(1)

if __name__ == "__main__":
    input_queue = queue.Queue()
    tt = TimerQueue(input_queue, time_url_dict)
    tt.start()