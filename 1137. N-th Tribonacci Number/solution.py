class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n < 3: return 1
        
        t0, t1, t2 = 0, 1, 1
        for _ in range(2, n):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
            
        return t2

    def tribonacci_alt(self, n: int) -> int:       
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
            
        return c
