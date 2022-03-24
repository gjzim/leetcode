from typing import List

class Solution:
    def missingNumber_bit(self, nums: List[int]) -> int:
        missing = 0        
        for i, n in enumerate(nums):
            missing ^= n^(i+1)

        return missing

    def missingNumber(self, nums: List[int]) -> int:
        """Use cyclic sort"""
        
        i, n = 0, len(nums)
        while i < n:
            j = nums[i]            
            if nums[i] < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        for i in range(n):
            if nums[i] != i:
                return i

        return n

