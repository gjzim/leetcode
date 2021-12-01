import random, collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        if len(nums1) < len(nums2):
            short, long = nums1, nums2
        else:
            short, long = nums2, nums1

        counts = collections.Counter(short)
        common = []
        
        for i in long:
            if i in counts and counts[i] > 0:
                common.append(i)
                counts[i] -= 1

        return common
            


        
