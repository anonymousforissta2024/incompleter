#Source: https://stackoverflow.com/questions/53550866/multiprocessing-typeerror-cant-pickle-thread-lock-objects
class class_one(object):
    def __init__(self):
        self.var = {}
        self.list = []
        self.get()
    def get_result(self, varam):
        q.put(A(varam))
    def get(self):
        for i in [6,7,8,9]:
            self.list.append(pool.apply_async(self.get_result, (i, )))
            #p = Process(target=self.get_result, args=(i, ))
            #process_list.append(p)
            #p.start()
        pool.close()
        pool.join()

if __name__ == '__main__':
    freeze_support()
    process_num =2
    process_list = []
    g = class_one()

    for i in g.list:
        print(i.get())
    # for j in process_list:
    #     j.join()
    # print(q.qsize())
    # if q.empty():
    #     print("error")
    # while (not q.empty()):
    #     print(q.get().varam)
    #     g.var[q.get().varam]=q.get()