def isLegal(x, y, L):
    '''
    isLegal(int, int, list) --> bool
    For our knightsTour, this function tells us if a move is legal. 
    A move is legal if the x and y coordinates 
    are within bounds, and if the board at position
    has a value of 0 (represents a "nul" value).
    '''
    return x >= 0 and y >= 0 and x < len(L) and y < len(L[0]) and L[x][y] == 0

def knightsTourHelper(board, row, col, knightNum):
    '''
    Helper function to determine where a next move will be 
    and if it can happen.
    '''
    moves = [[2, 1], [-2, 1], [2, -1], [-2, -1],
             [1, 2], [-1, 2], [1, -2], [-1, -2]]
    #place first num on the board, reference to check next positions
    board[row][col] = knightNum

    if knightNum == (len(board) * len(board[0])):
        return board

    for drow, dcol in moves:
        newRow = row + drow
        newCol = col + dcol
        if isLegal(newRow, newCol, board):
            board[newRow][newCol] = knightNum
            if knightsTourHelper(board, newRow, newCol, knightNum + 1)!= None:
                return board
            board[newRow][newCol] = 0

    return None

def knightsTour(rows, cols):
    '''
    knightsTour(int, int) --> list
    Returns a "board" of moves representing a knights tour when given 
    rows and cols of a board.
    '''
    for i in range(rows):
        for j in range(cols):
            board = [([0] * cols) for row in range(rows)]
            board[i][j] = 1
            #combination of all the moves possible
            board = knightsTourHelper(board, i, j, 1)
            if board != None:
                return board

    return None
