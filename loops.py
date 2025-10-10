fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

print("\nLoop over a string:")
message = "hello"
for ch in message:
    print(ch)

print("\nLoop using range():")
for i in range(5):  # 0,1,2,3,4
    print("i =", i)

print("\n--- Using break / continue ---")
for num in range(1, 10):
    if num == 5:
        print("Reached 5, breaking out")
        break
    if num % 2 == 0:
        print(num, "is even — skipping via continue")
        continue
    print(num, "is odd")

print("\nLoop with else clause:")
for n in range(3):
    print("n:", n)
else:
    print("Loop finished without break")

print("\n=== WHILE loop examples ===")

count = 0
while count < 5:
    print("count is", count)
    count += 1

print("\nWhile loop with break:")
n = 0
while True:
    print("Looping, n =", n)
    n += 1
    if n >= 3:
        print("n reached 3, breaking")
        break

print("\nWhile with else clause:")
k = 0
while k < 3:
    print("k:", k)
    k += 1
else:
    print("While loop ended normally (no break)")

print("\nNested loops example:")
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i = {i}, j = {j}")
