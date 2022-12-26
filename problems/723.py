# 这个题是个陷阱题 不是用扫描+dfs去做的 因为只能消除横三+/竖三+ 并不是需要消除那种奇形怪状的

def candyCrush(board):
    R = len(board)
    C = len(board[0])
    todo = True
    
    while todo:
        todo = False
        for i in range(R):
            for j in range(C-2):
                if abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]):
                    val = -abs(board[i][j])
                    board[i][j] = board[i][j+1] = board[i][j+2] = val
                    todo = True

        for j in range(C):
            for i in range(R-2):
                if abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+2][j]):
                    val = -abs(board[i][j])
                    board[i][j] = board[i+1][j] = board[i+2][j] = val
                    todo = True
        
        if todo:
            for j in range(C):
                last = R-1
                for i in range(R-1,-1,-1):
                    if board[i][j]>0:
                        board[last][j] = board[i][j]
                        last-=1
                for i in range(last,-1,-1):
                    board[i][j]=0
    return board

board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
candyCrush(board)