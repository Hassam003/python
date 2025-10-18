class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Informal or nicely readable string."""
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    def __repr__(self):
        """Official representation — should be unambiguous and, if possible, evaluable."""
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages!r})"


# Create instances
b1 = Book("1984", "George Orwell", 328)
b2 = Book("Brave New World", "Aldous Huxley", 288)

# Print / str: uses __str__
print(b1)       # '1984' by George Orwell, 328 pages
print(b2)       # 'Brave New World' by Aldous Huxley, 288 pages

# repr: when you inspect or use repr()
print(repr(b1))  # Book(title='1984', author='George Orwell', pages=328)
print(repr(b2))

# In interactive interpreter, when you just type `b1`, __repr__ is used
b1  # shows Book(title='1984', author='George Orwell', pages=328)

# Using both in a list
books = [b1, b2]
print(books)  # the list uses repr for its elements

# If __repr__ is not defined, Python falls back to default representation (e.g., <__main__.Book object at 0x...>)
