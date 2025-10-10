def greet(name):
    """
    Function that greets someone.
    name: string parameter
    """
    print(f"Hello, {name}!")


# Calling / invoking the function
greet("Ali")
greet("Sara")

print("\n--- Function with return value ---")


def add(a, b):
    """Return the sum of a and b."""
    return a + b


result = add(5, 3)
print("5 + 3 =", result)

print("\n--- Function with default parameter ---")


def power(base, exponent=2):
    """
    Raise base to the power of exponent.
    If exponent is not given, square the base.
    """
    return base ** exponent


print("power(4):", power(4))  # uses default exponent=2 → 16
print("power(2, 3):", power(2, 3))  # 2^3 = 8

print("\n--- Function with multiple tasks ---")


def describe_person(name, age, hobby):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Hobby: {hobby}")


describe_person("Ali", 25, "painting")

print("\n--- Function calling another function ---")


def square(x):
    return x * x


def sum_of_squares(a, b):
    return square(a) + square(b)


print("Sum of squares of 3 and 4:", sum_of_squares(3, 4))

print("\n--- Variable-length arguments *args, **kwargs ---")


def print_args(*args):
    print("Positional arguments:", args)


def print_keyword_args(**kwargs):
    print("Keyword arguments:", kwargs)


print_args(1, 2, 3, "hello")
print_keyword_args(name="Sara", age=20)

print("\n--- Returning nothing (i.e., returning None implicitly) ---")


def say_goodbye(name):
    print(f"Goodbye, {name}!")


res = say_goodbye("Ahmed")
print("Return value is:", res)  # will print None
