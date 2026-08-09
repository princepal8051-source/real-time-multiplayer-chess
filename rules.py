def valid_pawn_move(
    piece,
    from_row,
    from_col,
    to_row,
    to_col,
    target_piece=""
):
    if piece == "wp":

        if from_col == to_col and to_row == from_row - 1:
            return target_piece == ""

        if from_row == 6 and from_col == to_col and to_row == from_row - 2:
            return target_piece == ""

        if to_row == from_row - 1 and abs(to_col - from_col) == 1:
            return target_piece != "" and target_piece[0] == "b"

    elif piece == "bp":

        if from_col == to_col and to_row == from_row + 1:
            return target_piece == ""

        if from_row == 1 and from_col == to_col and to_row == from_row + 2:
            return target_piece == ""

        if to_row == from_row + 1 and abs(to_col - from_col) == 1:
            return target_piece != "" and target_piece[0] == "w"

    return False


def valid_knight_move(from_row, from_col, to_row, to_col):

    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)

    return (
        (row_diff == 2 and col_diff == 1)
        or
        (row_diff == 1 and col_diff == 2)
    )


def valid_rook_move(board, from_row, from_col, to_row, to_col):

    if from_row != to_row and from_col != to_col:
        return False

    if from_col == to_col:

        step = 1 if to_row > from_row else -1

        for row in range(from_row + step, to_row, step):

            if board[row][from_col] != "":
                return False

    else:

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

    return (
        valid_rook_move(
            board,
            from_row,
            from_col,
            to_row,
            to_col
        )
        or
        valid_bishop_move(
            board,
            from_row,
            from_col,
            to_row,
            to_col
        )
    )


def valid_king_move(from_row, from_col, to_row, to_col):

    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)

    if row_diff == 0 and col_diff == 0:
        return False

    return row_diff <= 1 and col_diff <= 1


def is_same_color(piece1, piece2):

    if piece1 == "" or piece2 == "":
        return False

    return piece1[0] == piece2[0]


# =========================================================
# FIND KING
# =========================================================

def find_king(board, color):

    king = "wk" if color == "white" else "bk"

    for row in range(8):
        for col in range(8):

            if board[row][col] == king:
                return row, col

    return None


# =========================================================
# CAN ATTACK
# =========================================================

def can_attack(board, from_row, from_col, to_row, to_col):

    piece = board[from_row][from_col]

    if piece == "":
        return False

    piece_type = piece[1]

    if piece_type == "p":

        if piece == "wp":
            return (
                to_row == from_row - 1
                and abs(to_col - from_col) == 1
            )

        if piece == "bp":
            return (
                to_row == from_row + 1
                and abs(to_col - from_col) == 1
            )

    elif piece_type == "n":

        return valid_knight_move(
            from_row,
            from_col,
            to_row,
            to_col
        )

    elif piece_type == "r":

        return valid_rook_move(
            board,
            from_row,
            from_col,
            to_row,
            to_col
        )

    elif piece_type == "b":

        return valid_bishop_move(
            board,
            from_row,
            from_col,
            to_row,
            to_col
        )

    elif piece_type == "q":

        return valid_queen_move(
            board,
            from_row,
            from_col,
            to_row,
            to_col
        )

    elif piece_type == "k":

        return valid_king_move(
            from_row,
            from_col,
            to_row,
            to_col
        )

    return False


# =========================================================
# CHECK
# =========================================================

def is_in_check(board, color):

    king_position = find_king(board, color)

    if king_position is None:
        return True

    king_row, king_col = king_position

    opponent = "black" if color == "white" else "white"

    for row in range(8):
        for col in range(8):

            piece = board[row][col]

            if piece == "":
                continue

            if piece[0] != opponent[0]:
                continue

            if can_attack(
                board,
                row,
                col,
                king_row,
                king_col
            ):
                return True

    return False


# =========================================================
# BASIC MOVE
# =========================================================

def is_valid_piece_move(
    board,
    from_row,
    from_col,
    to_row,
    to_col
):

    piece = board[from_row][from_col]
    target_piece = board[to_row][to_col]

    if piece == "":
        return False

    if is_same_color(piece, target_piece):
        return False

    piece_type = piece[1]

    if piece_type == "p":

        return valid_pawn_move(
            piece,
            from_row,
            from_col,
            to_row,
            to_col,
            target_piece
        )

    elif piece_type == "n":

        return valid_knight_move(
            from_row,
            from_col,
            to_row,
            to_col
        )

    elif piece_type == "r":

        return valid_rook_move(
            board,
            from_row,
            from_col,
            to_row,
            to_col
        )

    elif piece_type == "b":

        return valid_bishop_move(
            board,
            from_row,
            from_col,
            to_row,
            to_col
        )

    elif piece_type == "q":

        return valid_queen_move(
            board,
            from_row,
            from_col,
            to_row,
            to_col
        )

    elif piece_type == "k":

        return valid_king_move(
            from_row,
            from_col,
            to_row,
            to_col
        )

    return False


# =========================================================
# LEGAL MOVE
# =========================================================

def has_legal_move(board, color):

    for from_row in range(8):

        for from_col in range(8):

            piece = board[from_row][from_col]

            if piece == "":
                continue

            if color == "white" and piece[0] != "w":
                continue

            if color == "black" and piece[0] != "b":
                continue

            for to_row in range(8):

                for to_col in range(8):

                    if not is_valid_piece_move(
                        board,
                        from_row,
                        from_col,
                        to_row,
                        to_col
                    ):
                        continue

                    captured_piece = board[to_row][to_col]

                    board[to_row][to_col] = piece
                    board[from_row][from_col] = ""

                    still_in_check = is_in_check(
                        board,
                        color
                    )

                    board[from_row][from_col] = piece
                    board[to_row][to_col] = captured_piece

                    if not still_in_check:
                        return True

    return False


def is_checkmate(board, color):

    if not is_in_check(board, color):
        return False

    return not has_legal_move(board, color)


def is_stalemate(board, color):

    if is_in_check(board, color):
        return False

    return not has_legal_move(board, color)