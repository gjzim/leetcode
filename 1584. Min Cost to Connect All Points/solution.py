from typing import List

class UF:
    def __init__(self, n):
        self.d = [-1]*n

    def find(self, a):
        """Find and return the root/parent of an element"""
        if self.d[a] < 0:
            return a
        else:
            self.d[a] = self.find(self.d[a])

            return self.d[a]

    def union(self, a, b):
        """Union two elements into a single set"""
        ra = self.find(a)
        rb = self.find(b)

        if self.d[ra] < self.d[rb]:
            self.d[ra] += self.d[rb]
            self.d[rb] = ra
        else:
            self.d[rb] += self.d[ra]
            self.d[ra] = rb

class Solution:
    def minCostConnectPoints_kruskal(self, points: List[List[int]]) -> int:
        n = len(points)        
        edges = []
        
        for u in range(n):
            for v in range(u + 1, n):
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                edges.append((dist, u, v))

        edges.sort()
        
        uf = UF(n)
        total = 0
        used = 0

        for w, u, v in edges:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                total += w
                used += 1
                
                if used == n - 1:
                    break
                
        return total

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Prims"""
        n = len(points)        
        edges = [(0, 0)]
        inMst = [False] * n        
        total = used = 0
        
        while used < n:
            weight, cur = heapq.heappop(edges)
            
            if inMst[cur]: 
                continue
                
            inMst[cur] = True
            total += weight
            used += 1
            
            for next in range(n):
                if not inMst[next]:
                    nextWeight = abs(points[cur][0] - points[next][0]) + \
                                 abs(points[cur][1] - points[next][1])
                    
                    heapq.heappush(edges, (nextWeight, next))            
        
        return total
