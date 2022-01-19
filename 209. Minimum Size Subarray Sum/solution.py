import random
from typing import List

class Solution:
    def minSubArrayLen_sw(self, target: int, nums: List[int]) -> int:       
        start = cursum = 0
        result = len(nums) + 1

        for end in range(len(nums)):
            cursum += nums[end]
                      
            while cursum >= target:
                result = min(result, end - start + 1)
                cursum -= nums[start]
                start += 1

        return result % (len(nums) + 1)

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            sums[i] = sums[i - 1] + nums[i - 1]
       
        result = len(sums)
        for start in range(len(sums)):
            pos = self.binarySearch(sums, start, len(sums)-1, sums[start] + target)
            if pos < len(sums):
                result = min(result, pos - start)
                
        return result % len(sums)

    def binarySearch(self, nums: List[int], start: int, end: int, target: int) -> int:
        while start <= end:
            mid = start + ((end-start)//2)
            
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
            
        return start

