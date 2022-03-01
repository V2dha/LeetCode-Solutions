class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            count = 0
            for bit in bin(i):
                if bit == '1':
                    count+= 1
            l.append(count)
        return l
        