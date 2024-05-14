#Source: https://stackoverflow.com/questions/70382456/typeerror-function-takes-x-positional-argument-but-x-were-given
if __name__ == '__main__':
    pth = "/home/abd/Downloads/"
    pth2 = "/home/abd/Desktop/"

    Proc1 = multiprocessing.Process(target=watcher, args=(pth))
    Proc2 = multiprocessing.Process(target=watcher, args=(pth2))
    Proc1.start()
    Proc2.start()