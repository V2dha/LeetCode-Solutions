class Solution:
    def longestPalindrome(self, s: str) -> str:
        """"""
        if s == None or len(s) < 1:
            return ""
        res_len = 0
        res_left = 0
        res_right = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_len:
                    res_left = l
                    res_right = r+1
                    res_len = r-l+1
                l -= 1
                r += 1
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_len:
                    res_left = l
                    res_right = r+1
                    res_len = r-l+1
                l -= 1
                r += 1
        return s[res_left:res_right]
    

            
        