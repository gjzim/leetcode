from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            post[i] *= post[i+1] * nums[i+1]

        pre = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] *= pre * post[i]
            pre *= nums[i]
            
        return result

    def productExceptSelf_space_optimized(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        pre = post =  1        

        for i in range(len(nums)):
            result[i] *= pre
            pre *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            result[i] *= post
            post *= nums[i]
            
        return result


