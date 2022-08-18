import threading


class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        self.lock.acquire()
        self.count += 1
        self.lock.release()


counter = Counter()
t1 = threading.Thread(target=counter.increment)
t2 = threading.Thread(target=counter.increment)
t1.start()
t2.start()
