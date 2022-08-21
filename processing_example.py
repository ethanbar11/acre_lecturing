from multiprocessing import Process
from threading import Thread


x = 5


def worker():
    global x
    x = x + 1
    print('worker', x)


if __name__ == '__main__':
    p = Thread(target=worker)
    p.start()
    p.join()
    print(x)
