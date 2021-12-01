import random

class Solution:
    def reverseBits_old(self, n: int) -> int:
        bits = [0] * 32

        i = 0
        while n:
            bits[i] = n%2
            n //= 2
            i += 1

        for i in range(32):
            n = n*2 + bits[i]    

        return n

    def reverseBits(self, n: int) -> int:
        bits = [0] * 32

        i = 0
        while n:
            bits[i] = n & 1
            n = n >> 1
            i += 1       

        for i in range(32):
            n = (n << 1) + bits[i]

        return n

    def reverseBits(self, n: int) -> int:
        ans = 0   
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n = n >> 1

        return ans

def generate_test(sol):
    num = random.randint(0, 4294967297)    
    bits = list(f'{num:032b}')
    bits.reverse()

    if sol.reverseBits(num) != sol.reverseBits_old(num):
        print('error')

sol = Solution()
for i in range(10000):
    generate_test(sol)
    
