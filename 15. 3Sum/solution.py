from typing import List

class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            self.findAndAddPairs(nums, -nums[i], i+1, triplets)
        
        return triplets

    def findAndAddPairs(self, nums, target, left, triplets):
        right = len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] == target:
                triplets.append([-target, nums[left], nums[right]])

                left, right = left + 1, right - 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
