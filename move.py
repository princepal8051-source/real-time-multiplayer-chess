def move_piece(board, from_row, from_col, to_row, to_col):

    board[to_row][to_col] = board[from_row][from_col]
    board[from_row][from_col] = ""