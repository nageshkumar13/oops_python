"""6. Combining Principles
Combining all principles in a single example."""

from abc import ABC, abstractmethod

# Abstraction
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name  # Public attribute
        self.__salary = salary  # Private attribute (encapsulation)

    def get_salary(self):  # Encapsulation with controlled access
        return self.__salary

    @abstractmethod
    def work(self):  # Abstract method
        pass

# Inheritance and Polymorphism
class Developer(Employee):
    def work(self):
        return f"{self.name} writes code."

class Designer(Employee):
    def work(self):
        return f"{self.name} designs user interfaces."

# Using all principles
dev = Developer("Rahul", 80000)
designer = Designer("Anita", 75000)

print(dev.work())  # Output: Rahul writes code.
print(designer.work())  # Output: Anita designs user interfaces.
print("Salary:", dev.get_salary())  # Encapsulation: Output: Salary: 80000
