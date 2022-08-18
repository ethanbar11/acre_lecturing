import threading
import time


class ThreadSafeQueue:
    def __init__(self):
        self.lst = []
        self.lock = threading.Lock()
        self.empty_lock = threading.Lock()

        # Locking the empty lock at the start of creating this class.
        self.empty_lock.acquire()

    def push(self, item):
        # Acquiring this lock for thread safety.
        self.lock.acquire()

        # I'm releasing the empty lock because now I know there is at least one item in the queue.
        if len(self.lst) == 0:
            self.empty_lock.release()

        self.lst.append(item)

        self.lock.release()

    def pop(self):
        if len(self.lst) == 0:
            print('Queue is empty')
            return None
        self.lock.acquire()
        item = self.lst.pop(0)
        self.lock.release()
        return item

    # def __len__(self):
    #     self.lock.acquire()
    #     length = len(self.lst)
    #     self.lock.release()
    #     return length

    def blocking_pop_busy_wait(self):
        # Busy waiting
        item = None
        while True:
            if len(self) != 0:
                self.lock.acquire()
                item = self.pop()
                self.lock.release()
                break
            time.sleep(0.01)
        return item

    def block_pop(self):
        self.lock.acquire()
        if len(self.lst) > 0:
            item = self.lst[0]
            del self.lst[0]
        else:
            self.lock.release()
            self.empty_lock.acquire()
            self.lock.acquire()
            item = self.lst[0]
            del self.lst[0]
            self.empty_lock.release()
        # Checking if the queue is empty.
        if len(self.lst) == 0:
            self.empty_lock.acquire()
        self.lock.release()
        return item


queue = ThreadSafeQueue()


def pop_and_print():
    global queue
    x = queue.block_pop()
    print(x)


if __name__ == '__main__':
    t = threading.Thread(target=pop_and_print)
    t.start()

    # time.sleep(5)
    queue.push(500)
    t.join()
    print('Yay')
