import pygame

from settings import *
from board import board
from pieces import load_pieces
from move import move_piece

from rules import (
    valid_pawn_move,
    valid_knight_move,
    valid_rook_move,
    valid_bishop_move,
    valid_queen_move,
    valid_king_move,
    is_same_color
)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

pieces = load_pieces()

selected_piece = None
selected_row = -1
selected_col = -1

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            col = event.pos[0] // SQUARE_SIZE
            row = event.pos[1] // SQUARE_SIZE

            # First Click
            if selected_piece is None:

                if board[row][col] != "":

                    selected_piece = board[row][col]
                    selected_row = row
                    selected_col = col

                    print(f"Selected: {selected_piece}")

            # Second Click
            else:

                piece = board[selected_row][selected_col]

                target_piece = board[row][col]

                if is_same_color(piece, target_piece):

                   print("Cannot capture your own piece")

                   selected_piece = None
                   selected_row = -1
                   selected_col = -1

                   continue

                target_piece = board[row][col]

                if is_same_color(piece, target_piece):

                        print("Cannot capture your own piece")

                        selected_piece = None
                        selected_row = -1
                        selected_col = -1

                        continue

                # White Pawn
                if piece == "wp":

                    if valid_pawn_move(
                        piece,
                        selected_row,
                        selected_col,
                        row,
                        col
                    ):
                        move_piece(
                            board,
                            selected_row,
                            selected_col,
                            row,
                            col
                        )
                        print("Valid White Pawn Move")
                    else:
                        print("Invalid White Pawn Move")

                # Black Pawn
                elif piece == "bp":

                    if valid_pawn_move(
                        piece,
                        selected_row,
                        selected_col,
                        row,
                        col
                    ):
                        move_piece(
                            board,
                            selected_row,
                            selected_col,
                            row,
                            col
                        )
                        print("Valid Black Pawn Move")
                    else:
                        print("Invalid Black Pawn Move")

                # White Knight
                elif piece == "wn":

                    if valid_knight_move(
                        selected_row,
                        selected_col,
                        row,
                        col
                    ):
                        move_piece(
                            board,
                            selected_row,
                            selected_col,
                            row,
                            col
                        )
                        print("Valid White Knight Move")
                    else:
                        print("Invalid White Knight Move")

                # Black Knight
                elif piece == "bn":

                    if valid_knight_move(
                        selected_row,
                        selected_col,
                        row,
                        col
                    ):
                        move_piece(
                            board,
                            selected_row,
                            selected_col,
                            row,
                            col
                        )
                        print("Valid Black Knight Move")
                    else:
                        print("Invalid Black Knight Move")

                # White Rook
                elif piece == "wr":

                    if valid_rook_move(
                        board,
                        selected_row,
                        selected_col,
                        row,
                        col
                    ):
                        move_piece(
                            board,
                            selected_row,
                            selected_col,
                            row,
                            col
                        )
                        print("Valid White Rook Move")
                    else:
                        print("Invalid White Rook Move")

                # Black Rook
                elif piece == "br":

                    if valid_rook_move(
                        board,
                        selected_row,
                        selected_col,
                        row,
                        col
                    ):
                        move_piece(
                            board,
                            selected_row,
                            selected_col,
                            row,
                            col
                        )
                        print("Valid Black Rook Move")
                    else:
                        print("Invalid Black Rook Move")

                # White Bishop
                elif piece == "wb":

                    if valid_bishop_move(
                        board,
                        selected_row,
                        selected_col,
                        row,
                        col
                    ):
                        move_piece(
                            board,
                            selected_row,
                            selected_col,
                            row,
                            col
                        )
                        print("Valid White Bishop Move")
                    else:
                        print("Invalid White Bishop Move")

                # Black Bishop
                elif piece == "bb":

                    if valid_bishop_move(
                        board,
                        selected_row,
                        selected_col,
                        row,
                        col
                    ):
                        move_piece(
                            board,
                            selected_row,
                            selected_col,
                            row,
                            col
                        )
                        print("Valid Black Bishop Move")
                    else:
                        print("Invalid Black Bishop Move")

                # White Queen
                elif piece == "wq":

                    if valid_queen_move(
                        board,
                        selected_row,
                        selected_col,
                        row,
                        col
                    ):
                        move_piece(
                            board,
                            selected_row,
                            selected_col,
                            row,
                            col
                        )
                        print("Valid White Queen Move")
                    else:
                        print("Invalid White Queen Move")

                # Black Queen
                elif piece == "bq":

                    if valid_queen_move(
                        board,
                        selected_row,
                        selected_col,
                        row,
                        col
                    ):
                        move_piece(
                            board,
                            selected_row,
                            selected_col,
                            row,
                            col
                        )
                        print("Valid Black Queen Move")
                    else:
                        print("Invalid Black Queen Move")

                # =========================
                # White King
                # =========================
                elif piece == "wk":

                    if valid_king_move(
                        selected_row,
                        selected_col,
                        row,
                        col
                    ):

                        move_piece(
                            board,
                            selected_row,
                            selected_col,
                            row,
                            col
                        )

                        print("Valid White King Move")

                    else:
                        print("Invalid White King Move")

                # =========================
                # Black King
                # =========================
                elif piece == "bk":

                    if valid_king_move(
                        selected_row,
                        selected_col,
                        row,
                        col
                    ):

                        move_piece(
                            board,
                            selected_row,
                            selected_col,
                            row,
                            col
                        )

                        print("Valid Black King Move")

                    else:
                        print("Invalid Black King Move")

                # Other Pieces
                else:

                    move_piece(
                        board,
                        selected_row,
                        selected_col,
                        row,
                        col
                    )

                    print("Piece Moved")

                selected_piece = None
                selected_row = -1
                selected_col = -1

    # Draw Board
    for row in range(ROWS):
        for col in range(COLS):

            color = WHITE if (row + col) % 2 == 0 else BROWN

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

    # Draw Pieces
    for row in range(8):
        for col in range(8):

            piece = board[row][col]

            if piece != "":
                screen.blit(
                    pieces[piece],
                    (
                        col * SQUARE_SIZE,
                        row * SQUARE_SIZE
                    )
                )

    pygame.display.update()

pygame.quit()