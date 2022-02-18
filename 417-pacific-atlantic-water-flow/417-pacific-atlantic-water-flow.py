class Solution:
    def dfs(self, i, j, n, m, heights, vis):
        if i<0 or j<0 or i>=n or j>=m:
            return
        
        vis[i][j] = 1
        
        #Down
        if i+1 < n and heights[i][j] <= heights[i+1][j] and vis[i+1][j] == 0:
            self.dfs(i+1, j, n, m, heights, vis)
            
        #Right
        if j+1 < m and heights[i][j] <= heights[i][j+1] and vis[i][j+1] == 0:
            self.dfs(i, j+1, n, m, heights, vis)
            
        #Up
        if i-1 >= 0 and heights[i][j] <= heights[i-1][j] and vis[i-1][j] == 0:
            self.dfs(i-1, j, n, m, heights, vis)
            
        #Left
        if j-1 >= 0 and heights[i][j] <= heights[i][j-1] and vis[i][j-1] == 0:
            self.dfs(i, j-1, n, m, heights, vis)
        
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        if n == 0:
            return 
        m = len(heights[0])
        pac = [[0 for i in range(m)] for j in range(n)]
        atl = [[0 for i in range(m)] for j in range(n)]
        
        #Pacific Ocean
        for i in range(n):
            self.dfs(i, 0, n, m, heights, pac)
        for i in range(m):
            self.dfs(0, i, n, m, heights, pac)
            
        #Atlantic Ocean 
        for i in range(n):
            self.dfs(i, m-1, n, m, heights, atl)
        for i in range(m):
            self.dfs(n-1, i, n, m, heights, atl)
            
        ans = []
        for i in range(n):
            for j in range(m):
                if pac[i][j] and atl[i][j]:
                    ans.append([i, j])
        return ans
        
        