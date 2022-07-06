from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def valid(size):
            return sum((num - 1) // size for num in nums) > maxOperations

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2

            if valid(mid):
                left = mid + 1
            else:
                right = mid
                
        return left
