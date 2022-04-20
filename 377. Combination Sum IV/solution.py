from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        combs = [0] * (target + 1)
        combs[0] = 1
        
        for i in range(1, target + 1):            
            for num in nums:
                if i >= num: 
                    combs[i] += combs[i - num]

        return combs[target]
