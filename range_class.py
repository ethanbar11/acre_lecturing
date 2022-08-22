class MyRange:
    def __init__(self, end, start=0, step=1):
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        # Saving the current value aside.
        current = self.current
        if abs(current) >= abs(self.end):
            raise StopIteration()
        else:
            self.current += self.step
            return current
