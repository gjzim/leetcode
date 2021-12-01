from typing import List
import random

class Solution:
    def findKthPositive_slow(self, arr: List[int], k: int) -> int:
        i = 0

        for n in range(1, arr[-1]+1):
            if n == arr[i]:
                i += 1
            else:
                k -= 1

            if k == 0: break

        return n+k

    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, h = 0, len(arr)-1
        
        while l <= h:
            m = l + ((h-l)//2)
            
            if arr[m]-(m+1) < k:
                l = m + 1
            else:
                h = m - 1
            
        return k+l


def generate_test(sol):
    length = random.randint(1, 800)
    arr = random.sample(list(range(1,1000)), k=length)
    k = random.randint(1, 1000)
    arr.sort()

    if sol.findKthPositive_slow(arr, k) != sol.findKthPositive(arr, k):
        print(sol.findKthPositive_slow(arr, k))
        print(sol.findKthPositive(arr, k))
        print(arr, k, 'error')


sol = Solution()
for i in range(1000):
    generate_test(sol)
