class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Approach - Bottom Up
        1. Calculate for first two n = 1 and n = 2 and constantly calculate steps for 
        each step iteratively till n
        2. Return the last step
        
        
        Time Complexity = O(n)
        
        """
        if n == 1 or n == 2:
            return n
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]