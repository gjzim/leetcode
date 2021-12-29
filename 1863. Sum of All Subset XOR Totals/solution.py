from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def _getSubsetXORs(nums):
            if len(nums) == 0: return [0]

            rest = _getSubsetXORs(nums[1:])
            return rest + [nums[0]^c for c in rest]

        return sum(_getSubsetXORs(nums))

sol = Solution()
print(sol.subsetXORSum([20]))
