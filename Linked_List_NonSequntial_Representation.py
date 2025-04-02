class ListArrayNonSeq:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.link = [-1] * capacity
        self.first = -1
        self.size = 0
        self.free = 0

    def __len__(self):
        return self.size

    def _get_free_index(self):
        while self.free < self.capacity and self.arr[self.free] is not None:
            self.free += 1
        if self.free >= self.capacity:
            return -1
        return self.free

    def add(self, data):
        self.insert(data)

    def insert(self, data):
        idx = self._get_free_index()
        if idx == -1:
            raise Exception("List is full")

        self.arr[idx] = data

        if self.first == -1 or self.arr[self.first] > data:
            self.link[idx] = self.first
            self.first = idx
        else:
            prev = self.first
            current = self.link[prev]
            while current != -1 and self.arr[current] < data:
                prev = current
                current = self.link[current]
            self.link[idx] = current
            self.link[prev] = idx

        self.size += 1

    def delete(self, data):
        if self.first == -1:
            return

        if self.arr[self.first] == data:
            idx = self.first
            self.first = self.link[self.first]
            self.arr[idx] = None
            self.link[idx] = -1
            self.size -= 1
            return

        prev = self.first
        current = self.link[prev]
        while current != -1 and self.arr[current] != data:
            prev = current
            current = self.link[current]

        if current != -1:
            self.link[prev] = self.link[current]
            self.arr[current] = None
            self.link[current] = -1
            self.size -= 1

    def __repr__(self):
        return f"[{', '.join(str(data) for data in self.arr if data is not None)}]"




if __name__ == "__main__":
    SIZE = 6
    lst = ListArrayNonSeq(SIZE)
    try:
        print(f"lst[{len(lst)}] = {lst}")
        lst.add("B")
        print(f"lst[{len(lst)}] = {lst}")
        lst.add("E")
        print(f"lst[{len(lst)}] = {lst}")
        lst.add("F")
        print(f"lst[{len(lst)}] = {lst}")
        lst.insert("C")
        print(f"lst[{len(lst)}] = {lst}")
        lst.insert("A")
        print(f"lst[{len(lst)}] = {lst}")
        lst.add("H")
        print(f"lst[{len(lst)}] = {lst}")
        lst.add("I")
    except Exception as e:
        print(e)

    try:
        lst.insert("G")
    except Exception as e:
        print(e)

    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("A")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("E")
    print(f"lst[{len(lst)}] = {lst}")
    lst.insert("G")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("C")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("F")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("G")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("B")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("H")
    print(f"lst[{len(lst)}] = {lst}")
    lst.insert("E")
    print(f"lst[{len(lst)}] = {lst}")
    lst.insert("F")
    print(f"lst[{len(lst)}] = {lst}")
