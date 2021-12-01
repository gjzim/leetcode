from typing import List
import random

class Solution:
    def maxSubArray_2(self, nums: List[int]) -> int:
        total, maximum = 0, nums[0]

        for i in nums:
            total += i            
            maximum = max(total, maximum)

            if total < 0:
                total = 0


        return maximum

    def maxSubArray(self, nums: List[int]) -> int:
        maxhere, maximum = 0, 0

        for n in nums:
            print(n, maxhere, maximum)
            maxhere = max(maxhere+n, n)
            maximum = max(maxhere, maximum)
            print(n, maxhere, maximum)
            print('----------------------')

        return maximum

def generate_test():
    length = random.randint(0,1000)
    nums = random.sample(range(-10000, 10000), length)

    nums.sort()
    sol = Solution()
    pos = sol.searchInsert(nums, target)
    
    nums.append(target)
    nums.sort()    

    if pos != nums.index(target):
        print('error')

    

sol = Solution()
print(sol.maxSubArray([31,-41,59,26,-53,58,97,-93,-23,84]))
