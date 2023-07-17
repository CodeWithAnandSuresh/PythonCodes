"""
Question: Swap the two numbers

Input:
num1 = 10
num2 = 20

Expected Output:
num1 = 20
num2 = 10
"""
# METHOD1: USING A TEMP PLACEHOLDER
# Input dynamic numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Printing the value of num1 and num2 before swapping
print(f"The value of num1 before swap: {num1}")
print(f"The value of num2 before swap: {num2}")

# Using a temporary variable as a place-holder to swap the values
temp = num1
num1 = num2
num2 = temp

# Printing the values of num1 and num2 after swapping
print(f"The value of num1 before swap: {num1}")
print(f"The value of num2 before swap: {num2}")
# ---------------------------------------------------------------------

# METHOD2: WITHOUT USING A TEMP PLACEHOLDER
# Input dynamic numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Printing the value of num1 and num2 before swapping
print(f"The value of num1 before swap: {num1}")
print(f"The value of num2 before swap: {num2}")

# Swapping the values of num1 and num2 without a temp variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

# Printing the values of num1 and num2 after swapping
print(f"The value of num1 before swap: {num1}")
print(f"The value of num2 before swap: {num2}")
