from typing import List
import random, collections

class Solution:
    def findDisappearedNumbers_hash(self, nums: List[int]) -> List[int]:
        counts = collections.Counter(nums)
        output = []
        for i in range(1, len(nums)+1):
            if i not in counts:
                output.append(i)
        
        return output

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i, output = 0, []

        while i < len(nums):
            n = nums[i]
            if nums[n-1] != nums[i]:
                nums[n-1], nums[i] = nums[i], nums[n-1]
            else:
                i += 1
 
        return [j+1 for j in range(len(nums)) if nums[j] != j+1]

    def findDisappearedNumbers_best(self, nums: List[int]) -> List[int]:
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

def generate_test(sol):
    maxLength = 10000
    length = random.randint(6, maxLength)

    nums = random.choices(range(1, length-5), k=length)
    if sol.findDisappearedNumbers_hash(nums) != sol.findDisappearedNumbers(nums):
        print('error')

sol = Solution()
for i in range(1000):
    generate_test(sol)

