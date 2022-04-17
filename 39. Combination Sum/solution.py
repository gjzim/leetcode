from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        def findCombinationSum(candidates, target, start, selectedSoFar, results):
            if target < 0: return            
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                result = selectedSoFar + [num]

                if target == num:
                    results.append(result)
                else:
                    findCombinationSum(candidates, target - num, i, result, results)


        results = []
        findCombinationSum(candidates, target, 0, [], results)
        return results
