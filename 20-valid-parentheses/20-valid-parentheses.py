class Solution:
    def isValid(self, s: str) -> bool:
        """
        Approach - Using a stack 
        1. Running a loop and going through each character in the string
        2. Append if it is one of the opening bracket ['(', '[', '{']
        3. Incase of a closing bracket [')', ']', '}']
            a. If the string is not empty then check the top of the stack 
            b. If the top == opening bracket and character == closing bracket
                then pop 
        4. If after the loop the stack is empty return true else return false
        """
        stack = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            else:
                if stack:
                    if stack[-1] == "(" and ch == ")":
                        stack.pop()
                    elif stack[-1] == "[" and ch == "]":
                        stack.pop()
                    elif stack[-1] == "{" and ch == "}":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return True if not stack else False
        
    
#         stack = []
#         openBrac = ['(', '[', '{']
        

#         for ch in s:
#             if ch in openBrac:
#                 stack.append(ch)
#             else:
#                 if stack:
#                     if stack[-1] == '(' and ch == ')':
#                         stack.pop()
#                     elif stack[-1] == '{' and ch == '}':
#                         stack.pop()
#                     elif stack[-1] == '[' and ch == ']':
#                         stack.pop()
#                     else:
#                         return False
#                 else:
#                     return False
#         return True if not stack else False
        
    
        
        