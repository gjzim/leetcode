from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack, nums = [root], {}

        while stack:
            node = stack.pop()
            if not node: continue

            if (k - node.val) in nums:
                return True
            
            nums[node.val] = True
            stack.append(node.left)
            stack.append(node.right)

        return False

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right

        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val

        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val

        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)
      
        left, right = nextLeft(stLeft), nextRight(stRight)
        
        while left < right:
            if left + right == k: return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
                
        return False


