class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            cur = guess(mid)
            
            if cur == -1:
                hi = mid - 1
            elif cur == 1:
                lo = mid + 1
            else:
                return mid
            
        return -1
