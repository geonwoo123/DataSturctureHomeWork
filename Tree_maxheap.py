class TreeBinaryHeapMax:
    def __init__(self):
        self.arr: list[int] = []

    def insert(self, elem: int) -> None:
        #max힙은 항상 부모노드가 자식보다 커야하므로 리스트에 넣고 bubble up해서 항상 큰값을 부모노드로 유지하도록 해주기기
        self.arr.append(elem)
        self.bubble_up()


    def delete(self) -> int | None:
        if not self.arr:
            return None
        if len(self.arr) == 1:
            return self.arr.pop()
        
        max_root = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.bubble_down()
        return max_root


    def bubble_up(self) -> None:
        #새로운 요소가 들어왔을때 부모보다 크면 부모랑 위치릴 바꿔주기기
        pos = len(self.arr) - 1
        while pos > 0:
            parent_pos = self.parent(pos)
            if self.arr[parent_pos] < self.arr[pos]:
                self.arr[parent_pos], self.arr[pos] = self.arr[pos], self.arr[parent_pos]
                pos = parent_pos
            else:
                break

    def bubble_down(self, pos: int = 0) -> None:
        #왜 제일 마지막값을 처음에 넣고 시작하느냐? 그것은 트리의 구조를 유지하기위해서 단순히 루트 다음인덱스를 루트로 지정하면 트리의 구조가 망가지기때문에 트리의 제일 아래 오른쪽을
        #을 먼저 빼서 맨 앞에서부터 위치를 보면서 정렬시키면 트리의 구조를 깨지않으면서 삭제 가능
        size = len(self.arr)
        while True:
            left = self.left(pos)
            right = self.right(pos)
            bigger = pos

            if left < size and self.arr[left] > self.arr[bigger]:
                bigger = left
            if right < size and self.arr[right] > self.arr[bigger]:
                bigger = right

            if bigger == pos:
                break

            self.arr[pos], self.arr[bigger] = self.arr[bigger], self.arr[pos]
            pos = bigger

    def parent(self, pos) -> int:
        return (pos - 1) // 2

    def left(self, pos) -> int:
        return 2 * pos + 1
    
    def right(self, pos) -> int:
        return 2 * pos + 2

    def __repr__(self) -> str:
        return f"{self.arr}"

#if __name__ == "__main__":
    #print("max heap:")
    #input = [20, 15, 2, 14, 10]
    #heap = TreeBinaryHeapMax()
    #for elem in input:
    #    heap.insert(elem)
    #    print(heap)
    #
    #for _ in range(len(heap.arr)):
    #    heap.delete()
    #    print(heap)

if __name__ == "__main__":
    print("max heap:")
    input = [20, 15, 2, 14, 10]
    heap = TreeBinaryHeapMax()
    for num, elem in enumerate(input):
        heap.insert(elem)
        print(f"{num}. inserted: {elem:2d}: {heap}")
    print()

    for num, _ in enumerate(range(len(heap.arr))):
        deleted = heap.delete()
        print(f"{num}. deleted: {deleted:2d}: {heap}")