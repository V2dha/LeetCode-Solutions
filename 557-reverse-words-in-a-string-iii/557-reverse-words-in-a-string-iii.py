class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        rev = ""
        for i in range(len(s)):
            if s[i] == " ":
                rev += word[::-1] + " "
                word = ""
            else:
                word += s[i]
        rev += word[::-1]
        return rev