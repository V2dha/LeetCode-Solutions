class Solution:
    """
Approach -
Sort the array in descending order and add the first two items after ordering them into group of 3 iteratively
Return the minCost if it is a multiple of 3 else if it is not then add the cost of the remaining items
    """
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1 or n == 2:
            return sum(cost)
        cost.sort(reverse=True)
        if n == 3:
            return cost[0]+cost[1]
        minCost = 0
        for i in range(2, n, 3):
            minCost += cost[i-2] + cost[i-1]
            
        if n%3==0:
            return minCost
        else:
            index = n - n%3
            return minCost + sum(cost[index:])
                