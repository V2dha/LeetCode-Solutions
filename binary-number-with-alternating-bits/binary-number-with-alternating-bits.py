from collections import deque
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = bin(n)
        for i in range(0,len(num)-1):
            if num[i] == num[i+1]:
                return False
        return True
                
        
    # def binary(self, n):
    #     q = deque()
    #     q.appendleft('1')
    #     l = []
    #     while n:
    #         l.append(q[-1])
    #         q.appendleft(q[-1]+'0')
    #         q.appendleft(q[-1]+'1')
    #         q.pop()
    #         n -= 1
    #     return l[len(l)-1]