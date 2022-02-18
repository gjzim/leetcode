from typing import List
import collections

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = collections.Counter(nums)
        result = 0

        for num in dic:
            if k == 0 :
                result += dic[num] > 1
            elif num + k in dic:
                result +=1 
                        
        return result

    def findPairs_bs(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        i = 0
        n = len(nums)
        
        while i < n - 1:
            num = nums[i]
            i += 1
            
            if self.inArr(nums, num + k, i, n - 1):
                result += 1
                while i < n - 1 and nums[i] == nums[i - 1]:
                    i += 1

        return result

    def inArr(self, nums, target, l, r):
        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return True

        return False

sol = Solution()
print(sol.findPairs([1,3,1,5,4], 0))
