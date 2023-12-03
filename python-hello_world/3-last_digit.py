#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10

# Determine the sign for display
sign = '-' if number < 0 else ''

# Output the result based on conditions
print(f"Last digit of {number} is {sign}{last_digit} and", end=' ')

if last_digit > 5:
    print("is greater than 5")
elif last_digit == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")