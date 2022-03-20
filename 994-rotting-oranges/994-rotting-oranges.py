class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Approach - BFS Breadth First Search Using Queue
        Time Complexity - O(N*N)
        Space Complexity - O(N*N)
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        minutes = 0
        total = 0
        count = 0
        rotten = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    total += 1
                if grid[i][j] == 2:
                    rotten.append([i, j])
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while rotten:
            k = len(rotten)
            count += k
            while k:
                x = rotten[0][0]
                y = rotten[0][1]
                rotten.pop(0)
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if nx <0 or ny<0 or nx>=m or ny>=n or grid[nx][ny] !=1:
                        continue
                    grid[nx][ny] = 2
                    rotten.append([nx,ny])
                k-=1
            if rotten:
                minutes += 1
        return minutes if total == count else -1
        