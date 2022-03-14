from typing import List

class Solution:
    def minOperations_bf(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n

        for i, c in enumerate(boxes):
            if c == '0':
                continue

            for j in range(n):
                result[j] += abs(j - i)

        return result

    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n

        leftCount = leftCost = 0
        for i in range(1, n):
            if boxes[i - 1] == '1':
                leftCount += 1

            leftCost += leftCount
            result[i] = leftCost

        rightCount = rightCost = 0
        for i in range(n - 2, -1, -1):
            if boxes[i + 1] == '1':
                rightCount += 1

            rightCost += rightCount
            result[i] += rightCost
                
        return result

