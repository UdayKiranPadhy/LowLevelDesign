"""

Chain of Responsibility

Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon
receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.


This pattern is used in the following cases:

        * More than one object may handle a request, and the handler isn’t known a priori. The handler should be ascertained
        automatically.
        * You want to issue a request to one of several objects without specifying the receiver explicitly.
        * The set of objects that can handle a request should be specified dynamically.

Example:
    ATM Dispenser
    * ATM Dispenser has 3 handlers, for 100, 50 and 20 notes.
    * Each handler has a successor, which is the next handler in the chain.
    * When a request is made, the ATM dispenser checks if it can dispense the requested amount.
    * If it can, it dispenses the amount and returns.
    * If it cannot, it passes the request to the next handler in the chain.
    * This continues until the request is handled or the chain ends.
    * If the chain ends without handling the request, the ATM dispenser cannot dispense the amount.

    Discount Calculator
    Logger
    Exception Handling

"""


class Handler:
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    def __init__(self, successor=None):
        self._successor = successor

    def set_successor(self, successor):
        self._successor = successor

    def handle(self, request):
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler class.
    """

    def handle(self, request):
        if self._successor:
            return self._successor.handle(request)
        return None


class ConcreteHandler1(AbstractHandler):
    """
    All Concrete Handlers either handle a request or pass it to the next handler
    in the chain.
    """

    def handle(self, request):
        if request == "1":
            return f"ConcreteHandler1: I'll handle the {request}.\n"
        else:
            return super().handle(request)


class ConcreteHandler2(AbstractHandler):
    def handle(self, request):
        if request == "2":
            return f"ConcreteHandler2: I'll handle the {request}.\n"
        else:
            return super().handle(request)


class ConcreteHandler3(AbstractHandler):
    def handle(self, request):
        if request == "3":
            return f"ConcreteHandler3: I'll handle the {request}.\n"
        else:
            return super().handle(request)


def client_code(handler):
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for request in ["1", "2", "3", "4"]:
        print(f"\nClient: Who wants to handle the request {request}?")
        result = handler.handle(request)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {request} was left untouched.", end="")

if __name__ == "__main__":
    """
    The other part of the client code constructs the actual chain.
    """

    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()

    handler1.set_successor(handler2)
    handler2.set_successor(handler3)

    print("Chain: Handler1 > Handler2 > Handler3\n")
    client_code(handler1)
    print("\n")

    print("Subchain: Handler2 > Handler3\n")
    client_code(handler2)
    print("\n")