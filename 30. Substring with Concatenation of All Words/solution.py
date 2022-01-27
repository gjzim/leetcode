import collections
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wlen = len(words[0])
        wslen = wlen * len(words)
        
        wcounts = collections.defaultdict(int)
        for w in words: wcounts[w] += 1        
        
        start, res = 0, []
        matches = collections.defaultdict(int)
        for end in range(wslen, len(s) + 1):
            matchCount = 0
            
            for i in range(start, end, wlen):
                word = s[i:i+wlen]
                matches[word] += 1
                if word not in wcounts or \
                   matches[word] > wcounts[word]:
                    break
                
                matchCount += 1

            if matchCount == len(words): res.append(start)
            start += 1

            matches.clear()

        return res
