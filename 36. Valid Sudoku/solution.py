from typing import List
import collections

class Solution:
    def isValidSudoku_mine(self, board: List[List[str]]) -> bool:
        # verify rows
        for row in range(9):
            if not self.isValidRow(row, board):
                return False
                
        # verify columns
        for col in range(9):
            if not self.isValidColumn(col, board):
                return False
            
        # verify subgrids
        for i in (0, 3, 6):
            rowStart, rowEnd = i, i + 3
            for j in (0, 3, 6):
                colStart, colEnd = j, j + 3
                grid = [
                    (rowStart, rowEnd),
                    (colStart, colEnd)
                ]
                    
                if not self.isValidGrid(grid, board):
                    return False

        return True

    def isValidRow(self, row, board):
        seen = {}
        for col in range(9):
            if board[row][col] == '.':
                continue

            if board[row][col] in seen:
                return False

            seen[board[row][col]] = True            
            
        return True

    def isValidColumn(self, col, board):
        seen = {}
        for row in range(9):
            if board[row][col] == '.':
                continue

            if board[row][col] in seen:
                return False

            seen[board[row][col]] = True            
            
        return True

    def isValidGrid(self, grid, board):
        rowStart, rowEnd = grid[0]
        colStart, colEnd = grid[1]
        seen = {}

        for row in range(rowStart, rowEnd):
            for col in range(colStart, colEnd):
                if board[row][col] == '.':
                    continue

                if board[row][col] in seen:
                    return False

                seen[board[row][col]] = True
        
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
        return True
