from typing import List

class Solution:
    def insert_slow(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        p = 0
        while p < len(intervals) and intervals[p][0] < newInterval[0]:
            p += 1

        if p < len(intervals):
            intervals.insert(p, newInterval)
        else:
            intervals.append(newInterval)

        return self.merge(intervals, start=0)

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged, i, n = [], 0, len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        merged.append(newInterval)

        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged

    def merge(self, intervals: List[List[int]], start: int) -> List[List[int]]:
        merged = [intervals[start]]
        
        for i in range(start + 1, len(intervals)):
            interval = intervals[i]
            if interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
  
        return merged
    
intervals = [[1,2]]
newInterval = [3,4]

sol = Solution()
print(sol.insert(intervals, newInterval))



[[3,4]]
[1,2]
[[1,4]]
[1,2]
[[1,2]]
[2,4]
