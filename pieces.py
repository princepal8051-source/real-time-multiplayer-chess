import pygame

def load_pieces():

    pieces = {}

    pieces["wk"] = pygame.image.load("/Users/princepal/Desktop/Chess_klt60.png")
    pieces["wq"] = pygame.image.load("/Users/princepal/Desktop/Chess_qlt60.png")
    pieces["wr"] = pygame.image.load("/Users/princepal/Desktop/Chess_rlt60.png")
    pieces["wb"] = pygame.image.load("/Users/princepal/Desktop/Chess_blt60.png")
    pieces["wn"] = pygame.image.load("/Users/princepal/Desktop/Chess_nlt60.png")
    pieces["wp"] = pygame.image.load("/Users/princepal/Desktop/Chess_plt60.png")

    pieces["bk"] = pygame.image.load("/Users/princepal/Desktop/Chess_kdt60.png")
    pieces["bq"] = pygame.image.load("/Users/princepal/Desktop/Chess_qdt60.png")
    pieces["br"] = pygame.image.load("/Users/princepal/Desktop/Chess_rdt60.png")
    pieces["bb"] = pygame.image.load("/Users/princepal/Desktop/Chess_bdt60.png")
    pieces["bn"] = pygame.image.load("/Users/princepal/Desktop/Chess_ndt60.png")
    pieces["bp"] = pygame.image.load("/Users/princepal/Desktop/Chess_pdt60.png")

    for piece in pieces:
        pieces[piece] = pygame.transform.scale(
            pieces[piece],
            (80, 80)
        )

    return pieces