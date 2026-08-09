move_history = []
captured_pieces = []


def add_move(
    piece,
    from_row,
    from_col,
    to_row,
    to_col,
    captured_piece=""
):

    move = {
        "piece": piece,
        "from": (from_row, from_col),
        "to": (to_row, to_col),
        "captured": captured_piece
    }

    move_history.append(move)

    if captured_piece != "":
        captured_pieces.append(captured_piece)


def get_move_history():
    return move_history


def get_captured_pieces():
    return captured_pieces