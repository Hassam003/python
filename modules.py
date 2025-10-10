import datetime
import os
import utils  # your own module
from math import factorial, floor
import random as rnd
import math

print("math.pi:", math.pi)
print("math.sqrt(16):", math.sqrt(16))

# 2. Import with alias

# Generate a random integer between 1 and 10
print("random integer 1-10:", rnd.randint(1, 10))

# 3. Import specific functions or names

print("factorial(5):", factorial(5))
print("floor(3.7):", floor(3.7))

# 4. Use functions from modules + your own module

# Suppose you create your own module in another file, utils.py:
# contents of utils.py might be:
#
# def greet(name):
#     return f"Hello, {name}!"
#
# def is_even(n):
#     return n % 2 == 0
#
# (You’d put that file in same folder or in Python path.)

# Then you import and use:

print(utils.greet("Ali"))
print("Is 7 even?", utils.is_even(7))
print("Is 8 even?", utils.is_even(8))

# 5. Exploring the standard library — example: os, datetime

print("Current working directory:", os.getcwd())
print("List of files:", os.listdir("."))

now = datetime.datetime.now()
print("Current date & time:", now)
print("Year:", now.year, "Month:", now.month, "Day:", now.day)

# 6. dir() and help() — exploring module contents
print("\nNames in math module:", dir(math))
print("\nHelp on math.sqrt:")
help(math.sqrt)
