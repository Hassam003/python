# Lists are ordered, changeable, and allow duplicates
fruits = ["apple", "banana", "cherry", "banana"]
print("Original list:", fruits)

# Access by index
print("fruits[1]:", fruits[1])  # banana

# Change an element
fruits[2] = "orange"
print("After changing index 2:", fruits)

# Add an element
fruits.append("kiwi")
print("After append:", fruits)

# Remove an element
fruits.remove("banana")
print("After remove('banana'):", fruits)

# Loop through the list
print("Looping through list:")
for f in fruits:
    print(" -", f)

print("\n")
