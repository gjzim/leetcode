from typing import List
import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        nodes = collections.deque([(0,0,1)])
        visited = set()
        n = len(grid) - 1

        while nodes:
            cur = nodes.popleft()
            if cur[0] == n and cur[1] == n:
                return cur[2]

            if (cur[0], cur[1]) in visited:
                continue

            visited.add((cur[0], cur[1]))
            nodes.extend(self.getNeighbors(cur, grid, n))

        return -1

    def getNeighbors(self, node, grid, n):
        x, y, d = node
        if grid[x][y] == 1: return []
        
        children = []        
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i < 0 or j < 0 or i > n or j > n or \
                   (i == x and j == y):
                    continue
                elif grid[i][j] == 0:
                    children.append((i, j, d + 1))

        return children
