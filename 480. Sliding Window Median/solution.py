from typing import List
from heapq import *

class Solution:
    def __init__(self):
        self.firstHalf = []
        self.secondHalf = []
    
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []

        for i, num in enumerate(nums):
            self.addNum(num)            

            if i >= k:
                self.removeNum(nums[i - k])

            if i >= k - 1:
                result.append(self.findMedian())
                
        return result

    def addNum(self, num: int) -> None:
        if not self.firstHalf or -self.firstHalf[0] >= num:
            heappush(self.firstHalf, -num)
        else:
            heappush(self.secondHalf, num)

        self.reorganize()

    def reorganize(self):
        if len(self.firstHalf) > len(self.secondHalf) + 1:
            heappush(self.secondHalf, -heappop(self.firstHalf))
        elif len(self.secondHalf) > len(self.firstHalf):
            heappush(self.firstHalf, -heappop(self.secondHalf))

    def removeNum(self, num: int) -> None:
        if -self.firstHalf[0] >= num:
            heap, num = self.firstHalf, -num
        else:
            heap = self.secondHalf
            
        i = heap.index(num)
        heap[i] = heap[-1]
        del heap[-1]
        
        if i < len(heap):
          heapq._siftup(heap, i)
          heapq._siftdown(heap, 0, i)

        self.reorganize()
            

    def findMedian(self) -> float:
        if len(self.firstHalf) == len(self.secondHalf):
            return -self.firstHalf[0] / 2.0 + self.secondHalf[0] / 2.0

        return -self.firstHalf[0] / 1.0
