from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        s = s.lower()

        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i] != s[j]: 
                    return False                
                i += 1
                j -= 1
        
        return True

sol = Solution()
print(sol.isPalindrome(".,"))
