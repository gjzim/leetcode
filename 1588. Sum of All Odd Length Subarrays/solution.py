import random
from typing import List

class Solution:
    def sumOddLengthSubarrays_1(self, arr: List[int]) -> int:
        # Uses sliding window technique
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

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # Uses prefix sum array
        n= len(arr)
        arr = [0] + arr
        for i in range(1, n+1):
            arr[i] += arr[i-1]

        total = arr[-1]
        for i in range(3, n+1, 2):
            for j in range(i, n+1):
                total += arr[j] - arr[j-i]

        return total
