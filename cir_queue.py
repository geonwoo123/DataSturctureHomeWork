class QueueCircular:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front_ = 0
        self.rear_ = 0

    def __len__(self):
        return (self.rear_ - self.front_ + self.capacity) % self.capacity

    def empty(self):
        return self.front_ == self.rear_

    def full(self):
        return (self.rear_ + 1) % self.capacity == self.front_

    def front(self):
        if self.empty():
            raise IndexError("front from empty queue")
        return self.arr[self.front_]
    
    def rear(self):
        if self.empty():
            raise IndexError("rear from empty queue")
        return self.arr[(self.rear_ - 1 + self.capacity) % self.capacity]

    def enqueue(self, data):
        if self.full():
            raise OverflowError("enqueue to full queue")
        self.arr[self.rear_] = data
        self.rear_ = (self.rear_ + 1) % self.capacity

    def dequeue(self):
        if self.empty():
            raise IndexError("dequeue from empty queue")
        data = self.arr[self.front_]
        self.front_ = (self.front_ + 1) % self.capacity
        return data   

    def __repr__(self):
        if self.empty():
            return "[]"
        ret = []
        i = self.front_
        while i != self.rear_:
            ret.append(self.arr[i])
            i = (i + 1) % self.capacity
        return "[" + ", ".join(map(str, ret)) + "]"


def info_queue(q):
    print(f"queue.cursor:{q.front_, q.rear_}")
    print(f"queue.data:{q.front() if not q.empty() else None, q.rear() if not q.empty() else None}")
    print(f"queue.status:{q.empty(), q.full()}")
    print(f"queue = {q}")
    print(f"queue.size = {len(q)}")


if __name__ == "__main__":
    SIZE = 8
    queue = QueueCircular(SIZE)
    print(f"queue = {queue}")
    info_queue(queue)
    print()

    data = "A"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()

    data = "B"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()

    data = "C"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()

    data = "D"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()

    print(f">> queue.dequeue() = {queue.dequeue()}")
    info_queue(queue)
    print()

    print(f">> queue.dequeue() = {queue.dequeue()}")
    info_queue(queue)
    print()

    data = "E"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()

    data = "F"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()

    data = "G"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()

    data = "H"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()

    data = "I"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()

    print(f">> queue.dequeue() = {queue.dequeue()}")
    info_queue(queue)
    print()

    print(f">> queue.dequeue() = {queue.dequeue()}")
    info_queue(queue)
    print()

    print(f">> queue.dequeue() = {queue.dequeue()}")
    info_queue(queue)
    print()

    print(f">> queue.dequeue() = {queue.dequeue()}")
    info_queue(queue)
    print()

    print(f">> queue.dequeue() = {queue.dequeue()}")
    info_queue(queue)
    print()

    print(f">> queue.dequeue() = {queue.dequeue()}")
    info_queue(queue)
    print()

    print(f">> queue.dequeue() = {queue.dequeue()}")
    info_queue(queue)
    print()

    data = "J"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()
        
