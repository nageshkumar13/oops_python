"""Classes and Objects: Classes are blueprints; objects are instances of these blueprints."""
# Class and Object
class Animal:
    def __init__(self, name):
        self.name = name  # Encapsulation (protected member)

    def sound(self):
        return "Some sound"  # Base behavior (to be overridden)

# Inheritance and Polymorphism
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Abstraction using an Interface (or ABC in Python)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Demonstration
dog = Dog("Buddy")  # Object instantiation
cat = Cat("Whiskers")

print(dog.name, ":", dog.sound())  # Polymorphism in action
print(cat.name, ":", cat.sound())

circle = Circle(5)
print("Circle Area:", circle.area())  # Abstraction



class Car:
    def __init__(self, make, model, year):
        self.make = make  # Attributes
        self.model = model
        self.year = year

    def start(self):  # Method
        return f"{self.make} {self.model} starts!"

# Creating Objects
car1 = Car("Toyota", "Camry", 2023)
car2 = Car("Honda", "Civic", 2022)

print(car1.start())  # Output: Toyota Camry starts!
print(car2.start())  # Output: Honda Civic starts!
