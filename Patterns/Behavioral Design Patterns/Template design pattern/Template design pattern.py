"""

It’s a behavioral design pattern that defines the skeleton of an algorithm in a base class, 
while allowing subclasses to override specific steps of that algorithm without changing its structure.

🧠 The Core Idea

You’ve got an overall process (a template) that never changes — a sequence of operations that must happen in a certain order.
But some steps vary depending on context, environment, or data.

So instead of rewriting the entire process every time, you:

Put the common steps in a base class.

Leave hook methods (abstract or overridable) for the variable steps.

Let subclasses fill in the details.


AbstractClass
   ├── template_method()
   ├── step1()
   ├── step2()
   ├── step3()
       ↑
ConcreteClassA
ConcreteClassB


"""

# Step 1: Abstract Base Class
from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water...")

    def pour_in_cup(self):
        print("Pouring into cup...")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

# Step 2: Concrete Implementations
class Tea(Beverage):
    def brew(self):
        print("Steeping the tea bag...")

    def add_condiments(self):
        print("Adding lemon...")
    
class Coffee(Beverage):
    def brew(self):
        print("Dripping coffee through filter...")

    def add_condiments(self):
        print("Adding sugar and milk...")

# Step 3: Client Code
tea = Tea()
print("Preparing Tea:")
tea.prepare_recipe()
print("\nPreparing Coffee:")
coffee = Coffee()
coffee.prepare_recipe()