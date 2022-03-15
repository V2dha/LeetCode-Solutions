class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Approach 1 - Using Combination and Maths
        1. Total number of paths to choose from is down (m-1) and right (n-1) i.e N = (m+n-2)
        2. Choose either m-1 path or either n-1 path i.e m+n-2 C m-1 or n-1
        3. Initialise res = 1 and run loop from 1 til r
        4. res = res * (N-r+i)/i  return res
        Time Complexity - O(N)
        Space Complexity - O(1)
        """
        N = n+m-2
        r = m-1
        res = 1
        for i in range(1, r+1):
            res = res*(N-r+i)//i
        return res

        """
        Approach 2 - Using Dynamic Programming in recursion
        1. Initialise dp[m][n] as 1 to store the visited coordinates and paths
        2. Same base conditions as in recursion
        3. If dp[i][j] != 1 then return dp[i][j] ie if it is visited
        4. else return dp[i][j] = func(i+1, j, m, n, dp) + func(i, j+1, m, n, dp) 
        5. return dp[0][0]
        Time Complexity - O(N*M)
        Space Compexity - O(N*M) (visited coord + recursion stack)
        """     
        def countPaths(self, i, j, m, n, dp):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if dp[i][j] != 1: return dp[i][j]
            else:
                dp[i][j] = self.countPaths(i, j, m, n, dp) + self.countPaths(i, j, m, n, dp)
                return dp[i][j]

        """
        Approach 1 - Using recursion 
        1. set base condition if the i or j moves out of bound
        2. set base condition if i and j reaches the last cell
        3. call recursive function on down dir i+1 and right dir j+1 and add them
        Time Complexity - Exponential (TLE)
        Space Complexity - Exponential stack space
        """
        def countPaths(self, i, j, m, n):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            else:
                return self.countPaths(i+1, j, m, n) + self.countPaths(i, j+1, m, n)
        