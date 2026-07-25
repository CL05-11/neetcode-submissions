class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        # Brute force O(n^2)
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         max_profit = max(max_profit,prices[j]-prices[i])
        
        # return max_profit
        # two pointer solution where time O(n) and space O(1)
        maxprofit = 0
        l = prices[0]

        for r in range(len(prices)):
            maxprofit = max(maxprofit,prices[r]-l)
            l = min(l,prices[r])
        return maxprofit

