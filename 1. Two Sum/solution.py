class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, _ in enumerate(nums):
            for j, _ in enumerate(nums[i+1:]):            
                if nums[i]+nums[j+i+1] == target:
                    return [i, j+i+1]

        return []

    def twoSumHash(nums, target):
        comps = {}
        for i, val in enumerate(nums):
            comp = target-val
            if comp not in comps:
                comps[val] = i
            else:
                return [comps[comp], i]
