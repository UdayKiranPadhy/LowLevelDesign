"""

We shall use the Strategy Pattern to define the movement strategies for different chess pieces.

We can use the Strategy Pattern here because each chess piece has a different way of moving, 
and we want to encapsulate these movement algorithms separately from the piece classes themselves.

We can also use Abstract Factory Pattern to create families of related chess pieces (like all white pieces or all black pieces)
But for simplicity, we will focus on the Strategy Pattern here.

"""

from abc import ABC, abstractmethod
from enum import Enum

class PieceType(Enum):
    KING = "King"
    QUEEN = "Queen"
    ROOK = "Rook"
    BISHOP = "Bishop"
    KNIGHT = "Knight"
    PAWN = "Pawn"

class Piece(ABC):
    def __init__(self):
        self.isKilled = False

    @abstractmethod
    def move_strategy(self):
        pass

class MovementStrategy(ABC):
    @abstractmethod
    def move(self):
        pass

class KingMovementStrategy(MovementStrategy):
    def move(self):
        print("King moves one square in any direction")

class QueenMovementStrategy(MovementStrategy):
    def move(self):
        print("Queen moves any number of squares in any direction")

class RookMovementStrategy(MovementStrategy):
    def move(self):
        print("Rook moves any number of squares horizontally or vertically")

class BishopMovementStrategy(MovementStrategy):
    def move(self):
        print("Bishop moves any number of squares diagonally")

class KnightMovementStrategy(MovementStrategy):
    def move(self):
        print("Knight moves in an 'L' shape: two squares in one direction and then one square perpendicular")

class PawnMovementStrategy(MovementStrategy):
    def move(self):
        print("Pawn moves forward one square, with the option to move two squares on its first move")

class King(Piece):
    def __init__(self, strategy, isWhite):
        super().__init__()
        self.strategy = strategy
        self.isWhite = isWhite

    def move_strategy(self):
        self.strategy.move()

class Queen(Piece):
    def __init__(self, strategy, isWhite):
        super().__init__()
        self.strategy = strategy
        self.isWhite = isWhite

    def move_strategy(self):
        self.strategy.move()

class Rook(Piece):
    def __init__(self, strategy, isWhite):
        super().__init__()
        self.strategy = strategy
        self.isWhite = isWhite

    def move_strategy(self):
        self.strategy.move()

class Bishop(Piece):
    def __init__(self, strategy, isWhite):
        super().__init__()
        self.strategy = strategy
        self.isWhite = isWhite

    def move_strategy(self):
        self.strategy.move()

class Knight(Piece):
    def __init__(self, strategy, isWhite):
        super().__init__()
        self.strategy = strategy
        self.isWhite = isWhite

    def move_strategy(self):
        self.strategy.move()

class Pawn(Piece):
    def __init__(self, strategy, isWhite):
        super().__init__()
        self.strategy = strategy
        self.isWhite = isWhite

    def move_strategy(self):
        self.strategy.move()


class PieceFactory:
    @staticmethod
    def create_piece(piece_type: PieceType, isWhite: bool) -> Piece:
        if piece_type == PieceType.KING:
            return King(KingMovementStrategy(), isWhite)
        elif piece_type == PieceType.QUEEN:
            return Queen(QueenMovementStrategy(), isWhite)
        elif piece_type == PieceType.ROOK:
            return Rook(RookMovementStrategy(), isWhite)
        elif piece_type == PieceType.BISHOP:
            return Bishop(BishopMovementStrategy(), isWhite)
        elif piece_type == PieceType.KNIGHT:
            return Knight(KnightMovementStrategy(), isWhite)
        elif piece_type == PieceType.PAWN:
            return Pawn(PawnMovementStrategy(), isWhite)
        else:
            raise ValueError("Invalid Piece Type")
