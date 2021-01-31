class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # base case
        if '*' not in p and '.' not in p:
            return s==p
        
        # setup dp table
        m = len(s)+1
        n = len(p)+1
        
        # dp[i][j] represents if s[:i] matches the pattern p[:j]
        dp = [[False for _ in range(n)] for _ in range(m)]
        
        # empty string matches empty string
        dp[0][0] = True
        
        # This deals with patterns like a* or a*b* or a*b*c*
        for i in range(1,len(dp[0])):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        
        
        for i in range(1,m):
            for j in range(1,n):
                # if current pattern is a dot
                # or if current pattern has same character
                # as current text then the answer is the one
                # diagonally above(removing both chars)
                if p[j-1] == '.' or (s[i-1] == p[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                    
                # if its a star then it gets intresting.
                # first its automatically equal to [i][j-2]
                # since thats accounting for the STAR being of 0 length
                # aka a* being ''(empty). Then if that doesnt work
                # if the pattern is a dot(accounting for .*) or 
                # previous pattern before * is simmilar as text
                # then its the answer above since your accounting for
                # removing last char of text
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = (dp[i][j] or dp[i-1][j])
                    # else false by default
                    
        # answer in last column/row
        return dp[-1][-1]