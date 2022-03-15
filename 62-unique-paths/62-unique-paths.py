class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        self.countPaths(0, 0, m, n, dp)
        return dp[0][0]
        
    """
    Approach - Using recursion 
    1. set base condition if the i or j moves out of bound
    2. set base condition if i and j reaches the last cell
    3. call recursive function on down dir i+1 and right dir j+1 and add them
    Time Complexity - Exponential (TLE)
    Space Complexity - Exponential stack space
    """
    def countPaths(self, i, j, m, n, dp):
        if i >= m or j >= n:
            return 0
        if i == m-1 and j == n-1:
            return 1
        if dp[i][j] != 1:
            return dp[i][j]
        else:
            dp[i][j] = self.countPaths(i+1, j, m, n, dp) + self.countPaths(i, j+1, m, n, dp)
            return dp[i][j]
        