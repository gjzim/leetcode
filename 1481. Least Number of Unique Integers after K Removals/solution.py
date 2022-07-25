from typing import List
import collections
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count, minHeap = collections.Counter(arr), []

        for num, freq in count.items():
            heapq.heappush(minHeap, (freq, num))
            
        while k:            
            freq, num = heapq.heappop(minHeap)
            k, freq = k - 1, freq - 1
            if freq:
                heapq.heappush(minHeap, (freq, num))
            
        return len(minHeap)
