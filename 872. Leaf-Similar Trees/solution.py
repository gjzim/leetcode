from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def _dfs(root, leaves):
            if root is None: return leaves

            if not root.left and not root.right:
                leaves.append(root.val)

            _dfs(root.left, leaves)
            _dfs(root.right, leaves)
            
            return leaves

        return _dfs(root1, []) == _dfs(root2, [])
        

def create_tree_from_list(nums, limit):
    if not nums: return None

    root = TreeNode(nums[0])
    nodes = deque([root])
    i = 1

    while i < len(nums):
        try:
            cur = nodes.popleft()
        except:
            return root

        if nums[i] <= limit:
            cur.left = TreeNode(nums[i])
            nodes.append(cur.left)

        if i+1 < len(nums) and nums[i+1] <= limit:
            cur.right = TreeNode(nums[i+1])
            nodes.append(cur.right)

        i += 2

    return root

null = 110
root1 = create_tree_from_list([3,5,1,6,2,9,8,null,null,7,4], 100)
root2 = create_tree_from_list([3,5,1,6,2,9,8,null,null,7,1], 100)
sol = Solution()
sol.leafSimilar(root1, root2)
