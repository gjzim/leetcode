from typing import List

class Solution:
    def countTriplets_bf(self, arr: List[int]) -> int:
        n, result = len(arr), 0
        for i in range(1, n):
            arr[i] ^= arr[i - 1]
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(j, n):
                    a = arr[j - 1] ^ (arr[i - 1] if i > 0 else 0)
                    b = arr[k] ^ arr[j - 1]
                    if a == b: result += 1

        return result

    def countTriplets_n2(self, arr: List[int]) -> int:
        arr.insert(0, 0)
        n = len(arr)        
        for i in range(1, n):
            arr[i] ^= arr[i - 1]
            
        result = 0        
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    result += j - i - 1

        return result

    def countTriplets(self, arr: List[int]) -> int:
        res = cur = 0
        count = {0: [1, 0]}
        
        for i, a in enumerate(arr):
            cur ^= a
            n, total = count.get(cur, [0, 0])
            res += i * n - total
            count[cur] = [n + 1, total + i + 1]

        return res    
