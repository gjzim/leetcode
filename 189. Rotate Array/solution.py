from typing import List

class Solution:
    def rotate_2nd_arr(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)        
        for i, num in enumerate(nums[:]):
            j = (i + k) % n
            nums[j] = num

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = (n - k) % n
        nums[:] = nums[k:] + nums[:k]

