from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowStart, windowSum = 0, sum(nums[:k])
        mavg = windowSum / k
       
        for windowEnd in range(k, len(nums)):            
            windowSum += nums[windowEnd] - nums[windowStart]
            mavg = max(mavg, windowSum / k)
            windowStart += 1

        return mavg


