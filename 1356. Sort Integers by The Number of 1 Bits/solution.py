from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda num: (self.hammingWeight(num), num))
        
        return arr

    def hammingWeight(self, num: int) -> int:
        num = (num & 0x5555) + ((num>>1) & 0x5555)
        num = (num & 0x3333) + ((num>>2) & 0x3333)
        num = (num & 0x0f0f) + ((num>>4) & 0x0f0f)
        num = (num & 0x00ff) + ((num>>8) & 0x00ff)

        return num
