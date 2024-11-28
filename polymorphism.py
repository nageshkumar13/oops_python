"""4. Polymorphism
Polymorphism allows the same method name to behave differently based on the object.

Example:"""

class Shape:
    def area(self):
        pass  # Base method, no implementation

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Objects of different shapes
rect = Rectangle(4, 5)
circle = Circle(3)

print("Rectangle Area:", rect.area())  # Output: Rectangle Area: 20
print("Circle Area:", circle.area())   # Output: Circle Area: 28.26
