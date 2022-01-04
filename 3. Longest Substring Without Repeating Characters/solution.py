class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, curlen, result = 0, 0, 0, 0
        seen = set()

        while start < len(s):
            while end < len(s) and s[end] not in seen:
                seen.add(s[end])
                curlen, end = curlen + 1, end + 1

            result = max(result, curlen)
            seen.remove(s[start])
            curlen, start = curlen - 1, start + 1            
            
        return result
