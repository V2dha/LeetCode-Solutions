# Find the local minima and store it as starting index. If not exists, return.
# Find the local maxima. and store it as an ending index. If we reach the end, set the end as the ending index.
# Update the solution (Increment count of buy-sell pairs)
# Repeat the above steps if the end is not reached.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Time Complexity = n
        i = 0
        maxProfit = 0
        n = len(prices)
        while i < n-1:
        # Find Local Minima
        # Note that the limit is (n-2) as we are
        # comparing present element to the next element
            while (i<n-1) and prices[i+1] <= prices[i]:
                i+=1
            
        # If we reached the end, break
        # as no further solution possible
            if i==n-1:
                break
                
        #Store local minima        
            buy = i
            i+=1
            
        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
            while (i<n) and prices[i] >= prices[i-1]:
                i+=1
                
        #Store local maxima
            sell = i-1
            
            maxProfit += prices[sell] - prices[buy]
            
        return maxProfit
        