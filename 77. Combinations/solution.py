from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def _combinations(s, n, k):        
            if n == 0 or k == 0: return [[]]

            combs = []
            for i in range(s, n-k+2):
                restCombs = _combinations(i+1, n, k-1)
                combs.extend([[i] + comb for comb in restCombs])

            return combs

        return _combinations(1, n, k)

