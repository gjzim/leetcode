from typing import List
import collections

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = collections.Counter(nums)

        missing, dup = 0, 0
        for i in range(1, len(nums) + 1):
            if i not in seen:
                missing = i
            elif seen[i] == 2:
                dup = i

        return [dup, missing]

    def findErrorNums_linear(self, nums: List[int]) -> List[int]:
        du, mis, l = 0, 0, len(nums)
        for i in nums:
            nums[i % l - 1] += l
        
        for i, v in enumerate(nums): 
            if v <= l:
                mis = i + 1
            elif v > 2 * l:
                du = i + 1
            if du and mis:
                return [du, mis]
