"""

the software equivalent of “there can be only one.” 
It’s the design pattern that makes sure only one instance of a class ever exists, 
and that all references point to that same instance.


🧠 What It Does

The Singleton pattern ensures:
Single Instance — Only one object of a class exists throughout the program.
Global Access Point — Everyone references that same instance.
Lazy Initialization — The instance is created only when first needed.

Perfect for:
Database connections
Thread pools
Configuration managers
Logging systems

Terrible for:
Anything else where you’re just too lazy to pass a reference.

"""

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# Example usage
a = Singleton()
b = Singleton()
print(a is b)  # True


# This approach overrides __new__, which controls object creation before __init__ runs. 
# Once _instance exists, future calls return the same object.
# If you find yourself overusing Singletons, take a breath and consider dependency injection instead.