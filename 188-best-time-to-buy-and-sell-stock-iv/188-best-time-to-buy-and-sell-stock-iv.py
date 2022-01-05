class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        evenProfit = [0 for d in prices]
        oddProfit = [0 for d in prices]
        
        for t in range(1, k+1):
            if t%2==0:
                currentProfit = evenProfit
                prevProfit = oddProfit
            else:
                currentProfit = oddProfit
                prevProfit = evenProfit
            maxSoFar = float("-inf")
            for d in range(1, len(prices)):
                maxSoFar = max(maxSoFar, prevProfit[d-1] - prices[d-1])
                currentProfit[d] = max(currentProfit[d-1], prices[d] + maxSoFar)
        return evenProfit[-1] if k%2==0 else oddProfit[-1]
        