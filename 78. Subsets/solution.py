from typing import List

class Solution:
    def subsets_iter(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
  
        for num in nums:
            subsets += [subset + [num] for subset in subsets]
    
        return subsets

    def subsets_backtrack(self, nums: List[int]) -> List[List[int]]:        
        def backtrack(start, cur, k, n):
            if len(cur) == k:
                subsets.append(cur[:])

            for i in range(start, n):
                cur.append(nums[i])
                backtrack(i + 1, cur, k, n)
                cur.pop()
        
        subsets = []
        n = len(nums)
        for k in range(n + 1):
            backtrack(0, [], k, n)        
    
        return subsets

    def subsets_dfs(self, nums):
        def dfs(nums, path, ret):
            ret.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path+[nums[i]], ret)
                
        ret = []
        dfs(nums, [], ret)
        return ret

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            bitmask = bin(i)[3:]
            
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output

