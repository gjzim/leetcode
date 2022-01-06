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

    def lengthOfLongestSubstring_alt(self, s: str) -> int:
        seen = {}
        result = start = 0

        for end, c in enumerate(s):
            if c in seen and start <= seen[c]:
                start = seen[c] + 1
            else:
                result = max(result, end - start + 1)

            seen[c] = end

        return result
