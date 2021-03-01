def binomial(n, c):
    if c == 0 or c == n:
        return 1
    if c > n-c:
        c = n-c
    a = 1
    for i in range(c):
        a = a * (n-i)
        a = a // (i+1)
    return a

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = []
        for i in range(rowIndex+1):
            l.append(binomial(rowIndex, i))
        return l
        