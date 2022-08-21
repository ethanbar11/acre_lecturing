class MyNumbers:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == 1:
            return self.a
        elif self.count == 2:
            return self.b
        elif self.count == 3:
            return self.c
        else:
            raise StopIteration()
#

numbers = MyNumbers()
print(set(numbers))
# for i in numbers:
#     print(i)
