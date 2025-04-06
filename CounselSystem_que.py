from typing import List, Optional

class Queue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.arr: List[Optional[int]] = [None] * capacity
        self.front_ = self.rear_ = -1

    def __len__(self):
        return self.rear_ - self.front_

    def __repr__(self) -> str:
        ret = ", ".join(map(str, self.arr[: len(self)]))
        return f"[{ret}]"
    
    def empty(self):
        return self.rear_ == self.front_
    
    def full(self):
        return len(self) == self.capacity
    
    def front(self):
        if self.empty():
            raise IndexError("front from empty queue")
        return self.arr[self.front_ + 1]
    
    def rear(self):
        if self.empty():
            raise IndexError ("rear from empty queue")
        return self.arr[self.rear_]
    
    def enqueue(self, data):
        if self.full():
            raise IndexError("enqueue from full queue")

        self.rear_ += 1
        self.arr[self.rear_] = data

    def dequeue(self):
        if self.empty():
            raise IndexError("dequeue from empty queue")
        ret = self.arr[self.front_ + 1]
        for i in range(self.rear_):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.rear_] = None
        self.rear_ -= 1
        return ret
    

def counsel(n: int, customers: List[int]):
    #먼저 큐 생성(크기는 고객수만큼 즉 len(customers))
    #고객 한명한명 큐에 enque해주기
    #상담사 n명만큼의 배열을 만들고 일단 0으로 초기화
    #deque해준 값을 배열에 넣기
    #[2,5,2,1,8]
    #[0,0,0]
    #time이란 변수로 시간을 카운트
    #반복문으로 상담사배열을 1씩 줄여주면서 1씩 줄때마다 time += 1
    #배열에 0이 있다면 그 위치에 다시 디큐한값 넣기
    #만약 고객 큐 배열의 길이가 0이면 상담사 배열의 뭐든 요소가 0이 될때까지 반복문
    #총 time 리턴하기기

    queue = Queue(len(customers))
    for custom in customers:
        queue.enqueue(custom)  #일단 customers을 전부 큐에 넣기 
    counselor = [0] * n
    time = 0   #[2,5,2,1,8] [0,0,0]
            
    for i in range(n):
        if not queue.empty():
            counselor[i] = queue.dequeue()
    while not queue.empty() or any(i > 0 for i in counselor):
        time += 1
        for i in range(n):
            if counselor[i] > 0:
                counselor[i] -= 1
                if counselor[i] == 0 and not queue.empty():
                    counselor[i] = queue.dequeue()

    return time

n = 2
customers = [2,5,8,1,3,5]
print(counsel(n,customers))

   

    

    




    


    

