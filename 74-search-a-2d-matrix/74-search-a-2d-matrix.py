class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            row = matrix[i]
            if target > row[n-1]:
                continue
            else:
                for j in range(n):
                    if row[j] == target:
                        return True
        return False
        