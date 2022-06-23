from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        pre = self.createPresumMatrix(mat, rows, cols)
        
        for row in range(rows):
            for col in range(cols):
                startRow, startCol = max(row - k, 0), max(col - k, 0)
                endRow, endCol = min(row + k + 1, rows), min(col + k + 1, cols)
                mat[row][col] =  pre[endRow][endCol] - pre[startRow][endCol] - pre[endRow][startCol] + pre[startRow][startCol]
        
        return mat

    def createPresumMatrix(self, mat, rows, cols):
        pre = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for row in range(rows):
            for col in range(cols):
                pre[row + 1][col + 1] = mat[row][col] + pre[row][col + 1] + pre[row + 1][col] - pre[row][col]

        return pre
