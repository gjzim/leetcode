from typing import List

class Solution:
    def generateParenthesis_iter(self, n: int) -> List[str]:
        result = []
        queue = deque([('', 0, 0)])
        
        while queue:
            perm, openCount, closeCount = queue.popleft()
            
            if openCount == n and closeCount == n:
                result.append(perm)
            else:
                if openCount < n:
                    queue.append((perm + '(', openCount + 1, closeCount))
                
                if openCount > closeCount:
                    queue.append((perm + ')', openCount, closeCount + 1))
        
        return result

    def generateParenthesis(self, n: int) -> List[str]:                
        def backtrack(s = [], left = 0, right = 0):
            if len(s) == 2 * n:
                ans.append("".join(s))
            else:                
                if left < n:
                    s.append("(")
                    backtrack(s, left + 1, right)
                    s.pop()
                if right < left:
                    s.append(")")
                    backtrack(s, left, right + 1)
                    s.pop()

        ans = []
        backtrack()
        return ans
