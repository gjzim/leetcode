from typing import List
import math

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:        
        points.sort(key = lambda point: point[1])
        
        prev_end = -math.inf    
        arrows = 0

        for start, end in points:           
            if start > prev_end:
                prev_end = end
                arrows += 1                    

        return arrows

sol = Solution()
print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
print(sol.findMinArrowShots([[1,2]]))
        
