import random

class Solution:
    def reverseVowels_slower(self, s: str) -> str:
        vowels = { v: True for v in 'aeiouAEIOU' }
        i, j = 0, len(s)-1
        chars = list(s)

        while i < j:
            if chars[i] not in vowels:
                i += 1

            if chars[j] not in vowels:
                j -= 1
            
            if i >= 0 and chars[i] in vowels and \
               j < len(chars) and chars[j] in vowels:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1

        return ''.join(chars)

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set('aeiouAEIOU')
        l, r = 0, len(s)-1
        
        while l < r:
            while l < r and s[l] not in vowels: l += 1
            while l < r and s[r] not in vowels: r -= 1

            if l >= r: break
            
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1

        return ''.join(s)


sol = Solution()
print(sol.reverseVowels('leetcode'))
        


