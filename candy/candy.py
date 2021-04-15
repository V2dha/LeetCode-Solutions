class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)-1
        l, r = [1]*len(ratings), [1]*len(ratings)
        count = 0
        
        for i in range(n):
            if ratings[i+1] > ratings[i]:
                l[i+1] = l[i] + 1
            if ratings[n-1-i] > ratings[n-i]:
                r[n-1-i] = r[n-i] + 1
        
        for i in range(len(l)):
            count += max(l[i], r[i])
        
        return count