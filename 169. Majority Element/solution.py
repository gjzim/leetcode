from typing import List
import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj, majCount = None, 0
        counts = {}

        for i in nums:
            if i not in counts:
                counts[i] = 0

            counts[i] += 1

            if counts[i] > majCount:
                maj = i
                majCount = counts[i]

        return maj

    def majorityElement_2(self, nums: List[int]) -> int:
        count, maj = 0, None
        
        for i in nums:
            if count < 1:
                maj = i
                count = 0

            if i == maj:
                count += 1
            else:
                count -= 1

        return maj
    

def generate_test(sol):
    length = random.randint(1,10000)
    major = random.randint(1,21474836)
    nums = [major] * (length // 2 + 1)
    nums += random.sample(range(0, 21474836), (length // 2))

    if major != sol.majorityElement_2(nums):
        print('error', major, sol.majorityElement_2(nums))
        
    
sol = Solution()
print(sol.majorityElement_2([1]))
print(sol.majorityElement_2([1,2,2]))
for i in range(1000):
    generate_test(sol)
