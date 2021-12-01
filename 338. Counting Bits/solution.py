from typing import List

class Solution:
    def countBits_mine(self, n: int) -> List[int]:
        out = [0]*(n+1)
        lastp2 = 1

        for i in range(1, n+1):                        
            if i == lastp2*2:
                lastp2 = i
                out[i] = 1
            else:
                out[i] = 1+out[i-lastp2]
            
        return out

    def countBits(self, n: int) -> List[int]:
        out = [0]*(n+1)

        for i in range(1, n+1):
            out[i] = out[i >> 1] + (i & 1)

        return out

##with open('list.txt', 'a') as file:    
##    for i in range(1001):        
##        out = f"{bin(i).count('1')} \n"
##        file.write(out)

sol = Solution()
print(sol.countBits(1000))
