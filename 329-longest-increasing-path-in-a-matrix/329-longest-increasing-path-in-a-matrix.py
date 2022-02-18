class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=uLjO2LUlLN4
        Approach - DFS and Memoization
        Time Complexity = O(N*M) without memoization O(2^N)
        Space Complexity = O(N*M) since we are using cache
        """
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        cache = [[0 for i in range(m)] for j in range(n)]
        longestPath = 0
        
        for i in range(n):
            for j in range(m):
                longest = self.dfs(i, j, n, m, matrix, cache)
                longestPath = max(longest, longestPath)
                
        return longestPath
    
    def dfs(self, i, j, n, m, matrix, cache):
        if cache[i][j]:
            return cache[i][j]
        
        max_path = 0
        for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
            if x >= 0 and y >= 0 and x < n and y < m and matrix[x][y] > matrix[i][j]:
                longest = self.dfs(x, y, n, m, matrix, cache)
                max_path = max(longest, max_path)
                
        cache[i][j] = max_path+1
                
        return cache[i][j]
        