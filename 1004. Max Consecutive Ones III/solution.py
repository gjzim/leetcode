from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = result = max_ones = 0

        for (end, d) in enumerate(nums):
            if d: max_ones += 1

            if end - start + 1 - max_ones > k:
                if nums[start]: max_ones -= 1
                start += 1

            result = max(result, end - start + 1)

        return result

    def longestOnes_concise(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0: k -= 1
        
            if k < 0:          
                if nums[left] == 0: k += 1
                left += 1
          
        return right - left + 1

sol = Solution()
print(sol.longestOnes_concise([1,1,1,0,0,0,1,1,1,1,0], 2))
