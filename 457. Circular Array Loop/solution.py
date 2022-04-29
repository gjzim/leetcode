from typing import List
import collections

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(len(nums)):
            loopDirection = nums[i] >= 0
            slow = fast = i

            while True:
                slow = self.getNextIndex(nums, n, loopDirection, slow)
                fast = self.getNextIndex(nums, n, loopDirection, fast)
                if fast != -1:
                    fast = self.getNextIndex(nums, n, loopDirection, fast)

                if slow == -1 or fast == -1 or slow == fast:
                    break

            if slow != -1 and slow == fast:
                return True

        return False

                
    def getNextIndex(self, nums, n, loopDirection, index):
        direction = nums[index] >= 0
        nextIndex = (index + nums[index]) % n
        
        if loopDirection != direction or index == nextIndex:
            return -1

        return nextIndex
