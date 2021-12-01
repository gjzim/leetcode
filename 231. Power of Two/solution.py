import random

class Solution:
    def isPowerOfTwoBM(self, n: int) -> bool:
        if n < 1: return False        
       
        return n & (n-1) == 0

    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1: return False
        
        while n % 2 == 0:
            n //= 2

        return n == 1
    
        
def generate_test(sol):
    n = random.randint(-2147483648, 2147483647)

    if sol.isPowerOfTwoBM(n) != sol.isPowerOfTwo(n):
        print('error')
    
    
sol = Solution()
for i in range(100000):
    generate_test(sol)

