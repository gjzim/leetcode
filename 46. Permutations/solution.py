from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]

        out = []
        for i, n in enumerate(nums):                        
            perms = self.permute(nums[:i] + nums[i+1:])
            
            for perm in perms:
                perm.insert(0, n)

            out.extend(perms)

        return out

        
