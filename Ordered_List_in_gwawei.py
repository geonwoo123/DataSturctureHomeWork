class ArrayListOrdered:

    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.arr: List[Optional[int]] = [None] * capacity
        self.cur = 0

    def __repr__(self):
        return str(self.arr)

    def __len__(self):
        return self.cur

    def empty(self):
        return self.cur == 0
    
    def full(self):
        return len(self) == self.capacity
    
    def add(self, data:int):
        i = len(self)
        if self.full():
            raise IndexError("list assignment index out of range")
        while i > 0 and self.arr[i-1] > data:
            self.arr[i] = self.arr[i-1]
            i -= 1
        self.arr[i] = data
        self.cur += 1

    def search(self, data:int):
        i = 0
        answer = False
        while i < len(self) and self.arr[i] != data:
            i += 1
        return 0 <= i < len(self)    
            

    def __contains__(self, data:int):
        return self.search(data)

    def clear(self):
        i = 0
        while i < len(self):
            self.arr[i] = None
            i += 1
        self.cur = 0

    def index(self, item:int):
        i = 0
        while i < len(self):
            if self.arr[i] == item:
                return i
            i += 1
        return -1
    
    def remove(self, item:int):
        if self.empty():
            raise ValueError("f{data} is not in array")
        i = self.index(item)
        while i < self.cur -1:
            self.arr[i] = self.arr[i+1]
            i += 1
        self.arr[self.cur - 1] = None
        self.cur -= 1

    def pop(self, index:int = -1):
        if self.empty():
            raise IndexError("error")
        if index < 0:
            index += self.cur
        i = index
        value = self.arr[index]
        while i < self.cur - 1:
            self.arr[i] = self.arr[i+1]
            i += 1
        self.arr[self.cur - 1] = None
        self.cur -= 1
        return value

if __name__ == "__main__":
    arr= ArrayListOrdered()
    arr.add(5)
    arr.add(3)
    arr.add(4)
    print(arr)
    print(f"arr.pop() = {arr.pop()}")
    print(f"arr.pop(0) = {arr.pop(0)}")
    arr.add(10)
    arr.add(1)
    print(arr)
    print(f"arr.pop(-3) = {arr.pop(-3)}")
    print(arr)
    print(f"arr.pop(-1) = {arr.pop(-1)}")
    print(arr)
    arr.add(5)
    arr.add(3)
    arr.add(1)
    arr.add(2)
    print(arr)
    print(f"arr.search(10) = {arr.search(10)}")
    print(f"arr.search(2) = {arr.search(2)}")
    print(f"arr.index(3) = {arr.index(1)}")
    print(f"arr.index(5) = {arr.index(5)}")        
    print(f"arr.has(10) = {10 in arr}")
    print(f"arr.has(10) = {4 in arr}")
    arr.remove(1)
    print(f"arr.remove(1): arr= {arr}")

            




            
        
                
                   
        


    
if __name__ == "__main__":
    arr = ArrayListOrdered()
    arr.add(5)
    arr.add(3)
    arr.add(4)
    arr.add(1)
    arr.add(2)
    print(arr)
    arr.clear()
    print(arr)
    print(f"arr.len = {len(arr)}")    


