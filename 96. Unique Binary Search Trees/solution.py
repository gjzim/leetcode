class Solution:
    def numTrees_bf(self, n: int) -> int:
        def countTrees(start, end, memo):
            if start > end: return 1
            key = str(start) + ':' + str(end)
            if key in memo: return memo[key]
            
            count = 0
            for i in range(start, end+1):
                count += countTrees(start, i-1, memo) * countTrees(i+1, end, memo)

            memo[key] = count
            return count

        return countTrees(1, n, {})   

    def numTrees(self, n: int) -> int:
        table = [0] * (n+1)
        table[0] = table[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                table[i] += table[j-1] * table[i-j]

        return table[n]   

