class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        result = ""
        def ispalindrome(s):
            return True if s==s[::-1] else False

        if len(s) == 1:
            return s

        if s==s[::-1]:
            return s

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if ispalindrome(s[i:j+1]):
                    if len(s[i:j+1]) > max_len:
                        max_len = len(s[i:j+1])
                        result = s[i:j+1]

        return result if result != "" else s[0]

# abb 

# i = 0
# j = 1 
# a 
# max_len = 1
# result = a

# j = 2
# ab

# i = 1
# j = 2





        