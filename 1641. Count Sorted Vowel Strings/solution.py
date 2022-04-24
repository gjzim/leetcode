class Solution:
    def countVowelStrings_dp_matrix(self, n: int) -> int:
        grid = [[i for i in range(1, 6)] for _ in range(n)]

        for row in range(1, n):
            for col in range(1, 5):
                grid[row][col] = grid[row][col - 1] + grid[row - 1][col]

        return grid[n - 1][4]

    def countVowelStrings(self, n: int) -> int:
        row = [i for i in range(1, 6)]

        for _ in range(1, n - 1):
            for cell in range(1, 5):
                row[cell] += row[cell - 1]

        return sum(row)

        
