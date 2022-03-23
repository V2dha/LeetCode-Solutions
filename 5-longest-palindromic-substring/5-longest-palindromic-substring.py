class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Approach - Centre Expansion 
        Time Complexity - O(N*N)
        Space Complexity - O(1)
        """
        if s == None or len(s) < 1:
            return ""
        res_len = 0
        res_left = 0
        res_right = 0
        for i in range(len(s)):
            #for cases like "racecar"
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_len:
                    res_left = l
                    res_right = r+1
                    res_len = r-l+1
                l -= 1
                r += 1
            #for cases like "abba"
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_len:
                    res_left = l
                    res_right = r+1
                    res_len = r-l+1
                l -= 1
                r += 1
        return s[res_left:res_right]
    

            
        