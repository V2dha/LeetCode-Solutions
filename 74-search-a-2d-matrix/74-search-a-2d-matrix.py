class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach - Consider the matrix as a list with m*n values
        1. Initialise low = 0, high = m*n-1 and while low <= high mid = low+high/2
        2. access matrix val by mat[mid/m][mid%n] if target < mat val -> high=mid-1 
        3. elif target > then low = mid+1 and if equal then return True
        Time Complexity - O(logM*N) (since M*N are all values in matrix)
        Space Complexity - O(1)
        """
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n-1
        while low <= high:
            mid = (low+high)//2
            x = matrix[mid//n][mid%n]
            if target < x:
                high = mid-1
            elif target > x:
                low = mid+1
            else:
                return True
        return False
        
#         """
#         Approach - 1. Find the row target may exist by comparing with last val of row
#         2. Apply Binary Search on that row if found return True else return False
#         Time Complexity - O(M) + O(logN) (Traversing each row and binary search on column)
#         Space Complexity - O(1)
#         """
#         m = len(matrix)
#         n = len(matrix[0])
#         for i in range(m):
#             row = matrix[i]
#             if target > row[n-1]:
#                 continue
#             else:
#                 l = 0
#                 r = n-1
#                 while l <= r:
#                     mid = (l+r)//2
#                     if target < row[mid]:
#                         r = mid-1
#                     elif target > row[mid]:
#                         l = mid+1
#                     else:
#                         return True
#         return False
        