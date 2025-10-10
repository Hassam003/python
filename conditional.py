number = 7

# if / elif / else
if number > 10:
    print(f"{number} is greater than 10")
elif number == 10:
    print(f"{number} is exactly 10")
else:
    print(f"{number} is less than 10")

print("\n--- FOR loop example ---")
# for loop: iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

print("\n--- WHILE loop example ---")
# while loop: repeat until condition is False
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # increment by 1

print("\nLoop done!")

# Combining loops and conditionals
print("\n--- Combined example: numbers and classification ---")
nums = [2, 7, 12, 5, 20]
for n in nums:
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
