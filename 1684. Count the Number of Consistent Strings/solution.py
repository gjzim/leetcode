from typing import List

class Solution:
    def countConsistentStrings_hash(self, allowed: str, words: List[str]) -> int:
        allowedChars = {}
        for i in allowed:
            allowedChars[i] = True

        count = 0
        for word in words:
            isValid = True
            
            for c in word:
                if c not in allowedChars:
                    isValid = False
                    break

            if isValid: count += 1

        return count

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedMask = 0
        for c in allowed:
            allowedMask |= 1 << (ord(c)-ord('a'))

        count = len(words)
        for word in words:           
            for c in word:
                cm = 1 << (ord(c)-ord('a'))
                if not cm & allowedMask:
                    count -= 1
                    break

        return count

sol = Solution()
print(sol.countConsistentStrings('adbcghz', ['a','x']))
