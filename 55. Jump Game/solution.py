from typing import List

class Solution:
    def canJump_dp(self, nums: List[int]) -> bool:
        n = len(nums)
        jumps = [False]*n
        jumps[0] = True

        for i, v in enumerate(nums):
            for j in range(i+1, min(i+v+1, n)):
                jumps[j] = jumps[i]
                
                if jumps[-1]: return True

        return jumps[-1]

    def canJump(self, nums: List[int]) -> bool:
        n, pos = len(nums), 0
        
        for i, v in enumerate(nums):
            pos = max(pos, i+v)
            
            if pos >= n-1: return True            
            if i > pos: return False
            
        return False
