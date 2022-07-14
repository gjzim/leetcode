import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scount = collections.Counter(s)
        tcount = collections.Counter(t)
        
        result = 0
        for c in scount.keys():
            tc = tcount.get(c, 0)
            
            if tc < scount[c]:
                result += scount[c] - tc
                
        return result
