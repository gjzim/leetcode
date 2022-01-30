class Solution:
    def getSum(self, a: int, b: int) -> int:       
        while b != 0:
            carry = a & b
            a = (a ^ b) & 0xFFFF
            b = (carry << 1) & 0xFFFF
            
        return a if a <= 0x7FFF else ~(a ^ 0xFFFF)
