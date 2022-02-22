class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Approach using Stack
        Time Complexity = O(N)
        """
        max_len, curr_len = 0, 0
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(curr_len)
                curr_len = 0
            else:
                if stack:
                    curr_len += stack.pop()+2
                    max_len = max(max_len, curr_len)
                else:
                    curr_len = 0
        return max_len
                    
        