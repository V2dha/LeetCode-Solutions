class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Approach - 1. First transpose the matrix (second loop 0 - i)
        2. Reverse each row using two ptr l and r
        Time Complexity - O(N*N) (Both for transpose & rev)
        Space Complexity - O(1) 
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        for i in range(n):
            l = 0
            r = n-1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1
        
        