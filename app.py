x = 'Awesome'


def myfunc():
    global x
    x = 'Fantastic'
    print(x)


myfunc()

print(x)

age = 36
txt = "My name is John, I am ", age
print(txt)

my_string = "hello"
print(my_string[0])

print('a' < 'b')
print('ab' > 'aa')
print('a' == 'A')

print(ord('a'))
print(ord('A'))

temperature = 9

if temperature > 30:
    print("It's warm outside. You should drink water.")

elif temperature >= 20:
    print("It's nice")

else:
    print("It's cold")

print("Done")


age = 18
message = "Eligible" if age >= 18 else "Not Eligible"  # Ternary Operator
print(message)

if age >= 18 and age < 65:
    print("Eligible")

if 18 <= age < 65:          # Chaining Comparison Operator, Thats how we write in maths
    print("Eligible")


for x in range(1, 10, 3):
    print("Hello World", x)


successful = False

for number in range(1, 4):
    print("Attempt")
    if successful:
        print("Successful")
        break
    else:
        print("False")
else:
    print("Failed")

for z in range(5):
    for y in range(3):
        print(f"{z},{y}")

count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x, count)
print(f"We have {count} even numbers")


# function that perform specific task
def greet(first, last):
    print(f"My name is {first} {last}")


greet("Hassam", "Umer")


# function that returns any value
def greetName(first, last):
    return f"Hi! My name is {first} {last}"


message = greetName("John", "Smith")

print(message)


# By default function return None (absence of value)
def alpha():
    print("Joy Land")


print(alpha())


# key argument
def sum(k, l):
    return k+l


print(sum(k=2, l=7))


# default parameter
def sum(k=8, l=9):
    return k+l


print(sum())


# xargs
def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


print("Start")
print(multiply(2, 3, 4, 5, 7))


# xxargs
def saveUser(**user):
    print(user["id"], user["name"])


saveUser(id=5, name="John", age=56)


def fizzBuzz(input):
    if input % 3 == 0 and input % 5 == 0:
        print("Fizz Buzz")
    elif input % 3 == 0:
        print("Fizz")
    elif input % 5 == 0:
        print("Buzz")
    else:
        print(input)


fizzBuzz(8)

z = (1, "2", 3, False, (2, 2, 2), [1, 2, 2])
x = (1, "2", 3, False, (2, 2, 2), [1, 2, 2])
print(z is x)

char = list("Hello World")
print(char)

letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0:3])
print(letters[:])  # copy of original list
print(letters[::-1])
