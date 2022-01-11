class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        profitSoFar = 0
        lmin = prices[0]
        for i in range(len(prices)):
            if prices[i] < lmin:
                lmin = prices[i]
                
            profitSoFar = prices[i] - lmin
            
            profit = max(profit, profitSoFar)
            
        return profit
        