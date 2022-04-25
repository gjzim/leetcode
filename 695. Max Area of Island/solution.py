from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in row] for row in grid]
        m, n = len(grid), len(grid[0])        

        def dfs(row, col):
            if row < 0 or col < 0 or \
                row >= m or col >= n or \
                visited[row][col] or \
                grid[row][col] == 0:
                return 0

            visited[row][col] = True

            return (1 + dfs(row - 1, col) +
                        dfs(row + 1, col) +
                        dfs(row, col - 1) +
                        dfs(row, col + 1))

        result = 0
        for row in range(m):
            for col in range(n):
                if not visited[row][col] and grid[row][col] == 1:                    
                    result = max(result, dfs(row, col))
        
        return result
