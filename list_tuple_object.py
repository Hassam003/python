# Sorting Lists, Tuples, and Objects in Python

# ----- Basic list sorting -----
from operator import attrgetter
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li)
print('Sorted list:\t', s_li)
print('Original list:\t', li)

# Sort in-place (changes the list)
li.sort()
print('After sort():\t', li)

# Sort descending
s_li_desc = sorted(li, reverse=True)
print('Descending:\t', s_li_desc)

# ----- Sorting tuples -----
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print('Tuple sorted:\t', s_tup)

# ----- Sorting sets -----
di = {9, 1, 8, 2, 7, 3, 6, 4, 5}
s_di = sorted(di)
print('Set sorted:\t', s_di)

# ----- Sorting strings -----
s = 'sortingexample'
s_sorted = sorted(s)
print('String sorted:\t', s_sorted)

# ----- Sorting by absolute value -----
li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print('Absolute sort:\t', s_li)

# ----- Sorting dictionaries by value -----
d = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_d = sorted(d)
print('Dict sort (keys):', s_d)

# ----- Sorting custom objects -----


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'({self.name}, {self.age}, ${self.salary})'


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

# Sort by name (using attrgetter)

s_employees = sorted(employees, key=lambda e: e.name)
print('\nSorted by name:\t', s_employees)

s_employees = sorted(employees, key=lambda e: e.age)
print('Sorted by age:\t', s_employees)

s_employees = sorted(employees, key=lambda e: e.salary, reverse=True)
print('Sorted by salary (desc):', s_employees)

# Using attrgetter (cleaner & faster)
s_employees = sorted(employees, key=attrgetter('age'))
print('Using attrgetter(age):', s_employees)

s_employees = sorted(employees, key=attrgetter('salary'))
print('Using attrgetter(salary):', s_employees)
