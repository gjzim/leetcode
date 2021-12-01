import random

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        mp = -1 if x < 0 else 1
        x *= mp
        
        while x:
            rev = (rev * 10) + (x % 10)
            x //= 10

        rev *= mp
        return 0 if rev < -2**31 or rev >= 2**31 else rev

sol = Solution()
print(sol.reverse(-8463847412))
print(sol.reverse(7463847412))



