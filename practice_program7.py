"""
Write a function which takes a string as input and returns true if it contains all the numbers from 0 to 9.

containsAllNumbers("a78b9c01cd3e4526fk") = true
//Explanation: Has all the numbers 0 to 9

containsAllNumbers("abcd1") = false
//Explanation: Is not having all the numbers from 0 to 9

containsAllNumbers("123456789") = false
//Explanation: 0 is missing
"""
import string

digits = string.digits  # A string containing all the digits (0-9)

def contains_all_numbers(input_string):
    found_digits = ""  # Initialize an empty string to store the digits found in the input string
    
    for char in input_string:
        if char in digits:  # Check if the character is a digit (0-9)
            found_digits += str(char)  # If so, add it to the found_digits string
    
    return sorted(found_digits) == sorted(digits)
  
# Test cases
print(contains_all_numbers("a78b9c01cd3e4526fk"))  # Output: True
print(contains_all_numbers("abcd1"))  # Output: False
print(contains_all_numbers("123456789"))  # Output: False
