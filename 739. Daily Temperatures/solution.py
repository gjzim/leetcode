from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, result = [], [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                cur = stack.pop()
                result[cur] = i - cur                

            stack.append(i)
       
        return result
