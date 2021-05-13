def convert(n):
    n1 = 0
    num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    for i in range(len(n)):
        n1 += num[n[i]]*(10**(len(n)-i-1))
    return n1
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = convert(num1)
        n2 = convert(num2)
        return str(n1+n2)
        