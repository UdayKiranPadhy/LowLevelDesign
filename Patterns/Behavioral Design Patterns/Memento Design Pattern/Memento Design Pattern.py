"""

It’s a behavioral design pattern used to capture and externalize an 
object’s internal state without violating encapsulation, so you can restore it to that state later.


When an object’s state changes, you might want to:

Undo an operation,

Roll back a transaction,

Restore a previous configuration.

The Memento pattern lets you do this without exposing the object’s private data to the outside world.
You ask the object to hand you a memento, store it, and later hand it back to the object to restore itself.

Client
   ↓
Originator → Memento ← Caretaker

Originator: The object whose state you want to save.

Memento: Stores the internal state of the originator.

Caretaker: Keeps the mementos safe but doesn’t look inside.

"""

# Step 1: The Memento
class TextMemento:
    def __init__(self, text):
        self._text = text

    def get_saved_text(self):
        return self._text

# Step 2: The Originator
class TextEditor:
    def __init__(self):
        self._text = ""

    def type(self, words):
        self._text += words

    def save(self):
        return TextMemento(self._text)

    def restore(self, memento):
        self._text = memento.get_saved_text()

    def get_text(self):
        return self._text

# Step 3: The Caretaker
class TextEditorHistory:
    def __init__(self):
        self._history = []

    def push(self, memento):
        self._history.append(memento)

    def pop(self):
        return self._history.pop() if self._history else None

# Step 4: Client code
if __name__ == "__main__":
    editor = TextEditor()
    history = TextEditorHistory()

    editor.type("Hello, ")
    editor.type("world!")
    print("Current Text:", editor.get_text())

    # Save
    history.push(editor.save())
    editor.type(" This is a Memento pattern example.")
    print("After typing more:", editor.get_text())