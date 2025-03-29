class Search:
    def __init__(self, data):
        self.arr = data

    def search_max(self):
        self.max = 0
        self.max_row = 0
        self.max_col = 0
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                    if self.arr[i][j] > self.max:
                         self.max = self.arr[i][j]
                         self.max_row = i
                         self.max_col = j

    def __str__(self):
         return f"가장 큰 수: {self.max}, 위치 {self.max_row,self.max_col}"

data = [
    [7, 3, 1],
    [2, 8, 5],
    [4, 9, 6]
]

answer = Search(data)
answer.search_max()
print(answer)                         