from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        i = j = 1
        while j < len(nums):
            if nums[i-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i
