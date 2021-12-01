from typing import List

class Solution:
    def romanToInt_2(self, s: str) -> int:
        stov = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        excps = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }
        
        total = 0
        
        for i, c in enumerate(s):
            if c in excps and i+1 < len(s) and s[i+1] in excps[c]:                
                total -= stov[c]
                continue
                
            total += stov[c]
            
        return total

    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = 0

        for i in range(0, len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total + roman[s[-1]]

sol = Solution()
print(sol.romanToInt('III'))
