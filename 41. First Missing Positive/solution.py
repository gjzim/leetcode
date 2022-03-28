from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n, i = len(nums), 0

        while i < n:
            j = nums[i] - 1

            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1

sol = Solution()
print(sol.firstMissingPositive([1]))
print(sol.firstMissingPositive([1,2,3,4,5]))
print(sol.firstMissingPositive([1,2,0]))
print(sol.firstMissingPositive([3,4,-1,1]))
print(sol.firstMissingPositive([7,8,9,11,12]))
