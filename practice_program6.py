"""
Write a function which takes a number as input & sums its digits to return a single digit.

sumDigits(123) = 6
//Explanation: 1+2+3=6

sumDigits(916) = 7
//Explanation: 9+1+6=16 => 1+6=7

sumDigits(19) = 1
"""

def sum_digits(string):
    count = 0  # Initialize the count variable to store the sum of digits
    new_count = 0  # Temporary variable to hold intermediate sums during iteration

    # Iterate over each character (digit) in the input string
    for digit in iter(string):
        count += int(digit)  # Convert the digit to an integer and add it to the count

    # Perform the iterative summing process until the count becomes a single-digit number
    while len(str(count)) > 1:
        new_count = count  # Store the current count in a temporary variable
        count = 0  # Reset the count variable for the next iteration

        # Iterate over each digit in the new_count (converted to string)
        for digit in iter(str(new_count)):
            count += int(digit)  # Convert the digit to an integer and add it to the count

    return count  # Return the final sum of digits

# Prompt the user to enter a number
user_input = input("Enter a number: ")

# Calculate the sum of digits using the sum_digits function and display the result
print(f"The sum of all digits is: {sum_digits(user_input)}")
