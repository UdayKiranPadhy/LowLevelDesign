from .piece import Piece


class Player:
    def __init__(self, name: str, piece: Piece):
        self.name = name
        self.piece = piece
