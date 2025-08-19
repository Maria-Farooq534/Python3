"""
Odd/Even & Prime Number Checker

Take a number and check if it’s odd/even.

Extend it to check if it’s prime.
"""

number = int(input("Enter a number : "))

if number % 2 == 0:
    print(f"The {number} is even.")
elif number % 2 == 1:
    print(f"The {number} is odd.")


