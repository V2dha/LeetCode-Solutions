class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if(len(s)%2 != 0):
            return False
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                stack.append(ch)
            elif stack and ch==')' and stack[-1]=='(':
                stack.pop()
            elif stack and ch=='}' and stack[-1]=='{':
                 stack.pop()
            elif stack and ch==']' and stack[-1]=='[':
                 stack.pop()
            else:
                return False
            
        return True if not stack else False
             
            
        
