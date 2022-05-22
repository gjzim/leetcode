class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:        
        num = [int(d) for d in str(n)]
        inverseAt = len(num) - 1
        
        for i in range(inverseAt, 0, -1):
            if num[i] < num[i - 1]:
                inverseAt = i - 1
                num[inverseAt] -= 1

        for i in range(inverseAt + 1, len(num)):
            num[i] = 9

        result = 0
        for d in num:
            result = (result * 10) + d
        
        return result
