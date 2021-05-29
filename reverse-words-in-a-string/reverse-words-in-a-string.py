class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.split(' '))
        res = ''
        print(l)
        for i in range(len(l)):
            if l[len(l)-1-i] != '':
                res += l[len(l)-1-i]
                res += ' '
        return res[:len(res)-1]
            