from typing import List

class Solution:
    def longestCommonPrefix_bp(self, strs: List[str]) -> str:
        i, lcp = 0, ""
        
        while True:
            if i >= len(strs[0]): return lcp
            
            c = strs[0][i]            
            for s in strs:
                if i >= len(s) or s[i] != c: return lcp

            i, lcp = i+1, lcp+c
        
        return lcp

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]

        strs.sort()
        for i, c in enumerate(strs[0]):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
            
        return strs[0]

    def longestCommonPrefix_concise(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        s1, s2 = min(strs), max(strs)
        
        for i, c in enumerate(s1):
            if s1[i] != s2[i]:
                return s1[:i]
            
        return s1
