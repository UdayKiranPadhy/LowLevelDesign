"""

The Command Pattern encapsulates a request as an object, allowing you to parameterize clients 
with different requests, queue or log them, and support undoable operations.

Basically, you convert every “action” (like turn the light on, delete a file, place an order) into a command object with a execute() method.
This object knows:

What needs to be done,
Who should do it,
When to do it.


Client → Invoker → Command → Receiver

Command: Abstract interface with execute() and possibly undo().

ConcreteCommand: Wraps a request and calls the receiver.

Receiver: Knows how to perform the actual action.

Invoker: Triggers commands (like a button or scheduler).

Client: Creates and wires everything.

"""


# Step 1: The Receiver (the actual worker)

class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")

# Step 2: The Command interface and Concrete Commands

class Command:
    def execute(self):
        pass

    def undo(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

# Step 3: The Invoker (remote control)

class RemoteControl:
    def __init__(self):
        self._command_history = []

    def press_button(self, command):
        command.execute()
        self._command_history.append(command)

    def press_undo(self):
        if self._command_history:
            command = self._command_history.pop()
            command.undo()

# Client code
light = Light()

light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()

remote.press_button(light_on)   # Light is ON
remote.press_button(light_off)  # Light is OFF

remote.press_undo()             # Undo last action -> Light is ON again

"""

Light is ON
Light is OFF
Light is ON


"""