class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n, hd = x^y, 0
        while n:
            n &= n-1
            hd += 1

        return hd
    
    
