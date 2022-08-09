import collections, heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        maxHeap, clock = [], 0
        
        for c, f in count.items():
            heapq.heappush(maxHeap, (-f, c))
        
        while maxHeap:
            waiting, target = [], n + 1

            while target > 0 and maxHeap:                
                f, c = heapq.heappop(maxHeap)
                
                if -f > 1:
                    waiting.append((f + 1, c))
                    
                clock, target = clock + 1, target - 1

        
            for f, c in waiting:
                heapq.heappush(maxHeap, (f, c))

            if maxHeap: clock += target
                
        return clock

        
