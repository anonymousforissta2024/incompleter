#Source: https://stackoverflow.com/questions/31884175/multiprocessing-typeerror-int-object-is-not-iterable
def main(i):
    global urlDepth
    global row
    global counter
    urlDepth = []
    row = 0
    counter = 0
    login(i)
    crawler(MENU_URL)


if __name__ == '__main__':
    workers = 2
    processes = []
    for p_number in range(workers):
        p = Process(target=main, args=p_number)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()