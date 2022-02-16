from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result, slen = "", len(s)
       
        for word in dictionary:                        
            wlen, reslen = len(word), len(result)
            if wlen < reslen or (wlen == reslen and word > result):
                continue
            
            i = j = 0
            while i < wlen and j < slen:
                if word[i] == s[j]: i += 1
                j += 1

            if i == wlen: result = word
            
        return result
