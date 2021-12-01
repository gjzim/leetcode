import math, random

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, h = 1, 46341

        while l <= h:
            m = (h-l)//2 + l

            if num/m > m:
                l = m+1
            elif num/m < m:
                h = m-1
            else:
                return True
            
        return False    
        
    
sol = Solution()
print(sol.isPerfectSquare(1))
print(sol.isPerfectSquare(2))
print(sol.isPerfectSquare(3))
print(sol.isPerfectSquare(2**31))
