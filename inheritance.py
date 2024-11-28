"""2. Inheritance
Inheritance enables a class to inherit the attributes and methods of another class."""

class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} moves."

class Bird(Animal):  # Bird inherits Animal
    def move(self):
        return f"{self.name} flies."

class Fish(Animal):  # Fish inherits Animal
    def move(self):
        return f"{self.name} swims."

# Creating objects
bird = Bird("Parrot")
fish = Fish("Goldfish")

print(bird.move())  # Output: Parrot flies.
print(fish.move())  # Output: Goldfish swims.
