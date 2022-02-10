from typing import List
import collections

class Solution:
    def findDuplicate_add_by_length(self, nums: List[int]) -> int:
        dup, l = 0, len(nums)
        for i in nums: nums[i % l - 1] += l

        for i, v in enumerate(nums):
            if v > 2 * l: dup = i + 1
            nums[i] = v % l

        return dup

    def findDuplicate_arr_as_hashmap(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]

        return nums[0]

    def findDuplicate_bs(self, nums: List[int]) -> int:
        low, high = 1, len(nums)
        res = -1

        while low <= high:
            mid = low + (high - low) // 2
            
            lesser_count = 0
            for i in nums:
                lesser_count += i <= mid

            if lesser_count > mid:
                res = mid
                high = mid - 1
            else:
                low = mid + 1               
        
        return res

    def findDuplicate_slow_fast(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow

    def findDuplicate_bits(self, nums: List[int]) -> int:
        dup, n  = 0, len(nums) - 1
        bits = n.bit_length()

        for bit in range(bits):
            mask = 1 << bit
            base_count, nums_count = 0, 0

            for i in range(n + 1):
                if i & mask: base_count += 1
                if nums[i] & mask: nums_count += 1

            if nums_count > base_count:
                dup |= mask

        return dup
