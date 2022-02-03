from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]

                if cur_sum < target: l += 1
                elif cur_sum > target: r -=1
                else: return target

                if abs(target - cur_sum) < abs(target - res):
                    res = cur_sum
            
        return res
