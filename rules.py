def valid_pawn_move(piece, from_row, from_col, to_row, to_col):

    # White Pawn
    if piece == "wp":

        if from_col == to_col and to_row == from_row - 1:
            return True

        if from_row == 6 and from_col == to_col and to_row == 4:
            return True

    # Black Pawn
    elif piece == "bp":

        if from_col == to_col and to_row == from_row + 1:
            return True

        if from_row == 1 and from_col == to_col and to_row == 3:
            return True

    return False


def valid_knight_move(from_row, from_col, to_row, to_col):

    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)

    if (row_diff == 2 and col_diff == 1) or \
       (row_diff == 1 and col_diff == 2):
        return True

    return False


def valid_rook_move(board, from_row, from_col, to_row, to_col):

    if from_row != to_row and from_col != to_col:
        return False

    if from_col == to_col:

        step = 1 if to_row > from_row else -1

        for row in range(from_row + step, to_row, step):

            if board[row][from_col] != "":
                return False

    elif from_row == to_row:

        step = 1 if to_col > from_col else -1

        for col in range(from_col + step, to_col, step):

            if board[from_row][col] != "":
                return False

    return True


def valid_bishop_move(board, from_row, from_col, to_row, to_col):

    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)

    if row_diff != col_diff:
        return False

    row_step = 1 if to_row > from_row else -1
    col_step = 1 if to_col > from_col else -1

    row = from_row + row_step
    col = from_col + col_step

    while row != to_row and col != to_col:

        if board[row][col] != "":
            return False

        row += row_step
        col += col_step

    return True


def valid_queen_move(board, from_row, from_col, to_row, to_col):

    if valid_rook_move(
        board,
        from_row,
        from_col,
        to_row,
        to_col
    ):
        return True

    if valid_bishop_move(
        board,
        from_row,
        from_col,
        to_row,
        to_col
    ):
        return True

    return False

def valid_king_move(from_row, from_col, to_row, to_col):

    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)

    # King can move only 1 square
    if row_diff <= 1 and col_diff <= 1:
        return True

    return False
def is_same_color(piece1, piece2):

    if piece1 == "" or piece2 == "":
        return False

    return piece1[0] == piece2[0]