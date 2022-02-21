class Solution:
    def isValid(self, weights, days, mid):
        day = 1
        package = 0
        for i in range(len(weights)):
            package += weights[i]
            if package > mid:
                day += 1
                package = weights[i]
            if day > days:
                return 0
        return 1
            
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days == 1:
            return sum(weights)
        if len(weights) == days:
            return max(weights)
        
        start = max(weights)
        end = sum(weights)
        res = 0
        while start <= end:
            mid = (start+end)//2
            if self.isValid(weights, days, mid):
                res = mid
                end = mid-1
            else:
                start = mid+1
        return res