class Solution:
    def hammingWeight(self, n: int) -> int:
        hw = 0
        while n:
            n &= n-1
            hw += 1

        return hw
    
    
