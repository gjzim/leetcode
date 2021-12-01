import random

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        rev, xc = 0, x
        while xc:
            rev = (rev * 10) + (xc % 10)
            xc //= 10    

        return rev == x

sol = Solution()
print(sol.isPalindrome(0))
