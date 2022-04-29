class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned.val == target.val:
            return cloned
        
        result = None
        if original.left:
            result = self.getTargetCopy(original.left, cloned.left, target)
            
        if result is None and original.right:
            result = self.getTargetCopy(original.right, cloned.right, target)
            
        return result

