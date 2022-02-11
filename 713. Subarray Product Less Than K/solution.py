from typing import List
import math

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        largest, n = max(nums), len(nums)
        
        if (largest == 1 and k > n) or \
           (largest > 1 and k > 0 and math.log(k, largest) > n):
            return (n * (n + 1)) // 2
        
        result = 0
        for start in range(n):
            product, end = 1, start
            while end < n:
                product *= nums[end]
                if product < k: result += 1
                else: break
                end += 1
      
        return result

    def numSubarrayProductLessThanK_concise(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        
        product, start, result = 1, 0, 0
        for end in range(len(nums)):
            product *= nums[end]

            while product >= k:
                product //= nums[start]
                start += 1

            result += end - start + 1
      
        return result

