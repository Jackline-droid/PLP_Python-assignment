"""
This is a simple calculator program.
It performs basic arithmetic operations: addition, subtraction, multiplication, and division.
"""


# 🧮 Simple Calculator Program

# Ask the user to enter the first number
first_number = input("Enter the first number: ")
first_number = float(first_number)  # convert to a number

# Ask the user to enter the second number
second_number = input("Enter the second number: ")
second_number = float(second_number)

# Ask the user to choose an operation
print("Choose an operation:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
operation = input("Enter operation symbol: ")

# Perform the operation
if operation == "+":
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")

elif operation == "-":
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")

elif operation == "*":
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")

elif operation == "/":
    if second_number == 0:
        print("Oops! You can't divide by zero.")
    else:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")

else:
    print("Invalid operation. Please choose one of: +, -, *, /")
