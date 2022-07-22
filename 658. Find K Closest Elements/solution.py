from typing import List
import heapq, bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n, p = len(arr), bisect.bisect_left(arr, x)
        if p == n: p - 1

        minheap = []
        for i in range(p - k - 1, p + k):
            if i >= 0 and i < n:
                heapq.heappush(minheap, (abs(arr[i] - x), arr[i])) 

        return sorted([heapq.heappop(minheap)[1] for _ in range(k)])

    def findClosestElements_1liner(self, arr: List[int], k: int, x: int) -> List[int]:
        return sorted(sorted(arr, key = lambda n: (abs(n - x), n))[:k])
