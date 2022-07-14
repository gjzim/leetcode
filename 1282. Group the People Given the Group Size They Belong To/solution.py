from typing import List
import collections

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            
        result = []
        for size in groups.keys():
            while groups[size]:
                result.append(groups[size][:size])
                groups[size] = groups[size][size:]
                            
        return result
