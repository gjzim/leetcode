from typing import List
import collections

class Solution:
    def topKFrequent_compact(self, nums: List[int], k: int) -> List[int]:
        numsSorted = dict(sorted(
            collections.Counter(nums).items(),
            key=lambda item: item[1],
            reverse=True
        ))
        
        return list(numsSorted.keys())[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        freq = [[] for i in range(len(nums) + 1)]
        count = collections.Counter(nums)
        
        for n, c in count.items():
            freq[c].append(n)
       
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
