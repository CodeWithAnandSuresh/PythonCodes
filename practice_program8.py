"""
Write a function which takes a string as input and prints reversed string in 3 formats as shown below.

reverseStr("Hello Folks Lets Code") =

edoC steL skloF olleH
Code Lets Folks Hello
olleH skloF steL edoC
"""

def reverse_str(sentence):
    
    reversed_full_string = sentence[::-1] # Reverse the full string
    
    reversed_word_order = ' '.join(sentence.split()[::-1])  # Reverse the word order
    
    reversed_each_word = ' '.join(word[::-1] for word in sentence.split()) # Reverse each individual word
    
    return reversed_full_string, reversed_word_order, reversed_each_word

# Obtain the reversed outputs
output = reverse_str("Hello Folks Lets Code")

# Print each output on a separate line
print("\n".join(output))
