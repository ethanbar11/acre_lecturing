import threading

x = 5


def worker():
    global x
    print(x)
    x = x + 1


def one_to_hundred():
    for i in range(100):
        print(i)


for i in range(1000):
    t = threading.Thread(target=worker)
    t.start()
