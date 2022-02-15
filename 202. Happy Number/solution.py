from typing import List

class Solution:
    def isHappy_set(self, n: int) -> bool:
        seen = {}

        while n not in seen:
            seen[n] = True
            
            t = 0
            while n:
                t += (n%10)**2
                n = n//10

            n = t            

        return n == 1

    def isHappy(self, n: int) -> bool:
        slow = fast = n

        while fast != 1 and self.digits_squared(fast) != 1:
            slow = self.digits_squared(slow)
            fast = self.digits_squared(self.digits_squared(fast))

            if slow == fast:
                return False

        return True
    
    def digits_squared(self, num):
        result = 0
        while num:
            result += (num % 10) * (num % 10)
            num //= 10

        return result
