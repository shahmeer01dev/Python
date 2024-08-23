""" Exception handling in Python is a way to manage errors that occur during the execution of a program. It allows you to respond to different error conditions in a controlled manner, preventing your program from crashing unexpectedly. """

"""
Python has a comprehensive hierarchy of built-in exception classes, all derived from the BaseException class. There are over 60 built-in exception classes, organized into several categories, including:

1. Base classes: These provide the foundation for other exceptions. Examples include BaseException, Exception, and Warning.
2. Concrete exceptions: These are specific exceptions that Python raises in response to various errors. Examples include ZeroDivisionError, IndexError, KeyError, and ValueError.
3. OS exceptions: These are related to operating system errors, such as OSError, FileNotFoundError, and PermissionError.
4. Warnings: These are used to alert about potential issues in the code, such as DeprecationWarning and UserWarning12.
"""

# try:
#     numerator = 10
#     denominator = 0
#     result = numerator / denominator
# except:
#     print("Error")

try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])
except ZeroDivisionError:
    print("Denominator cannot be 0.")
except IndexError:
    print("Index Out of Bound.")

# Using else = To run a block of code if no exceptions are raised in the try block.

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1 / num
    print(reciprocal)

# If the input number is even, the else block is executed. If an exception occurs, the else block is skipped.

# Using finally = To run a block of code regardless of whether an exception occurs or not.

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File closed.")

# In this example, the finally block ensures that the file is closed whether or not an exception occurs.

# Rasising Exception: You can raise exceptions using the raise keyword.

# def check_age(age):
#     if age < 18:
#         raise ValueError("Age must be at least 18.")
#     return True

# try:
#     check_age(15)
# except ValueError as e:
#     print(e)

# Here, a ValueError is raised if the age is less than 18, and it’s caught in the except block.

# Custom Exception: You can define your own exceptions by creating a new class that inherits from the Exception class.

class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(e)

# This allows you to create specific error types for your application.