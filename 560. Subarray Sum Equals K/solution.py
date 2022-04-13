from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        result = cursum = 0
        
        for num in nums:
            cursum += num
            if cursum - k in seen:                
                result += seen[cursum - k]
            
            seen[cursum] = seen.get(cursum, 0) + 1

        return result
