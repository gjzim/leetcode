class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:        
        def convert(node):
            if node:               
                convert(node.right)                
                node.val += self.presum
                self.presum = node.val
                convert(node.left)

        self.presum = 0
        convert(root)
            
        return root

