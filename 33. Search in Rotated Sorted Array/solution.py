from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = self.get_rotation_count(nums)
        n = len(nums)
        l, h = k, n + k - 1

        while l <= h:
            m = (l + h) // 2
            
            if nums[m % n] > target:
                h = m - 1
            elif nums[m % n] < target:
                l = m + 1
            else:
                return m % n

        return -1

    def get_rotation_count(self, nums):
        l, h = 0, len(nums) - 1

        while l < h:
            m = (l + h) // 2
            
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m

        return l

        
