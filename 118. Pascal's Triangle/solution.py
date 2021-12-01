from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1]*(i+1)
            triangle.append(row)
            
            for j in range(1,i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
            
        return triangle


sol = Solution()
triangle = sol.generate(30)
for row in triangle:
    print(row)
