import pygame
import threading
from settings import *
from board import board
from pieces import load_pieces
from database import save_move
from network import Network

from rules import (
    is_same_color,
    is_valid_piece_move,
    is_in_check,
    is_checkmate,
    is_stalemate
)

from history import (
    add_move,
    get_move_history,
    get_captured_pieces
)

from database import (
    create_tables,
    add_player,
    create_game,
    save_move,
    update_game_status
)
pygame.init()

network = Network()



def receive_moves():
     while True:
           try:
               data = network.receive()
               if data:
                   from_row, from_col, to_row, to_col = map(
                         int,
                         data.split(",")
                     )
                   board[to_row][to_col] = board[from_row][from_col]
                   board[from_row][from_col] = ""
                   print(
                        "Received Move:",
                        data
                        )

           except:
                pass

threading.Thread(
    target=receive_moves,
    daemon=True
).start()

# =========================================================
# DATABASE SETUP
# =========================================================

create_tables()

white_player = "Player 1"
black_player = "Player 2"

add_player(
    white_player,
    "white"
)

add_player(
    black_player,
    "black"
)

game_id = create_game(
    white_player,
    black_player
)

print("Game ID:", game_id)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

pieces = load_pieces()

selected_piece = None
selected_row = -1
selected_col = -1

current_turn = "white"

game_over = False
winner = None


# =========================================================
# CASTLING STATUS
# =========================================================

white_king_moved = False
black_king_moved = False

white_left_rook_moved = False
white_right_rook_moved = False

black_left_rook_moved = False
black_right_rook_moved = False


# =========================================================
# PROMOTION STATUS
# =========================================================

promotion_active = False
promotion_row = -1
promotion_col = -1
promotion_color = None


# =========================================================
# PROMOTION MENU
# =========================================================

def draw_promotion_menu():

    overlay = pygame.Surface((WIDTH, HEIGHT))

    overlay.set_alpha(180)

    overlay.fill((0, 0, 0))

    screen.blit(
        overlay,
        (0, 0)
    )

    font = pygame.font.Font(
        None,
        40
    )

    text = font.render(
        "Choose Promotion",
        True,
        (255, 255, 255)
    )

    text_rect = text.get_rect(
        center=(
            WIDTH // 2,
            100
        )
    )

    screen.blit(
        text,
        text_rect
    )

    options = [
        "q",
        "r",
        "b",
        "n"
    ]

    start_x = 160
    y = 250

    for i, option in enumerate(options):

        piece_code = (
            promotion_color
            + option
        )

        x = start_x + i * 90

        pygame.draw.rect(
            screen,
            (240, 217, 181),
            (
                x,
                y,
                80,
                80
            )
        )

        screen.blit(
            pieces[piece_code],
            (
                x,
                y
            )
        )


# =========================================================
# MAIN LOOP
# =========================================================

running = True


