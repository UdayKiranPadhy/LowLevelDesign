from collections import deque

from .Board import Board
from .Player import Player


class Game:
    def __init__(self, size: int = 3, players: deque = deque()):
        self.size = size
        self.board = Board(size)
        self.players: deque = players

    def __str__(self):
        return str(self.board)

    def __repr__(self):
        return str(self.board)

    def add_player(self, player: Player):
        self.players.append(player)

    def play(self):
        while True:
            player_to_play: Player = self.players.popleft()
            self.board.print_board()
            print(f"{player_to_play.name}'s turn")
            x, y = list(map(int, input("Enter cord: ").split(",")))
            if self.board.place_piece(x, y, player_to_play.piece):
                self.players.append(player_to_play)
            else:
                print("Invalid move player to play again")
                self.players.appendleft(player_to_play)

            if self.board.is_win(x, y, player_to_play.piece):
                print(f"{player_to_play.name} won!")
                self.board.print_board()
                break
