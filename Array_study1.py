class Array:
    def __init__(self,capacity = 10,fill = None):
        self.arr = [fill]*capacity

    def get(self,index):
        return self.arr[index]

    def set(self,index,value):
        self.arr[index] = value

    def __str__(self):
        return str(self.arr)

SIZE = 5
arr = Array(SIZE)
print(arr)
arr.set(0, 10)
arr.set(2, 30)
arr.set(1, 40)
arr.set(3, 20)
arr.set(4, 50)
print(f"arr = {arr}")
for i in range(SIZE):
    arr.set(i, i * 100)
print(f"arr = {arr}")            
        