from abc import ABC, abstractmethod

# Component interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


# Leaf class: Circle
class Circle(Shape):
    def draw(self):
        return "Drawing Circle"


# Leaf class: Rectangle
class Rectangle(Shape):
    def draw(self):
        return "Drawing Rectangle"


# Composite class: CompositeShape
class CompositeShape(Shape):
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw(self):
        result = "Composite Shape:\n"
        for shape in self.shapes:
            result += shape.draw() + "\n"
        return result


# Client code
if __name__ == "__main__":
    # Create individual shapes
    circle = Circle()
    rectangle = Rectangle()

    # Create a composite shape and add individual shapes to it
    composite_shape = CompositeShape()
    composite_shape.add_shape(circle)
    composite_shape.add_shape(rectangle)

    # Draw individual shapes and the composite shape
    print("Drawing individual shapes:")
    print(circle.draw())
    print(rectangle.draw())

    print("\nDrawing composite shape:")
    print(composite_shape.draw())


"""
Shape is the component interface that defines the common interface for all concrete classes (leaf and composite).
Circle and Rectangle are leaf classes implementing the Shape interface.
CompositeShape is a composite class that can contain a collection of leaf nodes (individual shapes) or other composite shapes. It also implements the Shape interface.
The client code demonstrates creating individual shapes (circle and rectangle) and a composite shape. The composite shape can contain both individual shapes and other composite shapes.
"""
