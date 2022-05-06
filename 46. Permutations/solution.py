from typing import List

class Solution:
    def permute_alt(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]

        result = []
        for i, num in enumerate(nums):                        
            perms = self.permute(nums[:i] + nums[i+1:])
            
            for perm in perms:
                result.append([num] + perm)

        return result

    def permute_alt1(self, nums: List[int]) -> List[List[int]]:        
        def generate(index, curPerm):
            if index == len(nums):
                result.append(curPerm)
            else:
                for i in range(len(curPerm) + 1):
                    newPerm = curPerm[:]
                    newPerm.insert(i, nums[index])
                    generate(index + 1, newPerm)
            
        result = []
        generate(0, [])        
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:        
        def generate(curPerm):
            if len(curPerm) == len(nums):
                result.append(curPerm[:])
            else:
                for i in range(len(nums)):
                    if nums[i] in curPerm: continue
                    
                    curPerm.append(nums[i])
                    generate(curPerm)
                    curPerm.pop()
            
        result = []
        generate([])        
        return result
        
