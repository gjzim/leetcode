from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def valid(diff):            
            placed, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= diff:
                    placed += 1
                    curr = position[i]                    
                     
            return placed >= m

        n = len(position)
        position.sort()
        left, right = 0, position[-1] - position[0] + 1
        
        while left < right:
            mid = left + (right - left) // 2

            if valid(mid):
                left = mid + 1
            else:
                right = mid
        
        return left - 1 if left > 0 else 0
