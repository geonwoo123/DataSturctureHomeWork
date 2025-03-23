class Array:
    def __init__(self, capacity = 10, fill = None):
        self.arr = [fill] * capacity
        self.fill = fill
        self.capacity = capacity
        self.cur = 0
        self.iter_cur = 0

    def get(self, index):
        return self.arr[index]

    def set(self, index, value):
        self.arr[index] = value

    def add(self, value):
        if self.cur >= len(self.arr):
            self.arr += [self.fill] * self.capacity
        self.set(self.cur, value)
        self.cur += 1

    def insert(self, index, value):
        self.add(None)
        i = self.cur-1
        while index<i:
            self.arr[i] = self.arr[i-1]
            i -= 1
        self.set(index, value)

    def __iter__(self):
        self.iter_cur = 0
        return self

    def __next__(self):
        if self.iter_cur < self.cur:
            value = self.arr[self.iter_cur]
            self.iter_cur += 1
            return value
        raise StopIteration        

    def __str__(self):
        return str(self.arr[:self.cur])

SIZE = 5
arr = Array(SIZE)
for i in range(5):
    arr.add(i * 5)
print(f"arr = {arr}")
for i in arr:
    print(f"elem = {i}")
for index, i in enumerate(arr):
    print(f"arr[{index}] = {i}")
sum_ = sum(arr)
print(f"sum = {sum_}")
