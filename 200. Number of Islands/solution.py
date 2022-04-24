from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in row] for row in grid]
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(row, col):
            if row < 0 or col < 0 or \
                row >= m or col >= n or \
                visited[row][col] or \
                grid[row][col] == '0':
                return
            
            visited[row][col] = True

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(m):
            for col in range(n):
                if not visited[row][col] and grid[row][col] == '1':
                    dfs(row, col)
                    count += 1
        
        return count
