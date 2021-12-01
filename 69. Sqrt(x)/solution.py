import random

class Solution:
    def mySqrt_bf(self, x: int) -> int:
        i = 0
        while (i+1)*(i+1) <= x: 
            i += 1
            
        return i

    def mySqrt(self, x: int) -> int:
        l, h = 0, 46341
        
        while l <= h:            
            m = (l+h)//2

            if ( m*m > x and (m+1)*(m+1) < x ) or \
               ( m*m < x and (m+1)*(m+1) > x ) :
                break

            if m*m < x:
                l = m + 1
            elif m*m > x:
                h = m - 1
            else:
                break
        
        return m
        
def generate_test(sol):
    x = random.randint(0,2147483640)    

    if sol.mySqrt(x) != int(x**0.5):
        print(x, sol.mySqrt(x), int(x**0.5))
        
    
sol = Solution()
for i in range(10000):    
    generate_test(sol)

