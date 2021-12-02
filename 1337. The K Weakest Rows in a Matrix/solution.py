import random
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        output = list(range(len(mat)))
        output.sort(key=lambda i: sum(mat[i]))
        
        return output[:k]


sol = Solution()
mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]]
print(sol.kWeakestRows(mat, 3))
        


