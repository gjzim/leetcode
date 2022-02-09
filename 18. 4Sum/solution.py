from typing import List

class Solution:
    def fourSum_iter(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n, res = len(nums), []

        for a in range(n - 3):            
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                
                c, d = b + 1, n - 1
                while c < d:
                    cur = nums[a] + nums[b] + nums[c] + nums[d]
                    if cur == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c, d = c + 1, d - 1

                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                    elif cur > target:
                        d -= 1
                    else:
                        c += 1

        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNSum(l, r, n, nums, target, result, results):
            if (r - l + 1) < n or n < 2 or target < nums[l] * n or target > nums[r] * n:
                return

            if n == 2:
                while l < r:
                    cur = nums[l] + nums[r]
                    if cur == target:
                        results.append(result + [nums[l], nums[r]])
                        l, r = l + 1, r - 1
                        
                        while l < r and nums[l] == nums[l - 1]: l += 1
                        while l < r and nums[r] == nums[r + 1]: r -= 1
                    elif cur > target:
                        r -= 1
                    else:
                        l += 1
            else:
                for i in range(l, r + 1):
                    if i == l or (i > l and nums[i] != nums[i - 1]):
                        findNSum(i + 1, r, n - 1, nums, target - nums[i], result + [nums[i]], results)

        
        nums.sort()
        results = []
        findNSum(0, len(nums) - 1, 4, nums, target, [], results)

        return results
