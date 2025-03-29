class Snail_array:
    def __init__(self, size:int):
        self.size = size
        self.snail_mat = [[0 for _ in range(size)] for _ in range(size)]
        print(self.snail_mat)

    def build_snail_array(self):
        top, bottom, left, right = 0, self.size - 1, 0, self.size-1
        value = 1
        while value <= self.size * self.size:
            for col in range(left, right + 1):
                self.snail_mat[top][col] = value
                value += 1
            top += 1

            for row in range(top, bottom + 1):
                self.snail_mat[row][right] = value
                value += 1
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    self.snail_mat[bottom][col] = value
                    value += 1
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    self.snail_mat[row][left] = value
                    value += 1
                left += 1

    def __iter__(self):
        return iter(self.snail_mat)
    
size = 3
answer = Snail_array(size)
answer.build_snail_array()
for i in answer:
    print(i)    
                                            

    

        
