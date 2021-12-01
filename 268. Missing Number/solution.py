from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0        
        for i, n in enumerate(nums):
            missing ^= n^(i+1)

        return missing


