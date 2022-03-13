from typing import List

class Solution:
    def partitionLabels_merge_interval(self, s: str) -> List[int]:
        intervals = self.getCharIntervals(s)
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return [(end - start + 1) for start, end in merged]

    def getCharIntervals(self, s):
        chars = {}

        for i, c in enumerate(s):
            if c in chars:
                chars[c][1] = i
            else:
                chars[c] = [i, i]
        
        return list(chars.values())

    def partitionLabels(self, s: str) -> List[int]:
        ends = {c: i for i, c in enumerate(s)}
        result = []
        l = r = 0

        for i, c in enumerate(s):
            r = max(r, ends[c])

            if i == r:
                result += [r - l + 1]
                l = i + 1

        return result
    
sol = Solution()
print(sol.partitionLabels('ababcbacadefegdehijhklij'))

