class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Approach - Find the local minimum and get the maximum profit
        Iterate through the array and update the minimum price and maximum profit
        Time Complexity - O(N)
        Space Complexity - O(1)
        """
        profit = 0
        profitsoFar = 0
        lmin = prices[0]
        for i in range(1, len(prices)):
            lmin = min(prices[i], lmin)
            profitsoFar = prices[i] - lmin
            profit = max(profitsoFar, profit)
        return profit