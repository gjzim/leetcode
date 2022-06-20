from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.pre = [[0 for _ in range(self.cols + 1)] for _ in range(self.rows + 1)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                self.pre[i + 1][j + 1] = matrix[i][j] + self.pre[i + 1][j] + self.pre[i][j + 1] - self.pre[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre[row2 + 1][col2 + 1] - self.pre[row1][col2 + 1] - self.pre[row2 + 1][col1] + self.pre[row1][col1]
