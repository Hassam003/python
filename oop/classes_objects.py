# ================================
# Classes & Instances — OOP Basics
# ================================

class Dog:
    """A simple Dog class example."""
    # Class attribute — shared by all instances
    species = "Canis familiaris"

    def __init__(self, name, age):
        """Initialize a new Dog instance."""
        self.name = name   # instance attribute
        self.age = age     # instance attribute

    def __str__(self):
        """Return a readable string representation."""
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        """Instance method: make the dog speak."""
        return f"{self.name} says {sound}"


# Create instances of Dog
dog1 = Dog("Max", 5)
dog2 = Dog("Bella", 3)

# Use the methods and attributes
print(dog1)                 # calls __str__, e.g. "Max is 5 years old."
print(dog2.name, dog2.age)  # “Bella 3”

print(dog1.speak("Woof"))   # “Max says Woof”
print(dog2.speak("Bark"))   # “Bella says Bark”

# Class attribute access
print("Species:", dog1.species, dog2.species)
print("Access via class:", Dog.species)
