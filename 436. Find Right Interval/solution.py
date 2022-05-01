from heapq import *
import bisect
from typing import List

class Solution:
    def findRightInterval_two_heaps(self, intervals: List[List[int]]) -> List[int]:
        result = [-1] * len(intervals)
        startTimeHeap = []
        endTimeHeap = []

        for i, interval in enumerate(intervals):    
            heappush(startTimeHeap, (interval[0], i))
            heappush(endTimeHeap, (interval[1], i))

        while endTimeHeap:
            end, i = heappop(endTimeHeap)
    
            while startTimeHeap and end > startTimeHeap[0][0]:
                heappop(startTimeHeap)
    
            if not startTimeHeap: 
                break

            result[i] = startTimeHeap[0][1]
        
        return result

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        intervals = sorted([start, end, i] for i, [start, end] in enumerate(intervals))
        starts = [start for start, _, _ in intervals]
        result = [-1] * n

        for start, end, i in intervals:
            right = bisect.bisect_left(starts, end)

            if right < n:
                result[i] = intervals[right][2]


        return result
