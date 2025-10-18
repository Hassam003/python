# Lists

# creating lists
my_list = [1, 2, 3, 4, 5]
print(my_list)           # [1, 2, 3, 4, 5]

# indexing & slicing
print(my_list[0])        # 1
print(my_list[-1])       # 5
print(my_list[1:4])      # [2, 3, 4]
print(my_list[:3])       # [1, 2, 3]
print(my_list[3:])       # [4, 5]

# modifying list
my_list.append(6)
my_list.insert(0, 0)     # insert at index 0
print(my_list)           # [0, 1, 2, 3, 4, 5, 6]

my_list.remove(3)        # remove first occurrence of 3
print(my_list)           # [0, 1, 2, 4, 5, 6]

popped = my_list.pop()   # removes last
print(popped, my_list)   # 6 [0,1,2,4,5]

# sorting / reversing
another = [4, 1, 3, 2, 5]
another.sort()
print(another)           # [1,2,3,4,5]
another.reverse()
print(another)           # [5,4,3,2,1]

# nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])      # 6

# iterate
for element in my_list:
    print(element)

# Tuples

# creating tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])       # 1

# single element tuple (needs comma)
single = (1,)
print(type(single))      # <class 'tuple'>

# unpacking
a, b, c = (10, 20, 30)
print(a, b, c)            # 10 20 30

# immutable: you can’t assign to my_tuple[0]

# Sets

# creating sets
my_set = {1, 2, 3, 4}
print(my_set)            # order may vary

# from list (duplicates removed)
dup = [1, 2, 2, 3, 3, 4]
set_from_dup = set(dup)
print(set_from_dup)      # {1,2,3,4}

# add, remove
my_set.add(5)
my_set.remove(2)
print(my_set)

# set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))        # {1,2,3,4,5,6}
print(a.intersection(b))  # {3,4}
print(a.difference(b))   # {1,2}
print(b.difference(a))   # {5,6}

# set comprehension
squared = {x * x for x in range(10)}
print(squared)           # {0,1,4,9,16,25,36,49,64,81}

# Limitations: set elements must be hashable (immutable types)
