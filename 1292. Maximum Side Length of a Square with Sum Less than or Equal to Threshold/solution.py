from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])
        pre = self.createPresumMatrix(mat, rows, cols)
        
        def valid(l):
            for r1 in range(rows - l + 1):
                for c1 in range(cols - l + 1):
                    r2, c2 = r1 + l, c1 + l
                    if pre[r2][c2] - pre[r1][c2] - pre[r2][c1] + pre[r1][c1] <= threshold:
                        return True

            return False

        left, right = 1, min(rows, cols) + 1
        while left < right:
            mid = left + (right - left) // 2

            if valid(mid):
                left = mid + 1
            else:
                right = mid

        return left - 1 if left > 1 else 0
        
    def createPresumMatrix(self, mat, rows, cols):
        pre = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for row in range(rows):
            for col in range(cols):
                pre[row + 1][col + 1] = mat[row][col] + pre[row][col + 1] + pre[row + 1][col] - pre[row][col]

        return pre

sol = Solution()
mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
print(sol.maxSideLength([[10]], 5))
