from typing import List

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        xors = []
        
        for i in range(m):
            for j in range(n):
                a = matrix[i - 1][j] if i > 0 else 0
                b = matrix[i][j - 1] if j > 0 else 0
                c = matrix[i - 1][j - 1] if i > 0 and j > 0 else 0
                matrix[i][j] ^= a ^ b ^ c
                xors.append(matrix[i][j])

        xors.sort(reverse = True)
        return xors[k - 1]

        
