from typing import List
import string, random

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            

def generate_test(sol):
    maxLength = 100000
    length = random.randint(1, maxLength)

    s = random.choices(string.printable, k=length)

    sc = s[::]
    sol.reverseString(sc)
    if sc != s[::-1]:
        print('error')

sol = Solution()
for i in range(1000):
    generate_test(sol)
