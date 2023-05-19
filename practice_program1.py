# 1. Reverse a String: Write a function to reverse a given string WITHOUT using any built-in string reversal functions.

def reverse_string(input_string):
    reversed_string = ''  # Initialize an empty string to store the reversed string
    for i in range(len(input_string) - 1, -1, -1):
        # Iterate over the indices of the input string in reverse order
        # and concatenate each character to the reversed_string
        reversed_string += input_string[i]
    return reversed_string

user_input = input("Enter a string to reverse: ")
print(reverse_string(user_input))
