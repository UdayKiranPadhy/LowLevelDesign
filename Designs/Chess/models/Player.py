"""

This module defines the Player class, which represents a player in the chess game.
We can also use Strategy Pattern to define different playing strategies for players
(like aggressive, defensive, etc.), but for simplicity, we will just define the basic Player class here.

"""

class Player:
    def __init__(self, name, isWhite):
        self.name = name
        self.isWhite = isWhite

    def get_name(self):
        return self.name

    def is_white(self):
        return self.isWhite