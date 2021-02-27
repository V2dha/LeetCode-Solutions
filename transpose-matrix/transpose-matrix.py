class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = []
        for i in range(len(matrix[0])):
            c = []
            for j in range(len(matrix)):
                c.append(matrix[j][i])
            r.append(c)
                
                
        return r
                
                
        