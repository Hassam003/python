class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self._pay = pay  # use underscore to indicate “protected/private” use

    @property
    def email(self):
        """Compute email from name (read-only property)."""
        return f"{self.first.lower()}.{self.last.lower()}@company.com"

    @property
    def pay(self):
        """Getter for pay."""
        return self._pay

    @pay.setter
    def pay(self, amount):
        """Setter for pay, with validation."""
        if amount < 0:
            raise ValueError("Pay must be non-negative")
        self._pay = amount

    @pay.deleter
    def pay(self):
        """Deleter: deletes the pay attribute."""
        print("Deleting pay …")
        del self._pay

    def fullname(self):
        return f"{self.first} {self.last}"


# Usage:

emp1 = Employee("Ali", "Khan", 50000)

print(emp1.fullname())         # Ali Khan
print(emp1.email)              # ali.khan@company.com
print(emp1.pay)                # 50000

# Use setter
emp1.pay = 60000
print(emp1.pay)                # 60000

# Try invalid setter
# emp1.pay = -100  # would raise ValueError

# Delete pay
del emp1.pay
# afterwards, accessing emp1.pay would raise AttributeError
