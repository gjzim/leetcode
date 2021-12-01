from collections import deque

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars, counts = deque(), {}
        
        for i, c in enumerate(s):
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
                chars.append((c, i))

        while chars:
            (c, i) = chars.popleft()
            if counts[c] == 1:
                return i
        
        return -1

sol = Solution()
print(sol.firstUniqChar("aabb"))
