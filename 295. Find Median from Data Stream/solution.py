from heapq import *

class MedianFinder:
    def __init__(self):
        # firstHalf is gonna store the first half of the
        # ordered numbers, so it's a max-heap.
        self.firstHalf = []
        # secondHalf is gonna store the first half of the
        # ordered numbers, so it's a min-heap.
        self.secondHalf = []

    def addNum(self, num: int) -> None:
        if not self.firstHalf or -self.firstHalf[0] >= num:
            heappush(self.firstHalf, -num)
        else:
            heappush(self.secondHalf, num)

        # Either both the heaps will have equal number of elements
        # or max-heap will have one more element than the min-heap
        if len(self.firstHalf) > len(self.secondHalf) + 1:
            heappush(self.secondHalf, -heappop(self.firstHalf))
        elif len(self.secondHalf) > len(self.firstHalf):
            heappush(self.firstHalf, -heappop(self.secondHalf))

    def findMedian(self) -> float:
        if len(self.firstHalf) == len(self.secondHalf):
            return -self.firstHalf[0] / 2.0 + self.secondHalf[0] / 2.0

        return -self.firstHalf[0] / 1.0
