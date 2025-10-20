"""

What It Is

The Bridge Design Pattern is a structural pattern that separates an abstraction from its implementation so that both can vary independently.

That’s a fancy way of saying:
Stop hard-wiring your features together. Make them composable instead of nested.

You bridge the gap between two orthogonal hierarchies:

Abstraction (the high-level control, e.g., Shape)

Implementation (the low-level details, e.g., DrawingAPI)

The abstraction knows about the implementation but doesn’t depend on its concrete form.

"""

from abc import ABC, abstractmethod

# The "Implementor" Interface
class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        pass


# Concrete Implementations
class VectorAPI(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"VectorAPI: Drawing circle at ({x}, {y}) with radius {radius}")

class RasterAPI(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"RasterAPI: Drawing pixels for circle at ({x}, {y}) with radius {radius}")


# The "Abstraction"
class Shape(ABC):
    def __init__(self, drawing_api: DrawingAPI):
        self._drawing_api = drawing_api

    @abstractmethod
    def draw(self):
        pass


# Refined Abstraction
class Circle(Shape):
    def __init__(self, x, y, radius, drawing_api):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self._drawing_api.draw_circle(self.x, self.y, self.radius)


# Client code
vector_circle = Circle(10, 20, 5, VectorAPI())
raster_circle = Circle(15, 30, 8, RasterAPI())

vector_circle.draw()
raster_circle.draw()



"""

Why You’d Actually Use This

Avoid subclass explosion.
Combine behaviors dynamically rather than pre-baking them in the class tree.

Keep abstractions independent.
Change your UI logic without breaking your rendering engine.

Enable runtime binding.
You can choose an implementation at runtime—useful in plugin or cross-platform architectures.

Promote loose coupling.
Classes depend on interfaces, not concrete implementations (classic Dependency Inversion).

"""

"""

Real-World Examples

Database Connectors
An ORM can separate data model abstractions (like User, Order, Product) from database implementations (MySQL, PostgreSQL, MongoDB). You can switch databases without rewriting models.

UI Frameworks
A button abstraction (Button) can use different rendering engines (WinButtonAPI, MacButtonAPI, WebButtonAPI).

Cross-Platform Game Engines
The game logic (abstraction) is the same, but the rendering backend (implementation) could be DirectX, Vulkan, or OpenGL.

Cloud Services
An abstraction layer for file storage can be bridged to multiple providers: AWS S3, Azure Blob, Google Cloud Storage.

Logging Systems
A logger abstraction can delegate to different logging providers—file, console, remote service—without changing application code.

"""