import collections, heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        chars, maxheap = collections.Counter(s), []
        for c, freq in chars.items():
            heapq.heappush(maxheap, (-freq, c))

        result, prev = "", None
        while maxheap:
            freq, c = heapq.heappop(maxheap)
    
            result += c    
            if prev and prev[0] < 0:
                heapq.heappush(maxheap, prev)
    
            prev = (freq + 1, c)

        return result if len(result) == len(s) else ""    
