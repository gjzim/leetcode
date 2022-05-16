from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:              
        return self.diffWaysToComputeWithMemo(expression)
    
    def diffWaysToComputeWithMemo(self, exp, memo = {}):
        if exp in memo:
            return memo[exp]
        
        if exp.isnumeric():
            return [int(exp)]
            
        result = []
        for i, c in enumerate(exp):
            if c.isnumeric(): continue

            lparts = self.diffWaysToCompute(exp[:i])
            rparts = self.diffWaysToCompute(exp[i+1:])

            for p1 in lparts:
                for p2 in rparts:
                    if c == '+':
                        result.append(p1 + p2)
                    elif c == '-':
                        result.append(p1 - p2)
                    elif c == '*':
                        result.append(p1 * p2)
        
        memo[exp] = result
        return result
