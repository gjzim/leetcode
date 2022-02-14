from typing import List

class Solution:
    def findUnsortedSubarray_slow(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] > nums[left + 1] and nums[right] < nums[right - 1]:
                break

            if nums[left] <= nums[left + 1]: left += 1
            if nums[right] >= nums[right - 1]: right -= 1

        if left >= right: return 0

        sub_max = sub_min = nums[left]
        for i in range(left, right + 1):
            if nums[i] > sub_max: sub_max = nums[i]
            if nums[i] < sub_min: sub_min = nums[i]

        while left > 0 and nums[left - 1] > sub_min:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] < sub_max:
            right += 1
           
        return right - left + 1

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        sub_max = sub_min = nums[left]
        for i in range(left, right + 1):
            if nums[i] > sub_max: sub_max = nums[i]
            if nums[i] < sub_min: sub_min = nums[i]

        while left > 0 and nums[left - 1] > sub_min:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] < sub_max:
            right += 1
           
        return right - left + 1
