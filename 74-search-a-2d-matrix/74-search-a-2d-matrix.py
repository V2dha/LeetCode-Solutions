class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach - 1. Find the row target may exist by comparing with last val of row
        2. Apply Binary Search on that row if found return True else return False
        Time Complexity - O(M) + O(logN) (Traversing each row and binary search on column)
        Space Complexity - O(1)
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            row = matrix[i]
            if target > row[n-1]:
                continue
            else:
                l = 0
                r = n-1
                while l <= r:
                    mid = (l+r)//2
                    if target < row[mid]:
                        r = mid-1
                    elif target > row[mid]:
                        l = mid+1
                    else:
                        return True
        return False
        