class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 1 or n == 0: 
            return 0
        count = 0
        fact = 1
        for i in range(1, n+1):
            fact *= i
        fact = str(fact)
        for i in range(len(fact)):
            if fact[len(fact)-1-i] != '0':
                break
            count += 1
        return count
        