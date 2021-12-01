import random, string, collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = collections.Counter(s)        
       
        total = 0
        for c, t in counts.items():
            total += t//2 * 2
                
            if total % 2 == 0 and t % 2 == 1:
                total += 1
           
        return total

sol = Solution()
print(sol.longestPalindrome("PsAAdxLfcKoXRLkqBwRcamfNGqRJIJLboTrOKq"))


def generate_test(sol):
    maxLength = 2000
    length = random.randint(1, maxLength)

    chars = random.choices(string.ascii_lowercase + string.ascii_uppercase, k=length)
    s = ''.join(chars)

    print(s)
    
#for i in range(200):
    #generate_test(sol)
