from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:        
        def findCombinationSum(nums, target, start, selectedSoFar, results):
            if target == 0:
                results.append(selectedSoFar)
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                if nums[i] > target:
                    break                
                
                findCombinationSum(nums, target - nums[i], i + 1, selectedSoFar + [nums[i]], results)

        results = []        
        candidates.sort()
        findCombinationSum(candidates, target, 0, [], results)
        return results
