#Source: https://stackoverflow.com/questions/57854166/nameerror-name-lock-is-not-defined
def send_request(data):
    global lock
    lock.acquire()
    print(data)
    lock.release()

if __name__ == '__main__':
    data_list = ['data1', 'data2', 'data3']
    lock = multiprocessing.Lock()
    pool = multiprocessing.Pool(3)

    pool.map(send_request, data_list)
    pool.close()
    pool.join()