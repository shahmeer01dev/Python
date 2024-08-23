# Opening a File

"""
The mode parameter specifies the mode in which the file is opened:
'r': Read (default mode)
'w': Write (creates a new file or truncates an existing file)
'a': Append (adds to the end of the file)
'b': Binary mode (e.g., 'rb', 'wb')
'+': Read and write (e.g., 'r+', 'w+')
"""

file = open("example.txt", "w")

# Reading from a File

"""
You can read the contents of a file using methods like:
read(): Reads the entire file.
readline(): Reads one line at a time.
readlines(): Reads all lines into a list.
"""

# file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Write in a File

"""
You can write to a file using methods like:
write(): Writes the specified string to the file.
writelines(): Writes all items in a list to the file.
"""

# file = open("example.txt", "w")
file.write("Hello, World!\n")
file.writelines(["Line 1\n", "Line 2\n"])
file.close()

# Appending to a File

# file = open("example.txt", "a")
file.write("Appending a new line.\n")
file.close()


# Using with Statement

"""
The with statement is used for file handling to ensure that the file is properly closed after its suite finishes, even if an exception is raised.
"""
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# No need to explicitly close the file

# Other File Operations

    # 1. Checking if a File Exists: Use the os.path.exists() method.

import os

if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")

    # 2. Renaming a File: Use the os.rename() method.

os.rename("example.txt", "new_example.txt")

    # 3. Deleting a File: Use the os.remove() method.

os.remove("new_example.txt")
