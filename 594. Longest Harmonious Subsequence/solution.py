from typing import List
import random, collections

class Solution:
    def findLHS_slow(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        if len(counts) < 2:
            return 0

        lhs_len = 0
        uniq_nums = sorted(counts)

        for i in range(len(uniq_nums)-1):
            if uniq_nums[i+1] - uniq_nums[i] == 1:
                cur_len = counts[uniq_nums[i+1]] + counts[uniq_nums[i]]
                lhs_len = max(lhs_len, cur_len)
        
        return lhs_len

    def findLHS(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)

        length = 0
        for c in counts:
            if (c+1) in counts:
                length = max(length, counts[c]+counts[c+1])
        
        return length

#file = open('input.txt', 'a')
def generate_test(sol):
    maxLength = 10000
    length = random.randint(1, maxLength)

    nums = random.choices(range(-10000, 10000), k=length)
    if sol.findLHS(nums) != sol.findLHS_slow(nums):
        print('error')
    

sol = Solution()
for i in range(1000):
    generate_test(sol)

#file.close()
