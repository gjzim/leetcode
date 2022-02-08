from typing import List

class Solution:
    def fourSum_using_3sum(self, nums: List[int], target: int) -> List[List[int]]:
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
