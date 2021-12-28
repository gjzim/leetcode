from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj = self.getAdjList(n, edges)
        visited, nodes = set(), [start]

        while nodes:
            cur = nodes.pop()

            if cur == end: return True

            if cur not in visited:
                nodes.extend(adj[cur])
                visited.add(cur)
        
        return False

    def getAdjList(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return adj
