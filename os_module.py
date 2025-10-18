import os

# 1. Get current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# 2. List files and directories in current folder
entries = os.listdir()
print("Entries in current directory:", entries)

# 3. Check if a path is file or directory
for name in entries:
    path = os.path.join(cwd, name)
    if os.path.isfile(path):
        print(f"File: {name}")
    elif os.path.isdir(path):
        print(f"Directory: {name}")

print("\n--- Making and removing directories ---")
new_dir = "test_folder"

if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created.")
else:
    print(f"Directory '{new_dir}' already exists.")

# Removing directory (if empty)
if os.path.exists(new_dir) and os.path.isdir(new_dir):
    os.rmdir(new_dir)
    print(f"Directory '{new_dir}' removed.")

print("\n--- Joining and splitting paths ---")
join_path = os.path.join(cwd, "some_folder", "file.txt")
print("Joined path:", join_path)

dir_name, file_name = os.path.split(join_path)
print("Directory portion:", dir_name)
print("Filename portion:", file_name)

# Splitting file name and extension
base, ext = os.path.splitext("example.py")
print("Base:", base, "Extension:", ext)

print("\n--- Checking absolute / relative paths ---")
rel = "folder/subfolder/file.txt"
print("Is absolute?", os.path.isabs(rel))
abs_path = os.path.abspath(rel)
print("Absolute path:", abs_path)

print("\n--- Walking directory tree (os.walk) ---")
for root, dirs, files in os.walk(cwd):
    print("Root:", root)
    print("Dirs:", dirs)
    print("Files:", files)
    print("-----")

print("\n--- Using os.environ (environment variables) ---")
home = os.environ.get("HOME") or os.environ.get("USERPROFILE")
print("Home directory from env:", home)
