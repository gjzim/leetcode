from typing import List
import random

class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        buy, sell, profit = prices[0], 0, 0

        for i in range(len(prices)-1):                        
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i+1]

            sell = max(sell, prices[i+1])
            profit = max(profit, sell-buy)

        return profit

    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0

        for i in range(1, len(prices)):                        
            profit = max(profit, prices[i]-buy)
            buy = min(buy, prices[i])

        return profit

    def bruteForce(self, prices):
        profit = 0

        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j] - prices[i])                
                
        return profit
    

def generate_test(sol):
    length = random.randint(1,1000)
    nums = random.sample(range(0, 10000), length)

    mp = sol.maxProfit(nums)
    mp_1 = sol.maxProfit_1(nums)
    if mp != mp_1:        
        print('error', mp, mp_1)
        print(nums)

sol = Solution()
for i in range(1000):    
    generate_test(sol)
    
