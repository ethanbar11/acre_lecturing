def func1():
    func2()


def func2():
    print(5 / 0)


class EthanException(Exception):
    pass

if __name__ == '__main__':
    raise EthanException()