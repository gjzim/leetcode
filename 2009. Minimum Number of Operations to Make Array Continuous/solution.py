from typing import List
from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = n = len(nums)
        nums = sorted(set(nums))
        
        for start, num in enumerate(nums):
            end = bisect_right(nums, num + n - 1)
            result = min(result, n - end + start)
           
        return result

    def minOperations_slow(self, nums: List[int]) -> int:               
        result = n = len(nums)
        nums = sorted(set(nums))
        m = len(nums)
                
        for start in range(m):
            end = start
            while end < m and nums[end] <= nums[start] + n - 1:
                end += 1

            result = min(result, n - end + start)
                        
        return result    
