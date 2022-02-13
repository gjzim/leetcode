class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = self.getNextValidPosition(s, i)
            j = self.getNextValidPosition(t, j)

            if i < 0 and j < 0:
                return True
            elif i < 0 or j < 0 or s[i] != t[j]:
                return False
            
            i -= 1
            j -= 1
        
        return True

    def getNextValidPosition(self, s, i):
        hashes = 0
        
        while i >= 0:
            if s[i] == '#':
                hashes += 1
            elif hashes > 0:
                hashes -= 1
            else:
                break

            i -= 1

        return i
