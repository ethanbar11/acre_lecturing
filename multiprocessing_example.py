from multiprocessing import Queue, Process


def push_to_queue_and_finish(queue):
    # Some training of your model
    pass

    queue.put(5)


if __name__ == '__main__':
    queue = Queue()
    n = 10
    for i in range(n):
        p1 = Process(target=push_to_queue_and_finish, args=(queue,))
        p1.start()

    for i in range(n):
        x = queue.get()
        print(x)


