from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = [0] * len(queries)
        
        for i, [xc, yc, r] in enumerate(queries):
            for x, y in points:                
                if (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r:
                    result[i] += 1
                    
        return result
                
