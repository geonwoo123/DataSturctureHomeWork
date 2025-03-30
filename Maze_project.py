import copy
from typing import List, Optional
def build_maze():
    grid = [
        ["E", 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, "X"],
    ]
    ent = ext = None
    rows = len(grid)
    cols = len(grid[0])
    for pos in range(rows * cols):
        row, col = pos // cols, pos % cols
        if grid[row][col] == "E":
            grid[row][col] = 0
            ent = row, col
            continue
        
        if grid[row][col] == "X":
            grid[row][col] = 0
            ext = row, col
    return grid, ent, ext


def print_mat(maze):
    print("\n".join(" ".join(f"{n:3}" for n in row) for row in maze))


class Stack:
    def __init__(self,capacity = 10):
        self.capacity = capacity
        self.arr:List[Optional[int]] = [None] * capacity
        self.top = -1

    def __len__(self):
        return self.top+1

    def empty(self):
        return self.top == -1

    def full(self):
        if self.top +1 >= self.capacity:
            return True
        return False

    def push(self,data: int):
        if self.full():
            raise IndexError("push from full stack")
        else:
            self.top += 1
            self.arr[self.top] = data

    def pop(self):
        if self.empty():
            raise IndexError("stack is empty")

        data = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return data

    def peek(self):
        if self.empty():
            raise IndexError("stack is empty")
        return self.arr[self.top]                    

    def __repr__(self):
        return str(self.arr[:self.top+1])


class Maze:
    # N, NE, E, SE, S, SW, W, NW
    dir_ = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    
    def __init__(self, map, ent, ext):
        self.maze = map
        self.ent = ent
        self.ext = ext
        self.rows, self.cols = len(self.maze), len(self.maze[0])
        self.stack = Stack(self.rows * self.cols)
    
        # 방문을 marking 하여 재방문을 피하기 위한 용도로 사용한다.
        self.mark = copy.deepcopy(self.maze)


    def explore(self):
        row, col = self.ent
        self.stack.push((row, col))
        self.mark[row][col] = 0  # 방문 표시
        count = 1

        while True:
            row, col = self.stack.peek()

            move_flag = False
            for dx, dy in self.dir_:
                nr, nc = row + dx, col + dy

                if not (0 <= nr < self.rows and 0 <= nc < self.cols):
                    continue

                if self.maze[nr][nc] == 0 and self.mark[nr][nc] == 0:
                    self.stack.push((nr, nc))
                    self.mark[nr][nc] = count
                    if (nr, nc) == self.ext:
                        return 
                        
                    count += 1
                    move_flag = True
                    break

            if not move_flag:
                self.stack.pop()

    def __str__(self):
        self.maze[self.ent[0]][self.ent[1]] = 'E'
        self.maze[self.ext[0]][self.ext[1]] = 'X'
        result = f"Maze Problem: {self.rows} x {self.cols}\n" + "\n".join(" ".join(f"{n:2}" for n in row) for row in self.maze)
        self.maze[self.ent[0]][self.ent[1]] = 0
        self.maze[self.ext[0]][self.ext[1]] = 0
        return result
        

if __name__ == "__main__":
    map, ent, ext = build_maze()
    maze = Maze(map, ent, ext)
    print(maze)
    print()

    print(f"Entrance = {ent}, Exit = {ext}")
    maze.explore()
    print_mat(maze.mark)