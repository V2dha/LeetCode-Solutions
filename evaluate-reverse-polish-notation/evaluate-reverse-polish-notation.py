class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return tokens[0]
        if not tokens:
            return 
        stack = []
        for c in tokens:
            if c.isdigit() or c.startswith('-') and c[1:].isdigit():
                stack.append(int(c))
            else:
                a = stack.pop()
                b = stack.pop()
                if  c == '+':
                    stack.append(a+b)
                if c == '-':
                    stack.append(b-a)
                if c == '*':
                    stack.append(b*a)
                if c == '/':
                    stack.append(int(b/a))
        return stack.pop()
                
        