from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        result = []        

        def dfs(node, path):
            if node == n - 1:
                result.append(path)

            for otherNode in graph[node]:
                dfs(otherNode, path + [otherNode])

        dfs(0, [0])
        return result
