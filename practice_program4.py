"""
Count Words in a String: 

Write a function that takes a string as input and counts the number of words in it.
"""

def count_words(string_input):
    """
    Count the number of words in the input string.

    Args:
        string_input (str): The input string to count the words from.

    Returns:
        int: The number of words in the string.
    """
    # Split the input string into words based on whitespace
    words = string_input.split()

    # Return the number of words in the string
    return len(words)

# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Count the words in the input string
word_count = count_words(input_string)

# Display the result
print("Number of words:", word_count)
