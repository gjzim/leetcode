from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:       
        start = cursum = 0
        result = len(nums) + 1

        for end in range(len(nums)):
            cursum += nums[end]
                      
            while cursum >= target:
                result = min(result, end - start + 1)
                cursum -= nums[start]
                start += 1

        return result % (len(nums) + 1)
        
