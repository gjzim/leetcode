from typing import List

class Solution:
    def getRow_1(self, rowIndex: int) -> List[int]:
        pt = []

        for row in range(rowIndex+1):
            pt.append([1]*(row+1))
            for col in range(row+1):
                if col > 0 and col < row:
                    pt[row][col]= pt[row-1][col-1] + pt[row-1][col]
                    
        return pt[rowIndex]

    def getRow_2(self, rowIndex: int) -> List[int]:
        prev, cur = [1], [1]

        for row in range(1, rowIndex+1):
            cur = [1]*(row+1)
            for col in range(row+1):
                if col > 0 and col < row:
                    cur[col]= prev[col-1] + prev[col]

            prev = cur
                    
        return cur

    def getRow(self, rowIndex: int) -> List[int]:
        row = [0]*(rowIndex+1)
        row[0] = 1

        for r in range(1, rowIndex+1):
            for c in range(r, 0, -1):
                row[c] += row[c-1]

        return row
    
sol = Solution()
print(sol.getRow(4))
