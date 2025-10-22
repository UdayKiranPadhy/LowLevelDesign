"""

We can use Observer Pattern to notify players about the moves made by the opponent and log the moves.
Where the Player class can implement the Observer interface to get notified about the moves.
And the Board class or Piece class can implement the Observable interface to notify the players.
But for simplicity, we will shall not implement it here.

We can also use State Design Pattern for players to manage whose turn it is to play.
The Board class can have a state which can be either Player1TurnState or Player2TurnState.
Each state will handle the move accordingly and switch the state after a valid move.
But for simplicity, we are skipping that here.

Used Singleton Pattern to ensure only one instance of the Board exists during a game.

"""

from enum import Enum
from Designs.Chess.models import Piece
from Designs.Chess.models.Player import Player


class Cell:
    def __init__(self, x: int, y: int, piece: Piece = None):
        self.x = x
        self.y = y
        self.piece = piece

class BoardState(Enum):
    ACTIVE = "Active"
    CHECK = "Check"
    CHECKMATE = "Checkmate"
    STALEMATE = "Stalemate"

class Board:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, player1: Player, player2: Player):
        self.cells = [[Cell(x, y) for y in range(8)] for x in range(8)]
        self.player1 = player1
        self.player2 = player2
        self.isWhiteTurn = True
        self.initialize()
        self.board_history = []
        self.boardstate = BoardState.ACTIVE
    
    def initialize(self):
        # Initialize pieces on the board
        for x in range(8):
            for y in range(8):
                if x == 1:
                    self.cells[x][y].piece = Piece.PieceFactory.create_piece(Piece.PieceType.PAWN, False)
                elif x == 6:
                    self.cells[x][y].piece = Piece.PieceFactory.create_piece(Piece.PieceType.PAWN, True)
                elif x == 0 or x == 7:
                    isWhite = (x == 7)
                    if y == 0 or y == 7:
                        self.cells[x][y].piece = Piece.PieceFactory.create_piece(Piece.PieceType.ROOK, isWhite)
                    elif y == 1 or y == 6:
                        self.cells[x][y].piece = Piece.PieceFactory.create_piece(Piece.PieceType.KNIGHT, isWhite)
                    elif y == 2 or y == 5:
                        self.cells[x][y].piece = Piece.PieceFactory.create_piece(Piece.PieceType.BISHOP, isWhite)
                    elif y == 3:
                        self.cells[x][y].piece = Piece.PieceFactory.create_piece(Piece.PieceType.QUEEN, isWhite)
                    elif y == 4:
                        self.cells[x][y].piece = Piece.PieceFactory.create_piece(Piece.PieceType.KING, isWhite)

    def play(self):
        while self.boardstate == BoardState.ACTIVE:
            # Get current player
            current_player = self.player1 if self.isWhiteTurn else self.player2

            # Get and validate move
            move = current_player.get_move()
            if self.validate_move(move, current_player):
                self.make_move(move, current_player)
                self.switch_turn()
            else:
                print("Invalid move. Try again.")
    
    def validate_move(self, move, player: Player):
        # Implement move validation logic
        pass

    def make_move(self, move, player: Player):
        # Implement move execution logic
        pass

    def switch_turn(self):
        self.isWhiteTurn = not self.isWhiteTurn