class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        profitsoFar = 0
        lmin = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lmin:
                lmin = prices[i]
            profitsoFar = prices[i] - lmin
            profit = max(profitsoFar, profit)
        return profit