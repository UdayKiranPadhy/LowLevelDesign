"""

The Mediator Pattern defines an object that encapsulates how a set of objects interact. 
It promotes loose coupling by preventing objects from referring to each other explicitly, 
letting you vary their interactions independently.


Client
   ↓
Mediator Interface → Concrete Mediator
   ↑                     ↑
Colleague Interface   Concrete Colleagues


Mediator: Defines communication methods for colleagues.

ConcreteMediator: Implements coordination logic.

Colleague: Objects that send messages via the mediator instead of directly to each other.

"""

# Step 1: The Mediator Interface
from abc import ABC, abstractmethod

class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, msg, user):
        pass


# Step 2: Concrete Mediator
class ConcreteChatMediator(ChatMediator):
    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def send_message(self, msg, sender):
        for user in self._users:
            if user != sender:
                user.receive(msg)


# Step 3: Colleague
class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send(self, msg):
        print(f"{self.name} sends: {msg}")
        self.mediator.send_message(msg, self)

    def receive(self, msg):
        print(f"{self.name} receives: {msg}")


# Step 4: Client code
mediator = ConcreteChatMediator()

alice = User("Alice", mediator)
bob = User("Bob", mediator)
charlie = User("Charlie", mediator)

mediator.add_user(alice)
mediator.add_user(bob)
mediator.add_user(charlie)

alice.send("Hey everyone!")
bob.send("Hi Alice!")
