class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:       
        sp, tp = 0, 0
        slen, tlen = len(s), len(t)
        
        while tp < tlen and sp < slen:
            if s[sp] == t[tp]:
                sp += 1

            tp += 1

        return sp == slen
