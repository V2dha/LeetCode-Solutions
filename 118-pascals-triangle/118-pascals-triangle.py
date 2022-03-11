class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTri = [[] for _ in range(numRows)]
        
        for i in range(numRows):
            pascalTri[i] = [0]*(i+1)
            pascalTri[i][0] = pascalTri[i][i] = 1
            for j in range(1, i):
                pascalTri[i][j] = pascalTri[i-1][j-1] + pascalTri[i-1][j]
                
        return pascalTri