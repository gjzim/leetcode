class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vmap = {
            'a': 1,
            'e': 2,
            'i': 4,
            'o': 8,
            'u': 16
        }

        seen = {0: -1}
        cur = res = 0
        for i, c in enumerate(s):
            cur ^= vmap.get(c, 0)
            seen.setdefault(cur, i)
            res = max(res, i - seen[cur])

        return res
