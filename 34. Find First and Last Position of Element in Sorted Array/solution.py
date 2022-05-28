from typing import List

class Solution:
    def searchRange_mine(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                beforeRange = self.searchRange(nums[:mid], target)
                afterRange = self.searchRange(nums[mid+1:], target)

                lowIndex = mid if beforeRange[0] == -1 else beforeRange[0]
                highIndex = mid if afterRange[0] == -1 else afterRange[1] + mid + 1

                return [lowIndex, highIndex]

        return [-1, -1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

        result[0] = self.deepBinarySearch(nums, target, 'left')
        if result[0] != -1:
            result[1] = self.deepBinarySearch(nums, target, 'right')

        return result

    def deepBinarySearch(self, nums, target, direction):
        result = -1
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                result = mid
                
                if direction == 'left':
                    hi = mid - 1
                elif direction == 'right':
                    lo = mid + 1

        return result
                
