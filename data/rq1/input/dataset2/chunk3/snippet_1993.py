#Source: https://stackoverflow.com/questions/62438408/sharing-a-list-between-processes-raises-the-error-attributeerror-forkawareloc
import multiprocessing


def test(c):
    c[0] = 1


class TestClass:
    def __init__(self):
        with multiprocessing.Manager() as manager:
            colorcodes = manager.list()
            p = multiprocessing.Process(target=test, args=(colorcodes,))
            p.start()
            p.join()
        print(colorcodes[0])


if __name__ == '__main__':
    TestClass()