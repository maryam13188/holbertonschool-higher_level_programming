#!/usr/bin/python3

# Import the add function from add_0.py
from add_0 import add

# Define variables a and b in separate lines
a = 1
b = 2

# Calculate the result using the imported function
result = add(a, b)

# Print the formatted result
print("{:d} + {:d} = {:d}".format(a, b, result))

# Prevent execution when imported
if __name__ == "__main__":
    pass
