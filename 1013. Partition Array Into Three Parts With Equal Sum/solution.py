from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0: return False

        i = cursum = found = 0
        while i < len(arr) and found < 2:
            cursum += arr[i]
            i += 1

            if cursum == total // 3:
                cursum = 0
                found += 1

        return i < len(arr) and found == 2
    
    def canThreePartsEqualSum_concise(self, arr: List[int]) -> bool:
        total = sum(arr)
        avg = total // 3
        cursum = found = 0
        
        for d in arr:
            cursum += d
            if cursum == avg:
                cursum = 0
                found += 1

        return total % 3 == 0 and found >= 3
