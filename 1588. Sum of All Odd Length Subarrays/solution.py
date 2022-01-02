from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        
        for k in range(1, len(arr)+1, 2):
            total += self.sumSubarrays(arr, k)

        return total

    def sumSubarrays(self, arr: List[int], k) -> int:
        start, wsum = 0, sum(arr[:k])
        total = wsum

        for end in range(k, len(arr)):
            wsum += arr[end] - arr[start]
            total += wsum
            start += 1

        return total

sol = Solution()
print(sol.sumOddLengthSubarrays([1000]))
