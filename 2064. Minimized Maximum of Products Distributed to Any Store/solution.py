import math
from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def valid(portion):
            #return sum((quantity - 1) // portion + 1 for quantity in quantities) <= n
            return sum(math.ceil(quantity / portion) for quantity in quantities) <= n

        left, right = 1, max(quantities)
        while left < right:
            mid = left + (right - left) // 2

            if valid(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
