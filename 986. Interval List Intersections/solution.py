from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0
        
        while i < len(firstList) and j < len(secondList):
            first, second = firstList[i], secondList[j]
                        
            if first[1] < second[0]: i += 1
            elif second[1] < first[0]: j += 1
            else:
                result.append([
                    max(first[0], second[0]), 
                    min(first[1], second[1])
                ])

                if first[1] < second[1]: i += 1
                else: j += 1

        return result
