from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, subsets):
            subsets.append(path)
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                
                dfs(nums[i+1:], path+[nums[i]], subsets)
                
        subsets = []
        nums.sort()
        dfs(nums, [], subsets)
        return subsets

    def subsetsWithDup_iter(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]        
        end = 0
        
        for i in range(len(nums)):
            start = 0            
            if i > 0 and nums[i] == nums[i - 1]:
                start = end
                
            end = len(result)
            for j in range(start, end):
                result.append(result[j] + [nums[i]])
        
        return result
