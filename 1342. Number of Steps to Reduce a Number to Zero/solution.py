import random

class Solution:
    def numberOfSteps_bf(self, num: int) -> int:
        steps = 0
        
        while num:            
            if num%2 == 1:
                num -= 1
            else:
                num /= 2
        
            steps += 1
            
        return steps

    def numberOfSteps(self, num: int) -> int:
        if num == 0: return 0
        
        steps = 0        
        while num:            
            steps += 1 + (num & 1)
            num >>= 1
            
        return steps-1

def generate_test(sol):
    x = random.randint(0,2147483640)    

    if sol.numberOfSteps_bf(x) != sol.numberOfSteps(x):
        print('error')
        
sol = Solution()
for i in range(10000):    
    generate_test(sol)
