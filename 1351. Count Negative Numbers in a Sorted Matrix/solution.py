import random
from typing import List

class Solution:
    def countNegatives_BF(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    count += n-j
                    break
                
        return count

    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col, count = m-1, 0, 0

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                row -= 1
                count += (n-col)
            else:
                col += 1
                
        return count







