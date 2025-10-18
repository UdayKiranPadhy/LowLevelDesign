"""

Factory Method Pattern (aka Simple Factory on caffeine)
Intent

Defines an interface for creating one kind of object, but lets subclasses decide which concrete class to instantiate.
It’s about delegating object creation to subclasses.




"""


from abc import ABC, abstractmethod

# Product
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Products
class WindowsButton(Button):
    def render(self):
        return "Rendering a Windows-style button"

class MacButton(Button):
    def render(self):
        return "Rendering a Mac-style button"

# Creator
class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render(self):
        button = self.create_button()
        print(button.render())

# Concrete Creators
class WindowsDialog(Dialog):
    def create_button(self):
        return WindowsButton()

class MacDialog(Dialog):
    def create_button(self):
        return MacButton()

# Usage
dialog = WindowsDialog()
dialog.render()  # Rendering a Windows-style button



"""

Key idea: Each subclass decides which concrete button to create, but the main workflow (render()) is shared.

🏢 2. Abstract Factory Pattern (aka Factory of Factories)
Intent

Defines an interface for creating families of related or dependent objects without specifying their concrete classes.
It’s about producing entire product families that are designed to work together.

Analogy

Imagine designing an entire UI theme (not just buttons).
A Windows UI has buttons, checkboxes, menus — all styled consistently.
The Abstract Factory ensures that when you pick a theme, all UI elements belong to that family.

"""


from abc import ABC, abstractmethod

# Product Families
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def toggle(self):
        pass

# Concrete Products
class WindowsButton(Button):
    def render(self):
        return "Windows Button"

class WindowsCheckbox(Checkbox):
    def toggle(self):
        return "Windows Checkbox toggled"

class MacButton(Button):
    def render(self):
        return "Mac Button"

class MacCheckbox(Checkbox):
    def toggle(self):
        return "Mac Checkbox toggled"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

# Client code
def build_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.toggle())

# Usage
factory = MacFactory()
build_ui(factory)


"""

Key idea:
When you switch from MacFactory to WindowsFactory, your entire family of products changes — consistent, compatible, and cohesive.

🧠 Difference Breakdown
Aspect	Factory Method	Abstract Factory
Purpose	Creates one product	Creates families of related products
Scope	Single object	Multiple related objects
Flexibility	Subclass decides which object to create	Factory object decides which product family to use
Example analogy	One pizza store makes its own pizzas	Entire restaurant chain produces full menu sets (pizza, drinks, dessert)
Inheritance used for	Defining creation in subclasses	Encapsulating families of factories
Output type	One concrete class	Several objects that belong together
Complexity	Simpler, single hierarchy	More complex, deals with multiple hierarchies

"""