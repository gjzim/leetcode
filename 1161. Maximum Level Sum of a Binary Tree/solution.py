from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level, maxSum, maxLevel = 0, -math.inf, 0
        nodes = [root]
        
        while nodes:            
            children, curSum = [], 0
            
            for node in nodes:
                curSum += node.val
                
                if node.left: 
                    children.append(node.left)
                if node.right: 
                    children.append(node.right)
            
            nodes = children
            level += 1
            
            if curSum > maxSum:
                maxSum, maxLevel = curSum, level
            
        return maxLevel
