class Employee:
    """Base / parent class for all employees."""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    def raise_pay(self, amount):
        self.pay += amount
        return self.pay


class Developer(Employee):
    """Subclass of Employee — a specific kind of employee."""

    def __init__(self, first, last, pay, prog_lang):
        # call the parent constructor to initialize inherited attributes
        super().__init__(first, last, pay)
        # now add subclass-specific attribute
        self.prog_lang = prog_lang

    def __str__(self):
        return f"{self.fullname()} — Developer in {self.prog_lang}"


class Manager(Employee):
    """Subclass that adds management functionality."""

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # employees is a list of Employee objects that this manager manages
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        print(f"Manager: {self.fullname()} manages:")
        for e in self.employees:
            print("  -", e.fullname())


# --- Using the classes ---

dev1 = Developer("Ali", "Khan", 80000, "Python")
dev2 = Developer("Sara", "Ahmed", 90000, "Java")

mgr = Manager("Hassan", "Rizwan", 150000, employees=[dev1])

print(dev1)               # uses Developer’s __str__ (if defined) or fallback
print(dev2.fullname(), dev2.prog_lang)
print("Before raise:", dev1.pay)
dev1.raise_pay(5000)
print("After raise:", dev1.pay)

mgr.print_employees()
mgr.add_employee(dev2)
mgr.print_employees()
mgr.remove_employee(dev1)
mgr.print_employees()
