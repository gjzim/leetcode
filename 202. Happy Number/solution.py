from typing import List

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}

        while n not in seen:
            seen[n] = True
            
            t = 0
            while n:
                t += (n%10)**2
                n = n//10

            n = t            

        return n == 1

sol = Solution()
print(sol.isHappy(19))
