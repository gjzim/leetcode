from typing import List
from union_find import UF

class Solution:
    def longestConsecutive_uf(self, nums: List[int]) -> int:
        uf = UF(nums)

        for num in nums:
            uf.union(num, num + 1)
            uf.union(num, num - 1)

        return uf.largest_size

    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        seen = set(nums)

        for start in nums:
            if start - 1 not in seen:
                end = start
                while end + 1 in seen:
                    end += 1

                result = max(result, end - start + 1)
        
        return result
