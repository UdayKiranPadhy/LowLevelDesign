"""

For extensibality, the game can be extended to support boards of different sizes or even different variants of chess.
For example, we can create a 10x10 board for a variant of chess that includes additional pieces.
We can also implement different rules for movement or capturing based on the variant being played.

"""

if __name__ == "__main__":
    from Designs.Chess.models.Player import Player
    from Designs.Chess.models.Board import Board
    from Designs.Chess.models.Piece import Piece

    # Create players
    player1 = Player("Alice", True)
    player2 = Player("Bob", False)

    # Initialize board
    board = Board(player1=player1, player2=player2)
    board.initialize()


    # Display player information
    print(f"Player 1: {player1.get_name()}, Color: {'White' if player1.is_white() else 'Black'}")
    print(f"Player 2: {player2.get_name()}, Color: {'White' if player2.is_white() else 'Black'}")

    board.play()