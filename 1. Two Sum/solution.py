class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, _ in enumerate(nums):
            for j, _ in enumerate(nums[i+1:]):            
                if nums[i]+nums[j+i+1] == target:
                    return [i, j+i+1]

        return []
