from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval: interval[1])

        result = i = 0
        while i < len(intervals):
            cur_end = intervals[i][1]
            i += 1
            
            while i < len(intervals) and intervals[i][0] < cur_end:
                result += 1
                i += 1            

        return result

    def eraseOverlapIntervals_alt(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval: interval[1])

        prev_end = -10000000
        result = 0

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                result += 1       

        return result

sol = Solution()
print(sol.eraseOverlapIntervals_alt([[1,2]]))
        
