from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:        
        def findMaxBeauty(query):
            if query < items[0][0]:
                return 0
            
            left, right = 0, n
            while left < right:
                mid = left + (right - left) // 2
                
                if items[mid][0] <= query:
                    left = mid + 1
                else:
                    right = mid
                                
            return items[left - 1][1] if left > 1 else items[left][1]

        result = [0] * len(queries)
        n = len(items)
        
        items.sort(key = lambda item: (item[0], -item[1]))
        for i in range(1, n):
            items[i][1] = max(items[i][1], items[i - 1][1])
        
        
        for i, query in enumerate(queries):
            result[i] = findMaxBeauty(query)
        
        return result
