from typing import List
import collections

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = collections.defaultdict(int)
        result = 0
        
        for num in nums:
            complement = k - num
            
            if seen[complement] > 0:
                seen[complement] -= 1
                result += 1
            else:
                seen[num] += 1
            
        return result
