class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def valid(num):
            total = 0
            for row in range(1, m + 1):
                count = min(num // row, n)
                if count == 0: 
                    break
                total += count
                
            return total >= k
        
        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            
            if valid(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
