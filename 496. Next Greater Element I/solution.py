from typing import List
import random

class Solution:
    def nextGreaterElementBF(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tab = {}
        for i in range(len(nums2)):
            tab[nums2[i]] = -1
            
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    tab[nums2[i]] = nums2[j]
                    break

        for i, num in enumerate(nums1):
            nums1[i] = tab[num]
            
        return nums1

    def nextGreaterElementBF2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tab = {}
        for i, num in enumerate(nums1):
            tab[num] = i

        for i, num in enumerate(nums2):
            if num not in tab:
                continue
            
            nums1[tab[num]] = -1
            
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    nums1[tab[num]] = nums2[j]
                    break
            
        return nums1

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tab, stack = {}, []
        for num in nums2:
            while stack and num > stack[-1]:
                tab[stack.pop()] = num

            stack.append(num)

        # while stack:
            # tab[stack.pop()] = -1

        for i, num in enumerate(nums1):
            # nums1[i] = tab[num]
            nums1[i] = tab.get(num, -1)
            
        return nums1


def generate_test(sol):
    maxLength = 1000
    numMin = 0
    numMax = 10000
    
    length = random.randint(1, maxLength)
    nums = random.sample(range(numMin, numMax), length)
    nums2 = nums[:random.randint(1, length)]
    random.shuffle(nums2)
    
    if sol.nextGreaterElementBF(nums2[::], nums) != sol.nextGreaterElement(nums2[::], nums):
        print('error')
    

sol = Solution()
for i in range(100):    
    generate_test(sol)    
