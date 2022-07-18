from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(row, col):
            if row >= m or col >= n or board[row][col] != 'X': 
                return 0
                        
            board[row][col] = '-'
            return 1 + dfs(row, col + 1) + dfs(row + 1, col)
        
        result, m, n = 0, len(board), len(board[0])
        for row in range(m):
            for col in range(n):
                if dfs(row, col):
                    result += 1
                    
        return result
