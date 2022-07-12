from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1xn2 = 0
        for num in nums:
            n1xn2 ^= num
        
        rightMostBit = n1xn2 & -n1xn2
##        rightMostBit = 1
##        while rightMostBit & n1xn2 == 0:
##            rightMostBit <<= 1 
        
        num1, num2 = 0, 0
        for num in nums:
            if rightMostBit & num:
                num1 ^= num
            else:
                num2 ^= num
            
        return [num1, num2]


sol = Solution()
print(sol.singleNumber([1,2,1,3,2,5]))
