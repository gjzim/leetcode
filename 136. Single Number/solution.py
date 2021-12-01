from typing import List
import random

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniq = 0
        for i in nums:
            uniq = uniq ^ i

        return uniq
    

def generate_test(sol):
    length = random.randint(1,20000)
    nums = random.sample(range(0, 20000), (length // 2))
    nums += nums
    uniq = random.randint(20001,30000)
    nums.append(uniq)
    random.shuffle(nums)

    if uniq != sol.singleNumber(nums):
        print('error')
        
    
sol = Solution()
for i in range(1000):    
    generate_test(sol)

