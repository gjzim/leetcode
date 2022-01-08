from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        i = 0
        p = j = n-1
        
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                result[p] = nums[i]*nums[i]
                i += 1
            else:
                result[p] = nums[j]*nums[j]
                j -= 1
                
            p -= 1
            
        return result
