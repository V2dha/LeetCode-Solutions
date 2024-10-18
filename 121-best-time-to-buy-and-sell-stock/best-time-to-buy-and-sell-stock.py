class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        lmin = prices[0]

        if len(prices) == 1:
            return max_profit

        for i in range(len(prices)):
            if prices[i] < lmin:
                lmin = prices[i]
            profit = prices[i] - lmin
            max_profit = max(profit, max_profit)

        return max_profit

        # max_profit = 0

        # if len(prices) == 1:
        #     return max_profit

        # if prices == sorted(prices, reverse=True):
        #     return max_profit

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j]-prices[i]
        #         if profit > max_profit:
        #             max_profit = profit

        # return max_profit

