from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        
        def feasible(day):
            bonquets, flowers = 0, 0
            
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
                    
            return bonquets >= m

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1            
        
        return left
