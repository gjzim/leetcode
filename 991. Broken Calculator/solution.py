class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        steps = 0
        
        while startValue < target:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1

            steps += 1
            
        return steps + startValue - target
        
