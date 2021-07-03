class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for c in s:
            if c.isalnum():
                if c.isupper():
                    c = c.lower()
                a += c
        if a[::-1] == a:
            return True
        else:
            return False
                
      