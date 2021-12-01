import random
import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:                
        if len(s) != len(t):
            return False
        
        chars = {}
        
        for c in s:
            chars[c] = chars.get(c, 0) + 1
       
        for c in t:
            if c not in chars:
                return False

            chars[c] -= 1
            if chars[c] == 0:
                del chars[c]
            
        return len(chars) == 0

    def isAnagramBetter(self, s: str, t: str) -> bool:                       
        schars, tchars = {}, {}
        
        for c in s:
            schars[c] = schars.get(c, 0) + 1
       
        for c in t:
            tchars[c] = tchars.get(c, 0) + 1
            
        return schars == tchars

    def isAnagramBF(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))
    
def generate_test(sol):
    maxLength = 50000
    length = random.randint(1, maxLength)

    chars = random.choices(string.ascii_lowercase, k=length)
    s = ''.join(chars)
    random.shuffle(chars)
    t = ''.join(chars)

    if bool(random.randint(0, 1)):
        mlength = random.randint(1, length)
        mchars = random.choices(string.ascii_lowercase, k=mlength)
        chars = chars + mchars
        random.shuffle(chars)
        t = ''.join(chars[:length])

    if sol.isAnagramBetter(s, t) != sol.isAnagram(s, t):
        print('error')
        

sol = Solution()
for i in range(1000):
    generate_test(sol)