while running:

    # =====================================================
    # EVENTS
    # =====================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:

            # =================================================
            # PROMOTION
            # =================================================

            if promotion_active:

                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if 250 <= mouse_y <= 330:

                    selected_option = None

                    if 160 <= mouse_x < 240:

                        selected_option = "q"

                    elif 250 <= mouse_x < 330:

                        selected_option = "r"

                    elif 340 <= mouse_x < 420:

                        selected_option = "b"

                    elif 430 <= mouse_x < 510:

                        selected_option = "n"


                    if selected_option:

                        board[
                            promotion_row
                        ][
                            promotion_col
                        ] = (
                            promotion_color
                            + selected_option
                        )

                        print(
                            "Pawn promoted to:",
                            selected_option.upper()
                        )

                        promotion_active = False

                        promotion_row = -1
                        promotion_col = -1
                        promotion_color = None


                        # -------------------------------------
                        # CHANGE TURN
                        # -------------------------------------

                        if current_turn == "white":

                            current_turn = "black"

                        else:

                            current_turn = "white"


                        print(
                            "Turn:",
                            current_turn
                        )


                        # -------------------------------------
                        # CHECKMATE
                        # -------------------------------------

                        if is_checkmate(
                            board,
                            current_turn
                        ):

                            winner = (
                                "White"
                                if current_turn == "black"
                                else "Black"
                            )

                            game_over = True

                            print(
                                "CHECKMATE!"
                            )

                            print(
                                winner,
                                "wins!"
                            )


                        # -------------------------------------
                        # STALEMATE
                        # -------------------------------------

                        elif is_stalemate(
                            board,
                            current_turn
                        ):

                            game_over = True

                            print(
                                "STALEMATE!"
                            )


                        # -------------------------------------
                        # CHECK
                        # -------------------------------------

                        elif is_in_check(
                            board,
                            current_turn
                        ):

                            print(
                                current_turn.capitalize(),
                                "is in CHECK!"
                            )

                continue


            # =================================================
            # GAME OVER
            # =================================================

            if game_over:

                continue


            # =================================================
            # BOARD POSITION
            # =================================================

            col = (
                event.pos[0]
                // SQUARE_SIZE
            )

            row = (
                event.pos[1]
                // SQUARE_SIZE
            )


            # =================================================
            # FIRST CLICK
            # =================================================

            if selected_piece is None:

                piece = board[row][col]


                # Empty square

                if piece == "":

                    continue


                # White turn

                if (
                    current_turn == "white"
                    and piece[0] != "w"
                ):

                    print(
                        "It's White's turn"
                    )

                    continue


                # Black turn

                if (
                    current_turn == "black"
                    and piece[0] != "b"
                ):

                    print(
                        "It's Black's turn"
                    )

                    continue


                selected_piece = piece

                selected_row = row

                selected_col = col


                print(
                    "Selected:",
                    selected_piece
                )


            # =================================================
            # SECOND CLICK
            # =================================================

            else:

                piece = board[
                    selected_row
                ][
                    selected_col
                ]

                target_piece = board[
                    row
                ][
                    col
                ]


                # ---------------------------------------------
                # OWN PIECE
                # ---------------------------------------------

                if is_same_color(
                    piece,
                    target_piece
                ):

                    print(
                        "Cannot capture your own piece"
                    )

                    selected_piece = None

                    selected_row = -1

                    selected_col = -1

                    continue


                castling = False


                # =================================================
                # WHITE CASTLING
                # =================================================

                if (
                    piece == "wk"
                    and not white_king_moved
                ):


                    # ---------------------------------------------
                    # KING SIDE
                    # ---------------------------------------------

                    if (

                        selected_row == 7

                        and selected_col == 4

                        and row == 7

                        and col == 6

                        and not white_right_rook_moved

                        and board[7][5] == ""

                        and board[7][6] == ""

                        and board[7][7] == "wr"

                        and not is_in_check(
                            board,
                            "white"
                        )

                    ):


                        board[7][4] = ""

                        board[7][5] = "wk"


                        through_check = is_in_check(
                            board,
                            "white"
                        )


                        board[7][5] = ""

                        board[7][4] = "wk"


                        if not through_check:

                            board[7][4] = ""

                            board[7][6] = "wk"

                            board[7][7] = ""

                            board[7][5] = "wr"


                            white_king_moved = True

                            white_right_rook_moved = True


                            castling = True


                            print(
                                "White King-side Castling"
                            )


                    # ---------------------------------------------
                    # QUEEN SIDE
                    # ---------------------------------------------

                    elif (

                        selected_row == 7

                        and selected_col == 4

                        and row == 7

                        and col == 2

                        and not white_left_rook_moved

                        and board[7][1] == ""

                        and board[7][2] == ""

                        and board[7][3] == ""

                        and board[7][0] == "wr"

                        and not is_in_check(
                            board,
                            "white"
                        )

                    ):


                        board[7][4] = ""

                        board[7][3] = "wk"


                        through_check = is_in_check(
                            board,
                            "white"
                        )


                        board[7][3] = ""

                        board[7][4] = "wk"


                        if not through_check:

                            board[7][4] = ""

                            board[7][2] = "wk"

                            board[7][0] = ""

                            board[7][3] = "wr"


                            white_king_moved = True

                            white_left_rook_moved = True


                            castling = True


                            print(
                                "White Queen-side Castling"
                            )


                # =================================================
                # BLACK CASTLING
                # =================================================

                elif (
                    piece == "bk"
                    and not black_king_moved
                ):


                    # ---------------------------------------------
                    # KING SIDE
                    # ---------------------------------------------

                    if (

                        selected_row == 0

                        and selected_col == 4

                        and row == 0

                        and col == 6

                        and not black_right_rook_moved

                        and board[0][5] == ""

                        and board[0][6] == ""

                        and board[0][7] == "br"

                        and not is_in_check(
                            board,
                            "black"
                        )

                    ):


                        board[0][4] = ""

                        board[0][5] = "bk"


                        through_check = is_in_check(
                            board,
                            "black"
                        )


                        board[0][5] = ""

                        board[0][4] = "bk"


                        if not through_check:

                            board[0][4] = ""

                            board[0][6] = "bk"

                            board[0][7] = ""

                            board[0][5] = "br"


                            black_king_moved = True

                            black_right_rook_moved = True


                            castling = True


                            print(
                                "Black King-side Castling"
                            )


                    # ---------------------------------------------
                    # QUEEN SIDE
                    # ---------------------------------------------

                    elif (

                        selected_row == 0

                        and selected_col == 4

                        and row == 0

                        and col == 2

                        and not black_left_rook_moved

                        and board[0][1] == ""

                        and board[0][2] == ""

                        and board[0][3] == ""

                        and board[0][0] == "br"

                        and not is_in_check(
                            board,
                            "black"
                        )

                    ):


                        board[0][4] = ""

                        board[0][3] = "bk"


                        through_check = is_in_check(
                            board,
                            "black"
                        )


                        board[0][3] = ""

                        board[0][4] = "bk"


                        if not through_check:

                            board[0][4] = ""

                            board[0][2] = "bk"

                            board[0][0] = ""

                            board[0][3] = "br"


                            black_king_moved = True

                            black_left_rook_moved = True


                            castling = True


                            print(
                                "Black Queen-side Castling"
                            )


                # =================================================
                # NORMAL MOVE
                # =================================================

                if not castling:

                    if is_valid_piece_move(

                        board,

                        selected_row,

                        selected_col,

                        row,

                        col

                    ):

                        captured_piece = board[row][col]

                        # -----------------------------------------
                        # MAKE TEMPORARY MOVE
                        # -----------------------------------------

                        board[row][col] = piece

                        board[selected_row][selected_col] = ""


                        # -----------------------------------------
                        # CHECK OWN KING
                        # -----------------------------------------

                        illegal_move = is_in_check(
                             board,
                            current_turn
                         )


                        if illegal_move: 

                        # -------------------------------------
                        # UNDO MOVE
                        # -------------------------------------

                         board[selected_row][selected_col] = piece

                         board[row][col] = captured_piece

                         print("Illegal move:")
                         print("Your King is in check")


                        else:

                            #-------------------------------------
                            # SAVE MOVE TO DATABASE
                            # -------------------------------------

                            save_move(
                                game_id,
                                current_turn,
                                piece,
                                selected_row,
                                selected_col,
                                row,
                                col,
                                captured_piece
                             )

                            # -------------------------------------
                            # SAVE MOVE HISTORY
                            # -------------------------------------

                            add_move(
                               piece,
                               selected_row,
                               selected_col,
                               row,
                               col,
                               captured_piece
                               )
                            
                            move_data = f"{selected_row},{selected_col},{row},{col}"

                            network.send(move_data)

                            print("Move saved successfully")
                        
                        


                        if illegal_move:


                            # Undo move

                            board[
                                selected_row
                            ][
                                selected_col
                            ] = piece


                            board[row][col] = captured_piece


                            print(
                                "Illegal move:"
                            )

                            print(
                                "Your King is in check"
                            )


                        else:


                            # =====================================
                            # KING STATUS
                            # =====================================

                            if piece == "wk":

                                white_king_moved = True


                            if piece == "bk":

                                black_king_moved = True


                            # =====================================
                            # ROOK STATUS
                            # =====================================

                            if piece == "wr":

                                if (
                                    selected_row == 7
                                    and selected_col == 0
                                ):

                                    white_left_rook_moved = True


                                if (
                                    selected_row == 7
                                    and selected_col == 7
                                ):

                                    white_right_rook_moved = True


                            if piece == "br":

                                if (
                                    selected_row == 0
                                    and selected_col == 0
                                ):

                                    black_left_rook_moved = True


                                if (
                                    selected_row == 0
                                    and selected_col == 7
                                ):

                                    black_right_rook_moved = True


                            # =====================================
                            # PAWN PROMOTION
                            # =====================================

                            if (
                                piece == "wp"
                                and row == 0
                            ):

                                promotion_active = True

                                promotion_row = row

                                promotion_col = col

                                promotion_color = "w"


                                print(
                                    "Choose White Pawn Promotion"
                                )


                            elif (
                                piece == "bp"
                                and row == 7
                            ):

                                promotion_active = True

                                promotion_row = row

                                promotion_col = col

                                promotion_color = "b"


                                print(
                                    "Choose Black Pawn Promotion"
                                )


                            else:


                                # =================================
                                # CHANGE TURN
                                # =================================

                                if current_turn == "white":

                                    current_turn = "black"

                                else:

                                    current_turn = "white"


                                print(
                                    "Turn:",
                                    current_turn
                                )


                                # =================================
                                # CHECKMATE
                                # =================================

                                if is_checkmate(

                                    board,

                                    current_turn

                                ):


                                    winner = (

                                        "White"

                                        if current_turn == "black"

                                        else "Black"

                                    )


                                    game_over = True


                                    print(
                                        "CHECKMATE!"
                                    )

                                    print(
                                        winner,
                                        "wins!"
                                    )


                                # =================================
                                # STALEMATE
                                # =================================

                                elif is_stalemate(

                                    board,

                                    current_turn

                                ):


                                    game_over = True


                                    print(
                                        "STALEMATE!"
                                    )


                                # =================================
                                # CHECK
                                # =================================

                                elif is_in_check(

                                    board,

                                    current_turn

                                ):


                                    print(

                                        current_turn.capitalize(),

                                        "is in CHECK!"

                                    )


                    else:

                        print(
                            "Invalid Move"
                        )


                # =================================================
                # RESET SELECTION
                # =================================================

                selected_piece = None

                selected_row = -1

                selected_col = -1


    # =========================================================
    # DRAW BOARD
    # =========================================================

    for row in range(ROWS):

        for col in range(COLS):

            color = (

                WHITE

                if (row + col) % 2 == 0

                else BROWN

            )


            pygame.draw.rect(

                screen,

                color,

                (

                    col * SQUARE_SIZE,

                    row * SQUARE_SIZE,

                    SQUARE_SIZE,

                    SQUARE_SIZE

                )

            )


    # =========================================================
    # SELECTED PIECE
    # =========================================================

    if selected_piece is not None:

        pygame.draw.rect(

            screen,

            (255, 255, 0),

            (

                selected_col * SQUARE_SIZE,

                selected_row * SQUARE_SIZE,

                SQUARE_SIZE,

                SQUARE_SIZE

            ),

            4

        )


    # =========================================================
    # DRAW PIECES
    # =========================================================

    for row in range(ROWS):

        for col in range(COLS):

            piece = board[row][col]


            if piece != "":

                screen.blit(

                    pieces[piece],

                    (

                        col * SQUARE_SIZE,

                        row * SQUARE_SIZE

                    )

                )


    # =========================================================
    # PROMOTION MENU
    # =========================================================

    if promotion_active:

        draw_promotion_menu()


    # =========================================================
    # GAME OVER
    # =========================================================

    if game_over:

        font = pygame.font.Font(

            None,

            60

        )


        if winner:

            text = font.render(

                f"{winner} Wins!",

                True,

                (255, 0, 0)

            )

        else:

            text = font.render(

                "Stalemate!",

                True,

                (255, 0, 0)

            )


        text_rect = text.get_rect(

            center=(

                WIDTH // 2,

                HEIGHT // 2

            )

        )


        screen.blit(

            text,

            text_rect

        )


    # =========================================================
    # UPDATE DISPLAY
    # =========================================================

    pygame.display.update()


# =============================================================
# PRINT HISTORY WHEN GAME CLOSES
# =============================================================

print()
print("================================")
print("        MOVE HISTORY")
print("================================")

for number, move in enumerate(
    get_move_history(),
    start=1
):

    print(

        number,

        move["piece"],

        move["from"],

        "->",

        move["to"]

    )


print()
print("================================")
print("       CAPTURED PIECES")
print("================================")

print(
    get_captured_pieces()
)


pygame.quit()