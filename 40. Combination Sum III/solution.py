from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:      
        def findCombinationSum(target, start, selectedSoFar, results):
            if target == 0 and len(selectedSoFar) == k:
                results.append(selectedSoFar)
                return

            for i in range(start, 10):
                if i > target: break

                findCombinationSum(target - i, i + 1, selectedSoFar + [i], results)

        results = []           
        findCombinationSum(n, 1, [], results)
        return results
