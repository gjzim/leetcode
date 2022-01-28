import collections

class Solution:
    def minWindow_slow(self, s: str, t: str) -> str:
        schars = collections.defaultdict(int)
        tchars = collections.defaultdict(int)
        for c in t: tchars[c] += 1

        end, res = 0, s + 'a'
        for start in range(len(s)):
            while not self.isValid(schars, tchars) and end < len(s):
                schars[s[end]] += 1
                end += 1            

            if self.isValid(schars, tchars) and end - start - 1 < len(res):                
                res = s[start:end]
                
            schars[s[start]] -= 1        
        
        return res if len(res) < len(s) + 1 else ''

    def isValid(self, chars, pchars):
        for c in pchars:
            if c not in chars or chars[c] < pchars[c]:
                return False            

        return True

    def minWindow(self, s: str, t: str) -> str:
        chars = collections.defaultdict(int)
        for c in t: chars[c] += 1

        start = matched = sstart = 0
        min_len = len(s) + 1

        for end, c in enumerate(s):
            if c in chars:
                chars[c] -= 1
                if chars[c] >= 0:
                    matched += 1            

            while matched == len(t):
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    sstart = start
                                
                if s[start] in chars:
                    if chars[s[start]] == 0:
                        matched -= 1
                    chars[s[start]] += 1
                    
                start += 1
        
        return s[sstart:sstart+min_len] if min_len < len(s) + 1 else ''
