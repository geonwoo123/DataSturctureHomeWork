class Array:
    def __init__(self,capacity = 10,fill = None):
        self.arr = [fill] * capacity
        self.cur = 0

    def get(self, index):
        return self.arr[index]

    def set(self, index, value):
        self.arr[index] = value

    def add(self, value):
        self.arr[self.cur] = value
        self.cur += 1

    def __str__(self):
        return str(self.arr)
    
SIZE = 10
arr = Array(SIZE)
print(arr)
arr.add(1)
arr.add(2)
arr.add(3)
arr.add(4)
arr.add(5)
print(f"arr = {arr}")
for i in range(5, SIZE):
    arr.add(i * 10)
print(f"arr = {arr}")