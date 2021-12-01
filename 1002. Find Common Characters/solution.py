from typing import List
import collections, random

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chars = collections.Counter(words[0])

        for i in range(1, len(words)):
            cur = collections.Counter(words[i])

            for c in chars:
                chars[c] = min(chars[c], cur.get(c, 0))

##        output = []
##        for c in chars:
##            while chars[c] > 0:
##                output.append(c)
##                chars[c] -= 1
                
        return list(chars.elements())

words = []
with open('words.txt') as file:
    for word in file:
        words.append(word.strip())

def generate_test(sol, words):
    maxLength = 100
    length = random.randint(1, maxLength)

    random.shuffle(words)
    sol.commonChars(words)
    
sol = Solution()
print(sol.commonChars(["ella", "bello", "celli"]))
for i in range(2):
    #generate_test(sol,words)
    pass
