# Author: Caleb Moura

# Function 1: add_numbers
def add_numbers(a, b):
    """
    Add a and b
    """
    return a + b

# Function 2: subtract_numbers
def subtract_numbers(c, d):
    """
    subtract d from c
    """
    return c - d 

# Function 3: multiply_operations
def multiply_operations(x, y):
    """
    multiply the results of a + b and c - d
    """
    return x * y
# Test cases for multiply_operations function using "if" statements
result_1 = multiply_operations(2, 3)
if result_1 == 6:
    print("correct")
else:
    print("incorrect")

result_2 = multiply_operations(-1, 5)
if result_2 == 7:
    print("correct")
else:
    print("incorrect")

result_3 = multiply_operations(0, 0)
if result_3 == 0:
    print("correct")
else:
    print("incorrect")

result_4 = multiply_operations(10, -2)
if result_4 == -20:
    print("correct")
else:
    print("incorrect")