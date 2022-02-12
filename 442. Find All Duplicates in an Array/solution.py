from typing import List

class Solution:
    def findDuplicates_with_len(self, nums: List[int]) -> List[int]:
        l, result = len(nums), []
        
        for num in nums:
            if nums[num % l - 1] > l:
                result.append(num % l)
            else:
                nums[num % l - 1] += l

        return result
            

    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        
        for num in nums:
            abs_num = abs(num)
            
            if nums[abs_num - 1] < 0:
                result.append(abs_num)
            else:
                nums[abs_num - 1] = -nums[abs_num - 1]
                       
        return result


