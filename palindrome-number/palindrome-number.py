class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        if x < 0:
            return False
        else:
            while(x):
                rev = rev*10 + (x%10)
                x = x//10
            if(rev==temp):
                return True
            else:
                return False
                
        
