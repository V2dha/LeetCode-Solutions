class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.']*n for _ in range(n)]
        def isValid(row, col, board):
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 'Q':
                        if row == i or col == j or row+col == i+j or row-col == i-j:
                            return False
            return True
        def solve(board, row, ans):
            if row == n:
                res = [''.join(s) for s in board]
                ans.append(res)
                return 
            for col in range(n):
                if isValid(row, col, board):
                    board[row][col] = 'Q'
                    solve(board, row+1, ans)
                    board[row][col] = '.'
        ans = list()
        solve(board, 0, ans)
        return len(ans)
            
        