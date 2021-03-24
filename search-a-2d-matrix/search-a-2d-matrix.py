class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0]) 
        for arr in matrix:
            start = 0
            end = m-1
            if target <= arr[-1]:
                while start <= end:
                    mid = start + (end-start)//2
                    if arr[mid] == target:
                        return True
                    elif arr[mid] > target:
                        end = mid-1
                    else:
                        start = mid+1
        return False