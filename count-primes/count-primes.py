from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        count = 0
        prime = []
        for i in range(n):
            prime.append(True)
        p = 2
        while p*p < n:
            if prime[p] ==  True:
                for i in range (p*2, n, p):
                    prime[i] = False
            p += 1
        prime[0] = False
        prime[1] = False
        for i in range(n):
            if prime[i]:
                count += 1
        return count
                    
        