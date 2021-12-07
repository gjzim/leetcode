import random, string
from typing import List

class Solution:
    def validPalindrome_iter(self, s: str) -> bool:
        i, j = 0, len(s)-1

        while i < j:
            if s[i] != s[j]:
                return s[i+1:j] == s[j:i+1:-1] or \
                       s[i:j-1] == s[j-1:i:-1]

            i, j = i+1, j-1
                
        return True

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1

        while i < j:
            if s[i] != s[j]:
                return self.isPalindrome(s, i+1, j) or \
                    self.isPalindrome(s, i, j-1)

            i, j = i+1, j-1        
                
        return True
    
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
                
            i, j = i+1, j-1
            
        return True

    def validPalindrome_recursive(self, s: str) -> bool:
        return self.isValidPalindrome(s, 0, len(s)-1)

    def isValidPalindrome(self, s: str, i: int, j: int, skipped = False) -> bool:        
        if i > j: return True

        if s[i] == s[j]:
            return self.isValidPalindrome(s, i+1, j-1, skipped)
        else:           
            return not skipped and \
                   (self.isValidPalindrome(s, i+1, j, True) or self.isValidPalindrome(s, i, j-1, True) )       


def generate_test(sol, s = None):
    if s is None:
        maxLength = 100
        
        length = random.randint(2, maxLength)
        s = random.choices(string.ascii_lowercase, k=length)

        if bool(random.randint(0,1)):
            choice = random.randint(0,10)
            if choice == 0:
                s += [random.choice(string.ascii_lowercase)] + list(reversed(s))
            elif choice == 1:
                s += list(reversed(s))
            else:
                s += list(reversed(s))
                s[random.randint(0, length//2)] = random.choice(string.ascii_lowercase)
        else:
            choice = random.randint(1,length//2)
            while choice:
                s.pop()
                s.append(random.choice(string.ascii_lowercase))
                choice -= 1

        s = ''.join(s)
        
    if sol.validPalindrome(s) != sol.validPalindrome_recursive(s):
        print(s)

sol = Solution()
##generate_test(sol, "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
s = "cuffucu"
print(sol.validPalindrome(s))
print(sol.validPalindrome_recursive(s))
##generate_test(sol, "eeccccbebaeeabebccceea")
##for i in range(10):
##    generate_test(sol)
