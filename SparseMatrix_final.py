from typing import Iterable

class Matrix():
    def __init__(self, data):
        self.arr = data

    def __getitem__(self, row):
        return self.arr[row]

    def __iter__(self):
        return iter(self.arr)

    def __repr__(self):
        return "\n".join(" ".join(f"{n:3}" for n in row) for row in self.arr)    
  
    def build_sparse(self):
        rows, cols = len(self.arr), len(self.arr[0])
        arr = []
        for r in range(rows):
            for c in range(cols):
                v = self[r][c]
                if not v:
                    continue
                arr.append((r, c, self[r][c]))    
        return MatrixSparse(rows, cols, arr)
    
    def transpose(self):
         ret = [[0 for _ in range(len(self.arr))] for _ in range(len(self.arr[0]))]
         for r in range(len(self.arr[0])):
             for c in range(len(self.arr)):
                 ret[r][c] = self.arr[c][r]
         return Matrix(ret)        
            


class MatrixSparse(Iterable):
    def __init__(self, rows, cols, arr):
        self.rows = rows
        self.cols = cols
        self.arr = arr

    def __iter__(self):
        return iter(self.arr)
    
    def restore(self):
        ret = [[0] * self.cols for _ in range(self.rows)]
        for r, c, v in self.arr:
            ret[r][c] = v
        return Matrix(ret)
    
    def transpose(self):
        ret = []
        for i in range(len(self.arr)):
            for r, c, v in self.arr:
                if i != c:
                    continue
                ret.append((r, c, v))
        return MatrixSparse(self.rows, self.cols, ret)        
     
    def transpose_fast(self):
        row_size = [0] * self.cols
        for i, col, j in self.arr:
            row_size[col] += 1
        row_start = [0] * self.cols
        for i in range(1, self.cols):
            row_start[i] = row_start[i - 1] + row_size[i - 1]
        transposed = [None] * len(self.arr)
        for row, col, value in self.arr:
            position = row_start[col]
            transposed[position] = (col, row, value)
            row_start[col] += 1 
        return MatrixSparse(self.cols, self.rows, transposed) 
            


data = [
[15, 0, 0, 22, 0, -15],
[0, 11, 3, 0, 0, 0],
[0, 0, 0, -6, 0, 0],
[0, 0, 0, 0, 0, 0],
[91, 0, 0, 0, 0, 0],
[0, 0, 28, 0, 0, 0],
]
mat = Matrix(data)
print("matrix =")
print(mat)
print()
sparse = mat.build_sparse()
print("sparse =")
for i, elem in enumerate(sparse):
    print(f"{i}: {elem}")
print()
trans = sparse.transpose()
print("trans =")
for i, elem in enumerate(trans):
    print(f"{i}: {elem}")
print()
trans_fast = sparse.transpose_fast()
print("trans_fast =")
for i, elem in enumerate(trans_fast):
    print(f"{i}: {elem}")
print()

                    