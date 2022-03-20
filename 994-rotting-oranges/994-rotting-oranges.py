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
        minutes = 0   #to store time
        total = 0     #total number of fresh oranges
        count = 0     #total number of oranges that can be rotten
        rotten = []   #Queue to store position of rottened oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0: #count fresh oranges
                    total += 1
                if grid[i][j] == 2: #store position of rotten oranges
                    rotten.append([i, j])
        dx = [0,0,1,-1]  #directions
        dy = [1,-1,0,0]
        while rotten:    #queue is not empty
            k = len(rotten)  
            count += k   #add the oranges that have been rottened
            while k:
                x = rotten[0][0]
                y = rotten[0][1]
                rotten.pop(0)
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    #if index out of bounds or grid doesn't contain fresh oranges then continue
                    if nx <0 or ny<0 or nx>=m or ny>=n or grid[nx][ny] !=1:  
                        continue
                    #else mark it rotten and add the position to queue
                    grid[nx][ny] = 2
                    rotten.append([nx,ny])
                k-=1
            #count the total time of iteration of queue
            if rotten:
                minutes += 1

        return minutes if total == count else -1
        