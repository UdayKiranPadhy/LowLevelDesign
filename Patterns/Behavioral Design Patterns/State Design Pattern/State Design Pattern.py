"""

The State Design Pattern is what happens when your object finally grows a personality disorder — and you decide to manage it properly.

It’s a behavioral design pattern that lets an object change its behavior when its internal state changes.
From the outside, it looks like the object itself changed class.

Imagine a music player:

When it’s stopped, pressing play starts music.

When it’s playing, pressing play pauses it.

When it’s paused, pressing play resumes it.

With the State pattern, each state (Playing, Paused, Stopped) is a separate class, and each knows how to handle inputs appropriately.
The main Player object just says, “Whatever my current state is, you deal with it.”


Context
  ├── State (interface)
  │      ├── ConcreteStateA
  │      └── ConcreteStateB

Context: The object that has a current state and delegates behavior to it.
State: Defines the interface for behavior.
Concrete States: Implement specific behaviors for each state.

"""

# Step 1: The State interface
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def press_play(self, player):
        pass

# Step 2: Concrete States
class PlayingState(State):
    def press_play(self, player):
        print("Pausing the music.")
        player.state = PausedState()

class PausedState(State):
    def press_play(self, player):
        print("Resuming the music.")
        player.state = PlayingState()

class StoppedState(State):
    def press_play(self, player):
        print("Starting the music.")
        player.state = PlayingState()

# Step 3: The Context
class MusicPlayer:
    def __init__(self):
        self.state = StoppedState()

    def press_play(self):
        self.state.press_play(self)

# Step 4: Client code
player = MusicPlayer()
player.press_play()  # Starting the music.
player.press_play()  # Pausing the music.
player.press_play()  # Resuming the music.
player.press_play()  # Pausing the music.