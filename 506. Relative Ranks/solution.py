import random, heapq
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        q = []
        for i, s in enumerate(score):
            heapq.heappush(q, (s, i))

        while q:
            pos = len(q)
            _, i = heapq.heappop(q)

            if pos == 1:
                score[i] = 'Gold Medal'
            elif pos == 2:
                score[i] = 'Silver Medal'
            elif pos == 3:
                score[i] = 'Bronze Medal'
            else:
                score[i] = str(pos)
        
        return score

sol = Solution()
sol.findRelativeRanks([32,518,981,8,13,1,981])
        
