from typing import List
import random

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1

        while low <= high:
            mid = low + ((high-low)//2)
            
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return low



def generate_test():
    length = random.randint(0,20)
    target = random.randint(-100,100)
    nums = random.sample(range(-100, 100), length)

    nums.sort()
    sol = Solution()
    pos = sol.searchInsert(nums, target)
    
    nums.append(target)
    nums.sort()    

    if pos != nums.index(target):
        print('error')

##for i in range(1000):
##    generate_test()

sol = Solution()
print(sol.searchInsert([5,6,3,9,14], 9))


