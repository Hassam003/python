# Sets are unordered, changeable, and do not allow duplicates
nums = {1, 2, 3, 2, 1, 4}
print("Set (duplicates removed):", nums)

# Add an element
nums.add(5)
print("After add(5):", nums)

# Remove an element
nums.remove(2)
print("After remove(2):", nums)

# Check membership
print("3 in nums?", 3 in nums)
print("10 in nums?", 10 in nums)

# Loop through set
print("Looping through set:")
for n in nums:
    print(" ~", n)

print("\n")
