"""
Write a function which takes a number as input and prints the pattern with samples shown.

printPattern(2)
*
* *
*

printPattern(3)
*
* *
* * *
* *
*
"""

def print_pattern(number):
    pattern = ""
    
    for i in range(1, number + 1):
        pattern += "*" * i + "\n"  # Append the line of asterisks to the pattern
        
        if i == number:
            for j in range(i - 1, 0, -1):
                pattern += "*" * j  # Append the line of asterisks (reversed) to the pattern
                
                if j != 1:
                    pattern += "\n"  # Add a newline character if it's not the last line
    return pattern

user_input = int(input("Enter the number: "))  # Prompt the user to enter the number
pattern_output = print_pattern(user_input)  # Get the pattern output
print(pattern_output)  # Print the pattern
