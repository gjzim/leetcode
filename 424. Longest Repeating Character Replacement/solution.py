import collections

class Solution:
    def characterReplacement_slower(self, s: str, k: int) -> int:
        chars = collections.defaultdict(int)
        start, result = 0, 0

        for end, c in enumerate(s):
            chars[c] += 1            

            while len(chars) > k+1 or max(chars.values()) <= end-start-k:
                chars[s[start]] -= 1
                if chars[s[start]] == 0: del chars[s[start]]
                start += 1
                
            result = max(result, end-start+1)
            
        return result

    def characterReplacement(self, s: str, k: int) -> int:
        chars = collections.defaultdict(int)
        start = result = max_repeated = 0

        for end, c in enumerate(s):
            chars[c] += 1
            max_repeated = max(max_repeated, chars[c])

            if (end - start + 1 - max_repeated) > k:
                chars[s[start]] -= 1
                start += 1
                
            result = max(result, end - start + 1)
            
        return result
