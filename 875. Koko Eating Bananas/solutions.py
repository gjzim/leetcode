from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k):           
            return sum([math.ceil(pile / k) for pile in piles]) <= h

        left, right = 1, max(piles)
        
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
            
        return left
