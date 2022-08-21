class MyNumbers:
    def __init__(self):
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


numbers = MyNumbers()
for i in numbers:
    print(i)
