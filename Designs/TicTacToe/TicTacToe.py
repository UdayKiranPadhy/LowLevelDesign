from models.Game import Game
from models.Player import Player
from models.piece import Piece, PieceType

player1 = Player("Uday", Piece(PieceType.X))
player2 = Player("Ajay", Piece(PieceType.O))

game = Game(3)
game.add_player(player1)
game.add_player(player2)

game.play()
