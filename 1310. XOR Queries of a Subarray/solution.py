from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

##        result = []
##        for start, end in queries:
##            if start > 0:                
##                result.append(arr[end] ^ arr[start - 1])
##            else:
##                result.append(arr[end])

        return [arr[end] ^ arr[start - 1] if start else arr[end] for start, end in queries]
