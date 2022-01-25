from typing import List
import collections

class Solution:
    def shortestPath_slow(self, grid: List[List[int]], k: int) -> int:
        nodes = collections.deque([(0,0,0,k)])
        visited = set()
        m, n = len(grid) - 1, len(grid[0]) - 1

        while nodes:
            cur = nodes.popleft()
            if cur[0] == m and cur[1] == n:
                return cur[2]

            if (cur[0], cur[1], cur[3]) in visited:
                continue

            visited.add((cur[0], cur[1], cur[3]))
            nodes.extend(self.getNeighbors(cur, grid, m, n))
            
        return -1

    def getNeighbors(self, node, grid, m, n):
        x, y, d, k = node
        children = []
        for i, j in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
            if i < 0 or j < 0 or i > m or j > n:
                continue        
            elif grid[i][j] == 0:
                children.append((i, j, d + 1, k))
            elif k > 0:
                children.append((i, j, d + 1, k - 1))

        return children
