class SetUnion:
    def __init__(self, size):
        self.size = size
        self.parent: list[int] = [-1 for _ in range(size)] #각 노드의 부모가 누구인지 저장하는 배열로 처음에는 자기 자신이 자신의 부모이다.

    def find(self, node: int) -> int: #어떤 노드가 속한 집합의 대표 노드 찾아주는 메서드드
            #배열의 있는 데이터값은 그 인덱스의 노드의 부모노드를 의미 예를들어 parent = [0,1,2,2,4,2]
        if self.parent[node] < 0:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
        # if self.parent[node] == node:
        #     return node
        # return self.find(self.parent[node])          


    def union(self, n1: int, n2: int) -> None:
        root1 = self.find(n1)
        root2 = self.find(n2)
        if root1 == root2:
            return
        # root1의 집합이 더 크거나 같으면 (같을 때 root1을 부모로 만들기 위해 <= 사용)
        if self.parent[root1] <= self.parent[root2]:
            self.parent[root1] += self.parent[root2]
            self.parent[root2] = root1 # root1이 root2의 부모가 됨
        else: # root2의 집합이 엄격하게 더 크면
            self.parent[root2] += self.parent[root1]
            self.parent[root1] = root2 # root2가 root1의 부모가 됨




# if __name__ == "__main__":
#     SIZE = 10
#     # set0
#     sets = SetUnion(SIZE)
#     print(f"init = {sets.parent}")
#     # S1
#     sets.union(0, 6)
#     sets.union(0, 7)
#     sets.union(0, 8)
#     print(f"parent = {sets.parent}, find({8}) = {sets.find(8)}")
#     # S2
#     sets.union(4, 1)
#     sets.union(4, 9)
#     print(f"parent = {sets.parent}, find({9}) = {sets.find(9)}")
#     # S3
#     sets.union(2, 3)
#     sets.union(2, 5)
#     print(f"parent = {sets.parent}, find({5}) = {sets.find(5)}")

# if __name__ == "__main__":
#     SIZE = 10
#     sets = SetUnion(SIZE)
#     print(f" init = {sets.parent}")
#     for i, n in enumerate(range(9)):
#         sets.union(i, i + 1)
#         print(f"{n}: parent = {sets.parent} find({i}) ={sets.find(i)}")
if __name__ == "__main__":
    SIZE = 10
    sets = SetUnion(SIZE)
    print(f"parent = [{', '.join(f'{x:2d}' for x in sets.parent)}]")
    sets.union(0, 1)
    print(f"parent = [{', '.join(f'{x:2d}' for x in sets.parent)}],find({1}) = {sets.find(1)}" )
    sets.union(1, 2)
    print(f"parent = [{', '.join(f'{x:2d}' for x in sets.parent)}],find({2}) = {sets.find(2)}")
    sets.union(3, 4)
    print(f"parent = [{', '.join(f'{x:2d}' for x in sets.parent)}],find({4}) = {sets.find(4)}")
    sets.union(2, 4)
    print(f"parent = [{', '.join(f'{x:2d}' for x in sets.parent)}],find({4}) = {sets.find(4)}")
    sets.find(4)
    print(f"parent = [{', '.join(f'{x:2d}' for x in sets.parent)}],find({4}) = {sets.find(4)}")
            