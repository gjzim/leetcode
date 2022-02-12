from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [0] + [math.inf] * amount

        for i in range(0, amount + 1):            
            for coin in coins:
                if i + coin <= amount and amounts[i + coin] > amounts[i] + 1:
                    amounts[i + coin] = amounts[i] + 1
            
        return -1 if amounts[amount] == math.inf else amounts[amount]

    def coinChange_looking_backward(self, coins: List[int], amount: int) -> int:
        amounts = [0] + [math.inf] * amount

        for i in range(1, amount + 1):            
            for coin in coins:
                if i - coin >= 0 and amounts[i] > amounts[i - coin] + 1:
                    amounts[i] = amounts[i - coin] + 1
            
        return -1 if amounts[amount] == math.inf else amounts[amount]
