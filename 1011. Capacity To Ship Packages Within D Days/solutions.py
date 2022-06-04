from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            daysNeeded, total = 1, 0
            
            for weight in weights:
                total += weight
                
                if total > capacity:
                    total = weight
                    daysNeeded += 1
                    
                    if daysNeeded > days:
                        return False
                    
            return True
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
