from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def hasKpairs(diff):
            count = i = j = 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= diff:
                    j += 1
                
                count += j - i - 1
                i += 1
                
            return count >= k

        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = left + (right - left) // 2
            if hasKpairs(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
