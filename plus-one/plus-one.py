class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1]  = digits[-1] + 1
            return digits
        else:
            s = ''
            for n in digits:
                s += str(n)
            s = int(s) + 1
            s = str(s)
            digits = []
            for n in s:
                digits.append(int(n))
            return digits
        