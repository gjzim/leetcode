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
