# ================================================
# File Objects — Reading & Writing in Python
# ================================================

# Assume we have a file called "test.txt" in the same directory with some lines of text.

# --- Opening and reading from a file (manual way) ---
f = open("test.txt", "r")   # "r" = read mode
print("File name:", f.name)
print("Mode:", f.mode)
content = f.read()
print("Content of file:")
print(content)
f.close()  # must close manually

print("\n--- Using context manager (best practice) ---")
with open("test.txt", "r") as f2:
    contents2 = f2.read()
    print(contents2)

# After exiting the with-block, f2 is automatically closed
# Trying to read again will raise error

print("\n--- Reading line by line ---")
with open("test.txt", "r") as f3:
    # f3.readlines() gives a list of lines
    lines = f3.readlines()
    print("Lines:", lines)

print("\n--- Using for-loop to read lines efficiently ---")
with open("test.txt", "r") as f4:
    for line in f4:
        print(line, end="")  # `end=""` to avoid extra blank lines

print("\n--- Reading in chunks (for large files) ---")
with open("test.txt", "r") as f5:
    size = 100  # number of characters/chunk size
    chunk = f5.read(size)
    while len(chunk) > 0:
        print(chunk, end="")
        chunk = f5.read(size)

print("\n--- tell() and seek() ---")
with open("test.txt", "r") as f6:
    chunk = f6.read(10)
    print("\nAfter reading 10 chars, position:", f6.tell())
    f6.seek(0)  # move back to start
    print("After seeking back to 0, position:", f6.tell())
    part = f6.read(20)
    print("Next 20 chars:", part)

print("\n--- Writing to text files ---")
with open("test2.txt", "w") as wf:  # "w" = write mode (overwrites or creates new)
    wf.write("This is a new file.\n")
    wf.write("Adding another line.\n")

print("Written to test2.txt.")

print("\n--- Appending instead of overwriting ---")
with open("test2.txt", "a") as af:  # "a" = append mode
    af.write("Appending a third line.\n")

print("Appended to test2.txt.")

print("\n--- Copying a text file ---")
with open("test.txt", "r") as rf, open("test_copy.txt", "w") as wf:
    for line in rf:
        wf.write(line)

print("File copied as test_copy.txt")

print("\n--- Copying binary file (e.g. image) ---")
# Suppose you have "image.jpg" in same folder
with open("image.jpeg", "rb") as rb, open("image_copy.jpg", "wb") as wb:
    chunk_size = 4096
    chunk = rb.read(chunk_size)
    while len(chunk) > 0:
        wb.write(chunk)
        chunk = rb.read(chunk_size)

print("Binary file copied.")
