from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateTreesHelper(1, n)

    def generateTreesHelper(self, start, end):
        if start > end: return [None]

        trees = []
        for i in range(start, end+1):
            leftTrees = self.generateTreesHelper(start, i-1)
            rightTrees = self.generateTreesHelper(i+1, end)

            for left in leftTrees:
                for right in rightTrees:
                    trees.append(TreeNode(i, left, right))
                    
        return trees
