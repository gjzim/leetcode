import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pchars, chars = collections.defaultdict(int), collections.defaultdict(int)
        for c in p: pchars[c] += 1
        for c in s[:len(p)]: chars[c] += 1
        
        start, result_indexes = 0, []
        for end in range(len(p), len(s)):
            if pchars == chars: result_indexes.append(start)
            
            chars[s[end]] = chars.get(s[end], 0) + 1
            chars[s[start]] -= 1
            if chars[s[start]] == 0: chars.pop(s[start])
            start += 1            

        if pchars == chars: result_indexes.append(start)

        return result_indexes
