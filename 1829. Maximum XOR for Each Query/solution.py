from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] ^= nums[i - 1]

        mask = ~(0xFFFFF << maximumBit) & 0xFFFFF            
        return [~num & mask for num in nums[::-1]]
