class Solution(object):
    def isValidSudoku(self, board):
        rowset=[set() for _ in range(9)]
        colset=[set() for _ in range(9)]
        gridset=[set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if(board[i][j]=='.'):
                    continue
                gridno=(i//3)*3+(j//3)
                ispresentinrow=board[i][j] in rowset[i]
                ispresentincol=board[i][j] in colset[j]
                ispresentgrid=board[i][j] in gridset[gridno]

                if(ispresentinrow or ispresentincol or ispresentgrid):
                    return False
                rowset[i].add(board[i][j])
                colset[j].add(board[i][j])
                gridset[gridno].add(board[i][j])
        return True

