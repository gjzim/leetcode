from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []        

    def next(self) -> int:
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
            
        self.root = self.stack.pop()
        val = self.root.val
        
        self.root = self.root.right
        
        return val

    def hasNext(self) -> bool:
        return self.root or self.stack

class BSTIterator_Morris_Traverse:
    def __init__(self, root: Optional[TreeNode]):
        self.cur = root    

    def next(self) -> int:
        if self.cur.left is None:
            val = self.cur.val
            self.cur = self.cur.right
        else:
            pre = self.cur.left
            
            while pre.right and pre.right != self.cur:
                pre = pre.right

            if pre.right is None:
                pre.right = self.cur
                self.cur = self.cur.left
            else:
                pre.right = None
                val = self.cur.val
                self.cur = self.cur.right

        return val

    def hasNext(self) -> bool:
        return self.cur is not None
