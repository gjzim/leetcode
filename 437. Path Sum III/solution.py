from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # Solve using dfs
    def pathSum_dfs(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, target, path):
            if node is None: return 0

            path.append(node.val)
            
            pathsum = count = 0
            for i in range(len(path) - 1, -1, -1):
                pathsum += path[i]
                if pathsum == target:
                    count += 1
            
            count += dfs(node.left, target, path) 
            count += dfs(node.right, target, path)

            path.pop()

            return count

        return dfs(root, targetSum, [])

    # Solve using prefix sum
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:       
        seen = collections.defaultdict(int)
        seen[0] = 1

        return self.findPathSum(root, 0, targetSum, seen)
    
    def findPathSum(self, node, cursum, target, seen):
        if node is None: return 0        
        
        cursum += node.val
        count = seen[cursum - target]
        
        seen[cursum] += 1
        
        count += self.findPathSum(node.left, cursum, target, seen)
        count += self.findPathSum(node.right, cursum, target, seen)
           
        seen[cursum] -= 1

        return count
