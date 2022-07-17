from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDist(point):
            x, y = point
            return x * x + y * y
        
        minHeap = []        
        for i in range(k):
            dist = getDist(points[i])
            heapq.heappush(minHeap, (-dist, points[i]))

        for i in range(k, len(points)):
            dist = getDist(points[i])

            if -dist > minHeap[0][0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (-dist, points[i]))

        return [point for _, point in minHeap]
        
