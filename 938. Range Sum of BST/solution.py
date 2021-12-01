from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST_mine(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, total = [root], 0

        while stack:
            node = stack.pop()
            if not node: continue

            if node.val >= low and node.val <= high:
                total += node.val

            stack.extend([node.left, node.right])

        return total
        

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None: return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        if root.right > high:
            return self.rangeSumBST(root.left, low, high)

        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        

