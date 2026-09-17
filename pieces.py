import pygame
import os

def load_pieces():
    pieces = {}

    base = os.path.join(os.path.dirname(__file__), "assets")

    pieces["wk"] = pygame.image.load(os.path.join(base, "white king.jpeg"))
    pieces["wq"] = pygame.image.load(os.path.join(base, "white queen.jpeg"))
    pieces["wr"] = pygame.image.load(os.path.join(base, "white rook.jpeg"))
    pieces["wb"] = pygame.image.load(os.path.join(base, "white bishop.jpeg"))
    pieces["wn"] = pygame.image.load(os.path.join(base, "white knight.jpeg"))
    pieces["wp"] = pygame.image.load(os.path.join(base, "white pawn.jpeg"))

    pieces["bk"] = pygame.image.load(os.path.join(base, "black king.jpeg"))
    pieces["bq"] = pygame.image.load(os.path.join(base, "black queen.jpeg"))
    pieces["br"] = pygame.image.load(os.path.join(base, "black rook.jpeg"))
    pieces["bb"] = pygame.image.load(os.path.join(base, "black bishop.jpeg"))
    pieces["bn"] = pygame.image.load(os.path.join(base, "black knight.jpeg"))
    pieces["bp"] = pygame.image.load(os.path.join(base, "black pawn.jpeg"))

    for piece in pieces:
        pieces[piece] = pygame.transform.scale(pieces[piece], (80, 80))

    return pieces