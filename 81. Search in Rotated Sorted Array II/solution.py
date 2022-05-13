from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)        
        while n > 1 and nums[0] == nums[n - 1]:
            n -= 1
            
        k = self.get_rotation_count(nums, n)        
        l, h = k, n + k - 1

        while l <= h:
            m = (l + h) // 2
            
            if nums[m % n] > target:
                h = m - 1
            elif nums[m % n] < target:
                l = m + 1
            else:
                return True

        return False

    def get_rotation_count(self, nums, n):        
        l, h = 0, n - 1    

        while l < h:
            m = (l + h) // 2
            
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m

        return l

        
