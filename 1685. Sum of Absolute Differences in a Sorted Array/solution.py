from typing import List

class Solution:
    def getSumAbsoluteDifferences_1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = nums[:]
        for i in range(1, n):
            pre[i] += pre[i - 1]

        result = []
        for i, num in enumerate(nums):
            before = abs(pre[i - 1] - i * num) if i > 0 else 0
            after = abs((pre[-1] - pre[i]) - (n - i - 1) * num)
            result.append(before + after)
            
        return result
    
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum, right_sum, res, n = 0, sum(nums), [], len(nums)
        
        for i, num in enumerate(nums):
            res += [i * num - left_sum + right_sum - (n - i) * num]
            left_sum += num
            right_sum -= num
            
        return res



        
