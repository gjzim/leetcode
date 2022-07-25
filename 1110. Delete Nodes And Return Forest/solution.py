from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:       
        def reduce(node):
            if node is None: return None
            
            deletable = node.val in to_delete
            
            if node.left:
                if deletable and node.left.val not in to_delete: 
                    result.append(node.left)                
                node.left = reduce(node.left)
                
            if node.right:
                if deletable and node.right.val not in to_delete: 
                    result.append(node.right)                
                node.right = reduce(node.right)
                
            return None if deletable else node
            
        result, to_delete = [], set(to_delete)
        if reduce(root): result.append(root)
        return result
