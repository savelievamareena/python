class Tribonacci:
    def __init__(self, limit):
        self.prev_prev = 0
        self.prev = 1
        self.cur = 1
        self.limit = limit
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.limit:
            result = self.prev_prev
            self.prev_prev, self.prev, self.cur = self.prev, self.cur, self.prev_prev + self.prev + self.cur
            self.i += 1
            return result
        else:
            raise StopIteration


for i in Tribonacci(32):
    print(i)
