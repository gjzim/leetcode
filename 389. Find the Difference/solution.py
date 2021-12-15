class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = ord(t[-1])

        for i in range(len(s)):
            diff ^= ord(s[i]) ^ ord(t[i])        

        return chr(diff)

            
