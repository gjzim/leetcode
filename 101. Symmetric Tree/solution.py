from typing import List, Optional
from collections import deque
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pairs = deque([(root.left, root.right)])

        while pairs:
            (left, right) = pairs.popleft()          

            if left and right:
                if left.val != right.val:
                    return False

                pairs.append((left.left, right.right))
                pairs.append((left.right, right.left))

            elif not left and not right:
                pass
            else:
                return False
        
        return True

def create_tree_from_list(nums, limit=100):
    if not nums: return None

    root = TreeNode(nums[0])
    nodes = deque([root])
    i = 1

    while i < len(nums):
        try:
            cur = nodes.popleft()
        except:
            return root

        if nums[i] and nums[i] <= limit:
            cur.left = TreeNode(nums[i])
            nodes.append(cur.left)

        if i+1 < len(nums) and nums[i+1] and nums[i+1] <= limit:
            cur.right = TreeNode(nums[i+1])
            nodes.append(cur.right)

        i += 2

    return root

sol = Solution()
null = None
print(sol.isSymmetric(create_tree_from_list([5,4,1,null,1,null,4,2,null,2,null])))
print(sol.isSymmetric(create_tree_from_list([1,2,2,3,4,4,3])))
