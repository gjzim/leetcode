import random, heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = -(heapq.heappop(stones))
            s2 = -(heapq.heappop(stones))

            if s1 != s2:
                heapq.heappush(stones, -(s1-s2))
        
        return -stones[0] if stones else 0

    def lastStoneWeight_concise(self, stones: List[int]) -> int:
        q = [-stone for stone in stones]
        heapq.heapify(q)
        
        while (len(q)) > 1:
            heapq.heappush(q, heapq.heappop(q) - heapq.heappop(q))

        return -q[0]
