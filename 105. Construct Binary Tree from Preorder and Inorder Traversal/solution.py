from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree_slow(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
                                
        root = TreeNode(preorder[0])        
        rpos = inorder.index(root.val)        
        root.left = self.buildTree(preorder[1:rpos + 1], inorder[:rpos])
        root.right = self.buildTree(preorder[rpos + 1:], inorder[rpos + 1: ])
        
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def convertToTree(left, right):
            nonlocal rootIndex
            if left > right: return None

            rootVal = preorder[rootIndex]
            root = TreeNode(rootVal)
            
            rootIndex += 1

            root.left = convertToTree(left, ioIndex[rootVal] - 1)
            root.right = convertToTree(ioIndex[rootVal] + 1, right)
            
            return root

        rootIndex = 0
        ioIndex = {n: i for i, n in enumerate(inorder)}

        return convertToTree(0, len(preorder) - 1)
