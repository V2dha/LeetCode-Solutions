class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Approach - 1. Traverse the matrix and if the row or col contains 0 then set the corresponding first row or col as 0
        2. Traverse the matrix again and see if the first row or col contains 0 then set as 0
        3. Traverse the matrix for the first row and col if they contain zero
        Time Complexity = O(MN)
        Space Complexity - O(1)
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_zero = True
                    if j == 0:
                        first_col_zero = True
                    matrix[i][0] = matrix[0][j] = 0 #set the first row or col as zero 
                    
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
          
        #Traverse the first row or column if its zero
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
                
        return matrix
#         """
#         Approach - Use set to track the rows and columns that contain zero and then traverse again to set them as 0
#         Time Complexity = O(MN)
#         Space Complexity = O(M+N)
#         """
#         row = set()
#         col = set()
        
#         n, m = len(matrix), len(matrix[0])
        
#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 0:
#                     row.add(i)
#                     col.add(j)
                    
#         for i in range(n):
#             for j in range(m):
#                 if i in row or j in col:
#                     matrix[i][j] = 0
                    
#         return matrix