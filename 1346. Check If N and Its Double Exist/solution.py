from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = set()
        for i in arr:
            if i * 2 in nums or \
               (i % 2 == 0 and i // 2 in nums):
                return True

            nums.add(i)

        return False


