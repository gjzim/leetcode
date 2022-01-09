from typing import List
import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        total = 0        
        while k > 0:            
            elem = heapq.heappop(nums)
            if elem >= 0 or not nums or elem > -nums[0]: break
            total, k = total - elem, k - 1

        if k > 0: total += ((-1)**k) * elem

        return total + sum(nums)
