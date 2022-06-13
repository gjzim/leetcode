import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def valid(num):
            count = num // a + num // b + num // c
            count -= num // ab + num // bc + num // ca
            count += num // abc

            return count >= n

        ab, bc, ca = math.lcm(a, b), math.lcm(b, c), math.lcm(c, a)
        abc = math.lcm(ab, c)

        left, right = 1, max(a, b, c) * n
        #left, right = 1, 10 ** 10
        while left < right:
            mid = left + (right - left) // 2

            if valid(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
