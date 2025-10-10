# Tuples are ordered, unchangeable, and allow duplicates
colors = ("red", "green", "blue", "green")
print("Tuple:", colors)

# Access by index
print("colors[0]:", colors[0])

# Loop through tuple
print("Looping through tuple:")
for c in colors:
    print(" *", c)

# Tuple unpacking
a, b, c, d = colors
print("Unpacked:", a, b, c, d)

print("\n")
