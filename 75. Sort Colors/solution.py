from typing import List
import random

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums)-1

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1


def generate_test(sol):
    maxLength = 300
    length = random.randint(1, maxLength)

    nums = random.choices(range(3), k=length)
    sorted_nums = sorted(nums)
    sol.sortColors(nums)

    if sorted_nums != nums:
        print('error', nums, sorted_nums)

sol = Solution()
for i in range(10000):
    generate_test(sol)
