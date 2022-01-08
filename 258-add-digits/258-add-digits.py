class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = 0
            for n in str(num):
                s += int(n)
            num = s
        return num
            