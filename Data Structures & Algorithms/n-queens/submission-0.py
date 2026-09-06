class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def can(c, r, row, udiag, ddiag):
            if r not in row and c - r not in udiag and c + r not in ddiag:
                return True
            return False
        def queen(col, prevRow, upDiag, downDiag, board, ans):
            if col == n:
                ans.append(["".join(i) for i in board.copy()])
                return
            for i in range(n):
                if can(col, i, prevRow, upDiag, downDiag):
                    board[i][col] = 'Q'
                    prevRow.add(i)
                    upDiag.add(col - i)
                    downDiag.add(col + i)

                    queen(col+1, prevRow, upDiag, downDiag, board, ans)

                    prevRow.remove(i)
                    upDiag.remove(col - i)
                    downDiag.remove(col + i)
                    board[i][col] = '.'
        board = [['.' for _ in range(n)] for i in range(n)]
        ans = []
        queen(0, set(), set(), set(), board, ans)
        return ans

            

        