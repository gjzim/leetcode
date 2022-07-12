from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[el ^ 1 for el in row[::-1]] for row in image]
