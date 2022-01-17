from typing import List

class Solution:
    def merge_bf(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return

        nums1cp = nums1[:m]
        i, j, k = 0, 0, 0

        while j < m and k < n:
            if nums1cp[j] < nums2[k]:
                nums1[i] = nums1cp[j]
                j += 1
            else:
                nums1[i] = nums2[k]
                k += 1

            i += 1

        while j < m:
            nums1[i] = nums1cp[j]
            i, j = i+1, j+1

        while k < n:
            nums1[i] = nums2[k]
            i, k = i+1, k+1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p, m, n = m+n-1, m-1, n-1
        
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[p] = nums1[m]
                p, m = p-1, m-1
            else:
                nums1[p] = nums2[n]
                p, n = p-1, n-1

        while n >= 0:
            nums1[p] = nums2[n]
            p, n = p-1, n-1

    def merge_concise(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:       
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
                
        if n > 0:
            nums1[:n] = nums2[:n]
