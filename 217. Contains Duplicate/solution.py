class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        items = {}

        for i in nums:
            if i in items:
                return True

            items[i] = True

        return False
    
