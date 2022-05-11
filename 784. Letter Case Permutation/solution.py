from typing import List

class Solution:
    def letterCasePermutation_alt(self, s: str) -> List[str]:
        n, result = len(s), []
  
        for i in range(2**n, 2**(n + 1)):
            variant = list(s)
            bitmask = bin(i)[3:]            

            for j in range(n):
                if bitmask[j] == '1':
                    if variant[j].isalpha():
                        variant[j] = variant[j].swapcase()
                    else:
                        break       

                if j == n-1:
                    result.append(''.join(variant))
    
        return result

    def letterCasePermutation(self, s: str) -> List[str]:
        result = [s]

        for i in range(len(s)):            
            if s[i].isalpha():
                n = len(result)
                for j in range(n):                    
                    chs = list(result[j])
                    chs[i] = chs[i].swapcase()
                    result.append(''.join(chs))                   

        return result

sol = Solution()
print(sol.letterCasePermutation('3z4'))
