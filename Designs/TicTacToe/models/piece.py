from enum import Enum


class PieceType(Enum):
    X = 'X'
    O = 'O'


class Piece:
    def __init__(self, piece_type: PieceType):
        self.type = piece_type

    def __str__(self):
        return self.type.value
