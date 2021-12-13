class Solution:
    def isPowerOfThree_loop(self, n: int) -> bool:
        while n > 1 and n % 3 == 0:
            n //= 3
            
        return n == 1

    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (3**20) % n == 0

