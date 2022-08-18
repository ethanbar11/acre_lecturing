import threading


class Counter:
    def __init__(self):
        self.count = 0

    def add(self, value):
        new_value = self.count + value
        self.count = new_value


counter = Counter()
t1 = threading.Thread(target=counter.add, args=(50,))
t2 = threading.Thread(target=counter.add, args=(30,))

t1.start()
t2.start()
print(counter.count)

