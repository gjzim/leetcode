from typing import List
from random import randint

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k + 1)

    def quick_select(self, arr, lo, hi, k):
        if lo == hi:
            return arr[lo]
        
        pindex = self.partition(arr, lo, hi)

        if k > pindex:
            return self.quick_select(arr, pindex + 1, hi, k)
        elif k < pindex:
            return self.quick_select(arr, lo, pindex - 1, k)
        else:
            return arr[pindex]

    def partition(self, arr, lo, hi):
        rand_index = randint(lo, hi)
        arr[rand_index], arr[hi] = arr[hi], arr[rand_index]
        pivot = arr[hi]

        i = lo
        for j in range(lo, hi):
            if arr[j] <= pivot:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1

        arr[hi], arr[i] = arr[i], arr[hi]
        
        return i
