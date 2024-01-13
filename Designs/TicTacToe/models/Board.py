from .piece import Piece


class Board:
    def __init__(self, size: int = 3):
        self.size = size
        self.board: list[list[Piece | None]] = [[None for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                print("|", end="")
                if self.board[i][j] is None:
                    print("_", end="")
                else:
                    print(self.board[i][j].type.value, end="")
                print("|", end="")
            print()

    def place_piece(self, x: int, y: int, piece: Piece) -> bool:
        if self.board[x][y] is not None:
            return False
        self.board[x][y] = piece
        return True

    def is_win(self, x: int, y: int, piece: Piece) -> bool:
        row_match = True
        col_match = True
        diag_match = True
        anti_diag_match = True

        # for row matching
        for i in range(self.size):
            if self.board[i][y] is not None and self.board[i][y].type == piece.type:
                continue
            row_match = False
            break

        for j in range(self.size):
            if self.board[x][j] is not None and self.board[x][j].type == piece.type:
                continue
            col_match = False
            break

        i = 0
        for j in range(self.size):
            if self.board[i][j] is not None and self.board[i][j].type == piece.type:
                i += 1
                continue
            diag_match = False
            break

        i = self.size - 1
        for j in range(self.size - 1, -1, -1):
            if self.board[i][j] is not None and self.board[i][j].type == piece.type:
                i -= 1
                continue
            anti_diag_match = False
            break

        return row_match | col_match | diag_match | anti_diag_match
