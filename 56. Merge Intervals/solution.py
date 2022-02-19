from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval.start)
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start > merged[-1].end:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
  
        return merged
