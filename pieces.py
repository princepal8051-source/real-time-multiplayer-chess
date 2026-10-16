import pygame
from pathlib import Path

def load_pieces():

    pieces = {}

    image_directory = Path(__file__).resolve().parent / "image.py"

    pieces["wk"] = pygame.image.load(str(image_directory / "IMG-20260924-WA0009.png"))
    pieces["wq"] = pygame.image.load(str(image_directory / "IMG-20260924-WA0011.png"))
    pieces["wr"] = pygame.image.load(str(image_directory / "IMG-20260924-WA0014.png"))
    pieces["wb"] = pygame.image.load(str(image_directory / "IMG-20260924-WA0018.png"))
    pieces["wn"] = pygame.image.load(str(image_directory / "IMG-20260924-WA0010.png"))
    pieces["wp"] = pygame.image.load(str(image_directory / "IMG-20260924-WA0015.png"))

    pieces["bk"] = pygame.image.load(str(image_directory / "IMG-20260924-WA0008.png"))
    pieces["bq"] = pygame.image.load(str(image_directory / "IMG-20260924-WA0013.png"))
    pieces["br"] = pygame.image.load(str(image_directory / "IMG-20260924-WA0012.png"))
    pieces["bb"] = pygame.image.load(str(image_directory / "IMG-20260924-WA0007.png"))
    pieces["bn"] = pygame.image.load(str(image_directory / "IMG-20260924-WA0017.png"))
    pieces["bp"] = pygame.image.load(str(image_directory / "IMG-20260924-WA0016.png"))

    for piece in pieces:
        pieces[piece] = pygame.transform.scale(
            pieces[piece],
            (80, 80)
        )

    return pieces
