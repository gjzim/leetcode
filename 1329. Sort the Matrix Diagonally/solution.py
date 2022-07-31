from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        for row in range(1, m):
            for col in range(1, n):
                i, j = row, col
                
                while i > 0 and j > 0 and mat[i][j] < mat[i - 1][j - 1]:
                    mat[i][j], mat[i - 1][j - 1] = mat[i - 1][j - 1], mat[i][j]
                    i, j = i - 1, j - 1                    
        
        return mat
        
