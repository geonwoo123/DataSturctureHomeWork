from collections import deque

class WinnerTree:
    def __init__(self, runs: list[deque[float]]) -> None:
        self.runs = runs  # 정렬된 데이터 그룹 (run)
        self.size_runs = len(runs)  # run의 개수
        self.tree: list[int | None] = [None] * (2 * self.size_runs)  # Winner Tree의 인덱스 저장용 리스트

        # 트리 초기화
        self.build_tree()
        print("tree:", self.tree)  # 초기 트리 출력

    def build_tree(self) -> None:
        """ Winner Tree를 초기화하는 함수 """
        for i in range(self.size_runs):
            self.tree[self.size_runs + i] = i  # 리프 노드에 run 인덱스 저장

        # 내부 노드 채우기
        for i in range(self.size_runs - 1, 0, -1):
            self.tree[i] = self.winner(self.tree[2 * i], self.tree[2 * i + 1])

    def winner(self, left: int, right: int) -> int:
        """ 두 개의 run 중 더 작은 값을 가진 인덱스를 반환 """
        if self.value(left) < self.value(right):
            return left
        return right

    def value(self, idx: int) -> float:
        """ 주어진 인덱스의 run에서 가장 작은 값을 반환 (없으면 무한대) """
        if idx is None or not self.runs[idx]:
            return float("inf")  # 빈 deque인 경우 무한대 반환
        return self.runs[idx][0]  # deque의 첫 번째 값 반환

    def merge(self) -> float | None:
        """ Winner Tree를 활용하여 최소값을 반환하고 병합 수행 """
        winner_idx = self.tree[1]  # 트리 루트가 최소값을 가진 run의 인덱스
        if not self.runs[winner_idx]:  # 해당 run이 비었으면 종료
            return None
        
        value = self.runs[winner_idx].popleft()  # 가장 작은 값 제거
        self.update_tree(winner_idx)  # 트리를 업데이트
        return value

    def update_tree(self, idx: int) -> None:
        """ 새로운 최소값을 반영하여 Winner Tree를 업데이트 """
        idx += self.size_runs  # 리프 노드 위치 찾기
        while idx > 1:
            parent = idx // 2
            self.tree[parent] = self.winner(self.tree[2 * parent], self.tree[2 * parent + 1])
            idx = parent

# 실행 예제
if __name__ == "__main__":
    runs: list[deque[float]] = [
        deque([10, 15, 16]),  # Run 0
        deque([9, 20, 38]),  # Run 1
        deque([20, 20, 30]),  # Run 2
        deque([6, 15, 25, 28]),  # Run 3
        deque([8, 15, 50]),  # Run 4
        deque([9, 11, 16]),  # Run 5
        deque([90, 95, 99]),  # Run 6
        deque([17, 18, 20]),  # Run 7
    ]

    tree = WinnerTree(runs)
    merged = []

    while (val := tree.merge()) is not None:
        merged.append(val)

    print(merged)  # 정렬된 리스트 출력
    print(runs)  # 모든 run이 비워진 상태 출력
