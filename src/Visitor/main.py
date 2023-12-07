# Define the visitor interface
class ShapeVisitor:
    def visit_circle(self, circle):
        pass

    def visit_square(self, square):
        pass

# Define the shape interface
class Shape:
    def accept(self, visitor):
        pass

# Concrete implementation of Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)

# Concrete implementation of Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def accept(self, visitor):
        visitor.visit_square(self)

# Concrete implementation of a visitor to calculate area and perimeter
class AreaPerimeterVisitor(ShapeVisitor):
    def visit_circle(self, circle):
        area = 3.14 * circle.radius * circle.radius
        perimeter = 2 * 3.14 * circle.radius
        print(f"Circle - Area: {area}, Perimeter: {perimeter}")

    def visit_square(self, square):
        area = square.side * square.side
        perimeter = 4 * square.side
        print(f"Square - Area: {area}, Perimeter: {perimeter}")

# Client code
if __name__ == "__main__":
    shapes = [Circle(5), Square(4), Circle(3), Square(6)]

    # Create a visitor
    visitor = AreaPerimeterVisitor()

    # Apply the visitor to each shape
    for shape in shapes:
        shape.accept(visitor)
