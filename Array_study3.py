class Array:
    def __init__(self, capacity = 10, fill = None):
        self.arr = [fill] * capacity
        self.fill = fill
        self.capacity = capacity
        self.cur = 0

    def get(self, index):
        return self.arr[index]

    def set(self, index, value):
        self.arr[index] = value

    def add(self, value):
        if self.cur >= len(self.arr):
            self.arr += [self.fill] * self.capacity
        self.set(self.cur, value)
        self.cur += 1

    def __str__(self):
        return str(self.arr)

SIZE = 5
arr = Array(SIZE)
print(f"arr = {arr}")
for i in range(SIZE):
    arr.add(i)
print(f"arr = {arr}")
arr.add(5)
print(f"arr = {arr}")
arr.add(6)
print(f"arr = {arr}")       