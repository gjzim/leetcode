from typing import List

class Solution:
    def isIsomorphic_smart(self, s: str, t: str) -> bool:
        d1, d2 = [-1 for _ in range(256)], [-1 for _ in range(256)]

        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False

            d1[ord(s[i])] = d2[ord(t[i])] = i

        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        cmap, taken = {}, set()

        for i, c in enumerate(s):            
            if c not in cmap:
                if t[i] in taken:
                    return False
                
                cmap[c] = t[i]
                taken.add(t[i])
            elif cmap[c] != t[i]:
                return False

        return True
            

sol = Solution()
print(sol.isIsomorphic_smart("bbbaaaba", "aaabbbba"))
print(sol.isIsomorphic_smart("foo", "noo"))
print(sol.isIsomorphic_smart("abbaa", "cddcd"))
print(sol.isIsomorphic_smart("badc", "baba"))


