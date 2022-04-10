from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None: return []
        
        result = []        
        def dfs(node, path, curSum):            
            if node is None: return
            
            curSum += node.val
            curPath = path + [node.val]

            if curSum == targetSum and not node.left and not node.right:                
                result.append(curPath)
            else:
                dfs(node.left, curPath, curSum)
                dfs(node.right, curPath, curSum)
                
        dfs(root, [], 0)
        return result
