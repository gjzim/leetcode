from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k: return 0
        
        def valid(portion):
            return sum(pile // portion for pile in candies) >= k
        
        left, right = 1, max(candies) + 1
        
        while left < right:
            mid = left + (right - left) // 2
            if valid(mid):
                left = mid + 1
            else:
                right = mid
        
        return left - 1 if left > 1 else 1
