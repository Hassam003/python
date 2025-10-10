class Dog:
    # Class variable — shared by all instances
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance variables — unique to each instance
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"


# Create instances
dog1 = Dog("Buddy", 4)
dog2 = Dog("Lucy", 2)

# Accessing instance attributes
print(dog1.name, dog1.age)  # Buddy 4
print(dog2.name, dog2.age)  # Lucy 2

# Accessing class attribute
print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris
print(Dog.species)   # Canis familiaris

print("\nChanging dog1's name and age:")
dog1.name = "Max"
dog1.age = 5
print(dog1.description())

print("\nChanging the class variable:")
Dog.species = "Canine"

print("dog1.species:", dog1.species)  # updated
print("dog2.species:", dog2.species)  # updated
print("Dog.species:", Dog.species)

print("\nOverriding class variable in an instance:")
dog2.species = "Wolf-dog"
print("dog2.species (after override):", dog2.species)
print("dog1.species:", dog1.species)
print("Dog.species:", Dog.species)

# Checking attribute resolution
print("\nWhere is species looked up for dog2?")
# includes instance variables, including if species overridden
print(dog2.__dict__)
print(Dog.__dict__)   # includes the class attribute species
