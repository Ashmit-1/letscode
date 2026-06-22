class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            col = set()
            row = set()
            grid = set()

            for j in range(9):
                try:
                    ele = int(board[i][j])
                    if ele in row or ele > 9:
                        return False
                    else:
                        row.add(ele)
                except Exception as e:
                    pass

                try:
                    ele = int(board[j][i])
                    if ele in col or ele > 9:
                        return False
                    else:
                        col.add(ele)
                except Exception as e:
                    pass
                
                r = 3 * (i // 3) + (j//3)
                c = (i % 3) * 3 + (j%3)


                try:
                    ele = int(board[r][c])
                    if ele in grid or ele > 9:
                        return False
                    else:
                        grid.add(ele)
                except Exception as e:
                    pass

        return True


                
        