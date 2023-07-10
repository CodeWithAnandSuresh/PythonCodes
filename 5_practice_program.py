"""
Imagine you have a task where you need to develop a Python program that can identify and display any repeated words in a given string. 
How would you approach this task?
"""
def find_repeated_words(string):
    words = string.split()  # Split the input string into individual words
    word_frequency = {}  # Dictionary to store the frequency of each word
    repeated_words = []  # List to store the repeated words
    
    # Iterate through each word in the string
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1  # Increment the frequency count if the word is already in the dictionary
        else:
            word_frequency[word] = 1  # Add the word to the dictionary with an initial frequency of 1
        
        # Check if the word has a frequency greater than 1 and has not already been added to the repeated_words list
        if word_frequency[word] > 1 and word not in repeated_words:
            repeated_words.append(word)  # Add the repeated word to the repeated_words list
    
    return repeated_words

# Example usage
input_string = input("Enter a string: ")
repeated_words = find_repeated_words(input_string)
if len(repeated_words) > 0:
    print("Repeated words:", ", ".join(repeated_words))
else:
    print("No repeated words found in the string.")
