import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:       
        s1_chars = collections.Counter(s1)
        s2_chars = collections.Counter(s2[:len(s1)])       
        start = 0

        for end in range(len(s1), len(s2)):            
            if s1_chars == s2_chars: return True

            s2_chars[s2[end]] = s2_chars.get(s2[end], 0) + 1
            s2_chars[s2[start]] -= 1
            if s2_chars[s2[start]] == 0: s2_chars.pop(s2[start])
            start += 1
        
        return s1_chars == s2_chars

    def checkInclusion_fast(self, s1: str, s2: str) -> bool:       
        s1_chars, s2_chars = collections.defaultdict(int), collections.defaultdict(int)
        for c in s1: s1_chars[c] += 1
        for c in s2[:len(s1)]: s2_chars[c] += 1
        start = 0

        for end in range(len(s1), len(s2)):            
            if s1_chars == s2_chars: return True

            s2_chars[s2[end]] = s2_chars.get(s2[end], 0) + 1
            s2_chars[s2[start]] -= 1
            if s2_chars[s2[start]] == 0: s2_chars.pop(s2[start])
            start += 1
        
        return s1_chars == s2_chars
