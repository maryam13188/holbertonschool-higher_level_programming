#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

# Build the output message
message = f"Last digit of {number} is {last_digit} and is"

# Add the condition part
if last_digit > 5:
    message += " greater than 5"
elif last_digit == 0:
    message += " 0"
else:
    message += " less than 6 and not 0"

print(message)
