import random
import string

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        
        dp, ds = {}, {}

        for i in range(len(pattern)):
            if dp.get(pattern[i], -1) != ds.get(s[i], -1):
                return False

            dp[pattern[i]] = ds[s[i]] = i

        return True
