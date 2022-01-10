from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = result = 0
        picked = {}

        for end, fruit in enumerate(fruits):
            picked[fruit] = picked.get(fruit, 0) + 1
    
            while len(picked) > 2:
                picked[fruits[start]] -= 1                
                if picked[fruits[start]] == 0: 
                    del picked[fruits[start]]

                start += 1
    
            result = max(result, end - start + 1)

        return result
